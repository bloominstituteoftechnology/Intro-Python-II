from player.layer import ID_LAYER

from base import BaseTestCase


class TestOrder(BaseTestCase):

    _auto_include = False
    _settings = {'layer.order.test': 'l1 l2 l3'}

    def test_custom_dir(self):
        self.config.add_layer(
            'test', 'l1', path='player:tests/dir1/')
        self.config.add_layer(
            'test', 'l2', path='player:tests/bundle/dir1/')
        self.config.commit()

        storage = self.registry.get(ID_LAYER)
        self.assertIn('test', storage)
        self.assertEqual(2, len(storage['test']))
        self.assertEqual('l1', storage['test'][0]['name'])
        self.assertEqual('l2', storage['test'][1]['name'])


class TestOrderUnknown(BaseTestCase):

    _auto_include = False
    _settings = {'layer.order.test2': 'l1 l2 l3'}

    def test_custom_dir(self):
        self.config.add_layer(
            'test', 'l1', path='player:tests/dir1/')
        self.config.add_layer(
            'test', 'l2', path='player:tests/bundle/dir1/')
        self.config.commit()

        storage = self.registry.get(ID_LAYER)
        self.assertIn('test', storage)
        self.assertNotIn('test2', storage)
