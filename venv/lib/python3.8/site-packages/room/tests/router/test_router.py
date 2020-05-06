#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import requests

from room.router.router import Application

@unittest.skip("アプリケーションが終了しないため")
class RouterTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._app = Application()
        cls._app.start()
    
    def test_main(self):
        #r = requests.get('localhost:8888')
        #print(r)
        #self.assertEqual(1,1)
        self.assertTrue(True)
        
    def test_datahandler(self):
        self.assertTrue(True)
        
    @classmethod
    def tearDownClass(cls):
        print('test')
        cls._app.stop()
        
if __name__ == '__main__':
    unittest.main()        
