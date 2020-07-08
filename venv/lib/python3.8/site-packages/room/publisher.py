#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import zmq
import time
from zmq.utils import jsonapi as json

from room.utils import log

class Publisher(object):
    '''
    ZeroMQによるPub/SubパターンのPublisherを実装するためのクラス
    
    '''
    
    def __init__(self, port, title=''):
        '''
        ソケットの作成
        @param port: 送り先ポート
        @param title: メッセージの先頭に付与される文字列、subscriberはこれを参照してパケットを取得するか破棄するかを決める
        '''
        assert isinstance(port, int), '[type error]: {0} != int'.format(port)
        assert isinstance(title, str), '[type error]: {0} != str'.format(title)
        
        self.title = title
        context = zmq.Context() # Context作成
        self._sock = context.socket(zmq.PUB) # Publish用のソケット作成
        log.logging.info(port)
        self._sock.connect("tcp://%s:%s" % ("localhost", port))
        time.sleep(1.0) # SUB は定期的に PUB に接続を見に行くので、少し待つ必要が有る

    def send(self, data, title='', method='execute'):
        '''
        メッセージをsubscriberに送信する

        @param title: メッセージの先頭に付与される文字列、subscriberはこれを参照してパケットを取得するか破棄するかを決める
        @param method: subscriberで呼び出されるメソッド名
        @param data: メッセージ本体
        '''
        assert isinstance(title, str), '[type error]: {0} != str'.format(title)
        assert isinstance(method, str), '[type error]: {0} != str'.format(method)

        if title:
            self.title = title  # send時にtitleが設定されていればその値を使用する
            
        payload = json.dumps(data, sort_keys=True) # obj を JSON 形式の str に直列化
        self._sock.send_multipart([self.title.encode('utf-8'), method.encode('utf-8'), payload])

    def stop(self):
        '''
        ソケットを閉じる

        '''
        self._sock.close()
