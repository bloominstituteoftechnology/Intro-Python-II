#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import defaultdict

class SPEED(object):
    '''
    Markov chain
    イベントを予測する

    '''
    def __init__(self):
        self.window = []
        self.episode = []
        self.max_episode_length = 1
        self.tree = ContextTree()
        #self.pre_learning()
    '''
    def pre_learning(self):
        data = Data()
        past_events = data.load()

        for event in past_events:
            self.execute(event)
    '''

                    
    def execute(self, event):
        '''
        @param event: ('appliance', 'method')

        '''
        self.window.append(event) # windowに追加
        e = self.opposite(event) # 逆のイベントを取得

        for i in range(0, len(self.window)-1): # windowの前から走査
            
            if self.window[i] == e: # 入力されたイベントと逆のイベントがあれば
                self.episode = self.window[i:] # 一連のエピソードを取得 ex: deABca -> ABca

                if len(self.episode) > self.max_episode_length: # エピソード長がmax_episode_lengthより長ければ更新
                    self.max_episode_length = len(self.episode)

                self.window = self.window[-(self.max_episode_length+1):] # windowを更新
                contexts = self.generate_contexts(self.episode)
                self.update_tree(contexts) # treeを更新

                return self.prediction()

    def generate_contexts(self, episode):
        '''
        episodeの中のeventの組み合わせをparam

        @羅列する episode: list
        '''
        result = []
        for i in range(0, len(episode)):
            tmp = [];
            for j in range(i, len(episode)):
                tmp.append(episode[j])
                result.append(tmp[:]) # pythonの引数は参照渡しなのでtmpを渡すと次のループで書き換えられてしまう。そのため[:]で配列をコピーして渡す

        return sorted(result, key=len)

    def update_tree(self, contexts):
        '''
        '''
        for context in contexts:
            self.tree.upsert(context)

    
    def opposite(self, event):
        '''
        入力されたイベント(家電操作・入退室)と逆のイベントを返す
        
        ex: ('viera', 'on') -> ('viera', 'off')
          :  A -> a
        '''
        #return event.swapcase() # 大文字小文字を入れ替える
        #return (event[0], 'off') if event[1] == 'on' else (event[0], 'on') # on と off の入れ替え
        return (event[0], '0') if event[1] == 1 else (event[0], '1') # on と off の入れ替え


    def calc_probability(self, event, node):
        '''
        入力されたイベントが過去の状態(tree)とcontextの下で起こる確率を計算する

        '''
        if not isinstance(node, Node):
            return 0
        
        occurrence_c  = node.occurrence # total occurrence of episodes of k-1 length
        ck = self.tree.search_child(node.children, event)
        occurrence_ck = 0 if ck == None else ck.occurrence # total occurrence φ event after exploring the current episode

        child_nodes_occurrence = sum([c.occurrence for c in node.children])
        num_c0 = node.occurrence - child_nodes_occurrence # total number of null outcomes after exploring the current episode

        if occurrence_c == 0:
            # print('{0}/{1} ) [{2}]'.format(occurrence_ck, child_nodes_occurrence, event))
            return occurrence_ck / child_nodes_occurrence
        else:
            # print('{0}/{1} + {2}/{1} ( '.format(occurrence_ck, occurrence_c, num_c0), end='')
            return (occurrence_ck / occurrence_c) + (num_c0 / occurrence_c) * self.calc_probability(event, node.parent) # Pk = ck/c + ce/c * Pk-1


    def prediction(self):
        '''
        各イベントごとに現在の状態の次に起こる確率を計算する

        '''
        events = [c.event for c in self.tree.root.children] # アトミックなイベント
        start_node = self.tree.walk(self.tree.root, self.episode)
        return [(e, self.calc_probability(e, start_node)) for e in events] # 全てのイベントに対して現在のコンテキストの後に発生する確率を計算する

    
    def recommend(self, threshold=0):
        '''
        閾値以上の確率で起こるイベントを一つ推薦する

        '''
        ranking = sorted(self.prediction(), key=lambda x:x[1], reverse=True)
        # print(ranking[:3])
        if ranking and ranking[0][1] > threshold:
            return ranking[0][0]
        else:
            return None
        
        

class ContextTree(object):
    '''
    過去の履歴を保持するためのツリー

    '''

    def __init__(self):
        self.root = Node(parent=None, event='Root', occurrence=0)

        
    def upsert(self, context):
        '''
        contextが存在していればoccurenceをインクリメント
        存在していなければtreeにnodeを追加

        '''
        target = self.trace(self.root, context)

        if isinstance(target, Node):
            target.occurrence += 1 # update
        else:
            current_node = target[0] 
            new_node = Node(parent=current_node, event=target[1])
            current_node.children.append(new_node) # insert
        
    def trace(self, node, context):
        '''
        木をたどる

        @param context: list ex: [('viera', 'on'), ('light', 'off')]
        '''
        if len(context) == 0: return node # treeの最後まで辿れた

        child = self.search_child(node.children, context[0])
        if child:
            return self.trace(child, context[1:]) # 次のノードを探索
        else:
            # contextが残っているが、次のノードが見つからなかった場合
            # 短いcontextから追加していくので、
            # nodeが見つからないcontextは必ず要素が一つになるはずなのでcontext[0]としている
            # 辿れた一番最後のnodeと残りのevent(contextシークエンスの最後)を返す
            return (node, context[0])

    def walk(self, node, episode):

        if len(episode) == 0: return node

        for child in node.children:
            if child == episode[0]:
                return self.walk(child, episode[1:])
        

    def search_child(self, children, event):
        '''
        子ノードに指定されたイベントを持つノードがあるかを判定する
        '''
        for node in children:
            if node == event: return node
        return None

            
class Node(object):
    '''
    各コンテキストの発生回数を保持する

    '''
    class_id = -1

    @classmethod
    def get_id(cls):
        cls.class_id += 1
        return cls.class_id
    
    def __init__(self, parent, event, occurrence=1):
        self.id = Node.get_id()
        self.parent = parent 
        self.children = [] 
        self.event = event
        self.occurrence = occurrence # 発生回数
        
    def __str__(self):
        #return 'id:{0}, event:{1}, occ:{2}'.format(self.id, self.event, self.occurrence)
        return '{0}-{1}-{2}'.format(self.id, self.event, self.occurrence)        
        

    def __eq__(self, event):
        '''
        if self.event[0] == event:
            return True
        else:
            return False
        '''
        if event and self.event[0] == event[0] and self.event[1] == event[1]:
            return True
        else:
            return False
        
if __name__ == "__main__":
    speed = SPEED()
    count = 0
    correct = 0
    recommend = None
    
    for line in open('data.txt'):
        line = line[:-1]
        appliance, method = line.split(' ')
        print('recommend:{0}, currnet:{1}'.format(recommend, (appliance, method)))
        if recommend == (appliance, method): correct += 1 
        count += 1
        speed.execute((appliance, method))
        recommend = speed.recommend()        
        print('correct:{0}, count:{1}'.format(correct, count))
        print('accuracy:{0}%'.format((correct / count) * 100))
        print('--------')
        
        if count > 700:
            break
        

    
    '''
    input = ['A', 'B', 'b', 'D', 'C', 'c', 'a', 'B', 'C', 'b', 'd', 'c', 'A', 'D', 'a', 'B', 'A', 'd', 'a', 'b']
    # A -> viera on
    # B -> light
    # C -> fan
    # D -> tv

    input = [('viera', 1),
             ('light', 1),
             ('light', 0),
             ('tv', 1),
             ('fan', 1),
             ('fan', 0),
             ('viera', 0),
             ('light', 1),
             ('fan', 1),
             ('light', 0),
             ('tv', 0),
             ('fan', 0),
             ('viera', 1),
             ('tv',1),
             ('viera',0),
             ('light',1),
             ('viera',1),
             ('tv',0),
             ('viera',0),
             ('light',0)]

    for i in input:
        print(speed.execute(i))
    '''
    #print(speed.calc_probability(('light', 0), speed.tree.trace(speed.tree.root, [('viera', 1), ('tv', 0), ('viera', 0)])))
    #print(speed.calc_probability('A', speed.tree.trace(speed.tree.root, 'Adabdadd')))
    #print(speed.recommend())

    
    #speed.pre_learning()
    #print(speed.prediction())

    

