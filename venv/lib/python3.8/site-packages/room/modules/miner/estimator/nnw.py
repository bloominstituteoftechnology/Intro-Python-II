#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np

import chainer
import chainer.functions as F
import chainer.links as L
from chainer import optimizers
from chainer import serializers
from chainer import computational_graph

from room.modules.miner.estimator.nnw_data import Data
from room.utils.log import logging

class MLP(chainer.Chain):
    '''
    ネットワーク構造
    '''
    def __init__(self, n_in, n_units, n2_units, n_out):
        super(MLP, self).__init__(
            l1=L.Linear(n_in, n_units),
            l2=L.Linear(n_units, n2_units),
            l3=L.Linear(n2_units, n2_units),            
            l4=L.Linear(n2_units, n_out),
        )

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        h3 = F.relu(self.l3(h2))
        return self.l3(h3)
    

class NeuralNetWork(object):

    def __init__(self, appliance, pre_learning=False):
        self.appliance = appliance
        self.metadata_path = os.environ['PYTHONPATH'] + '/room/modules/miner/estimator/metadata/'
        self.n_in = 34    # 入力層のユニット数
        self.n_units = 10 # 隠れ層のユニット数
        self.n2_units = 5
        self.n_out = 2    # 出力層のユニット数
        self.setup_model() 
        self.setup_optimizer()
        
        if pre_learning:
            self.pre_learning() # 事前学習を行う
            self.load_model()
        
    def setup_model(self):
        self.model = L.Classifier(MLP(self.n_in, self.n_units, self.n2_units, self.n_out), F.softmax_cross_entropy)

    def setup_optimizer(self):
        self.optimizer = optimizers.Adam()        
        self.optimizer.setup(self.model)        
        
    def load_model(self):
        if os.path.exists(self.metadata_path + self.appliance + ".model"):
            print('Load model')            
            serializers.load_npz(self.metadata_path + self.appliance + ".model", self.model)        
        
    def resume(self, resume, optimizer):
        print('Load optimizer state from', resume)
        serializers.load_npz(resume, optimizer)    

    def train(self, x, t):
        # Pass the loss function (Classifier defines it) and its arguments        
        self.optimizer.update(self.model, x, t) # パラメータ更新

    def output(self, x):
        '''
        確率計算
        '''
        #return F.softmax(self.model.y).data # 先にtrainを実行している場合、model.yにforwardの結果が残ってるのでそれを利用する
        x = chainer.Variable(x)        
        return F.softmax(self.model.predictor(x)).data        

    def convert(self, probabilities, threshold=0.8):
        '''
        確率を状態に変換する
        '''
        logging.info('probability [0:{0}, 1:{1}]'.format(probabilities[0], probabilities[1]))
        
        if probabilities[0] > threshold:
            return 0
        elif probabilities[1] > threshold:
            return 1
        else:
            return None

    def predict(self, x):
        '''
        複数のデータを一度に予測できる
        @param x: 多次元配列 [[27..],[],[]] - 要素の一つ一つがnumpy.array型(要素np.float32)の配列
        @return [p]: 予測値(0, 1, None)の配列
        '''
        return [self.convert(probabilities) for probabilities in self.output(x)]
    
    def batch_training(self, x_train, y_train, batchsize):

        N = len(y_train) # データの行数
        perm = np.random.permutation(N) #randomに入れ替え
        sum_accuracy = 0
        sum_loss = 0
        
        for i in range(0, N, batchsize): # 0からNまでの数字をbatchsize間隔で生成してループ
            x = chainer.Variable(np.asarray(x_train[perm[i:i + batchsize]])) # xのミニバッチ取得
            t = chainer.Variable(np.asarray(y_train[perm[i:i + batchsize]])) # targetのミニバッチ取得
            self.train(x, t) # 学習
            sum_loss += float(self.model.loss.data) * len(t.data)
            sum_accuracy += float(self.model.accuracy.data) * len(t.data)
                
        
        print('train mean loss={}, accuracy={}'.format(
            sum_loss / N, sum_accuracy / N))
        

    def batch_evaluation(self, x_test, y_test, batchsize):
        N_test = len(y_test)
        sum_accuracy = 0
        sum_loss = 0
        
        for i in range(0, N_test, batchsize):
            x = chainer.Variable(np.asarray(x_test[i:i + batchsize]), volatile='on')
            t = chainer.Variable(np.asarray(y_test[i:i + batchsize]), volatile='on')
            loss = self.model(x, t)
            sum_loss += float(loss.data) * len(t.data)
            sum_accuracy += float(self.model.accuracy.data) * len(t.data)

        print('test mean loss={}, accuracy={}'.format(
            sum_loss/ N_test, sum_accuracy / N_test))

    def prepare_dataset(self):
        # Prepare dataset
        print('load CS27 dataset')
        data = Data()
        cs27 = data.load(self.appliance)
        cs27['data'] = cs27['data'].astype(np.float32)
        cs27['target'] = cs27['target'].astype(np.int32)

        N = round(len(cs27['data']) * 0.8)
        x_train, x_test = np.split(cs27['data'], [N])
        y_train, y_test = np.split(cs27['target'], [N])

        return x_train, y_train, x_test, y_test
        

    def batch_learning(self, n_epoch=100, batchsize=100):

        x_train, y_train, x_test, y_test = self.prepare_dataset()

        for epoch in range(1, n_epoch + 1):
            print('epoch', epoch)
            self.batch_training(x_train, y_train, batchsize)
            self.batch_evaluation(x_test, y_test, batchsize)
            
        self.save()
            
    def save(self):
        # Save the model and the optimizer
        print('save the model')
        serializers.save_npz(self.metadata_path + self.appliance + '.model', self.model)
        
        print('save the optimiezer')
        serializers.save_npz(self.metadata_path + self.appliance + '.state', self.optimizer)


    def pre_learning(self):
        if not os.path.exists(self.metadata_path + self.appliance + '.model'):
            print('start pre learning')
            self.batch_learning()
            print('end pre learning')

if __name__ == '__main__':

    appliance = 'curtain'
    
    NNW = NeuralNetWork(appliance)

    data = Data()
    cs27 = data.load_data(appliance)
    data  = cs27['data'].astype(np.float32)
    target = cs27['target'].astype(np.int32)
    
    # NNW.train(d, t) # offに偏るので全てを学習させない方が良い
    predict = [NNW.convert(probabilities) for probabilities in  NNW.output(data)]
    correct = target
    right = 0
    all = len(predict)

    for p, c in zip(predict, correct):
        if p == c:
            right +=1

    print('accuracy:{}'.format(right / all))
    
