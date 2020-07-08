from pyramid.exceptions import ConfigurationError
from player.layer import ID_LAYER

from base import BaseTestCase


class TestSettingsError(BaseTestCase):

    _settings = {'layer.custom': 'unknown'}
    _include = False

    def test_custom(self):
        self.assertRaises(
            ConfigurationError, self.config.include, 'player')


class TestSettingsCustom(BaseTestCase):

    _auto_include = False
    _settings = {'layer.custom': 'player:tests/bundle/'}

    def test_custom_dir(self):
        self.config.add_layer(
            'dir1', path='player:tests/dir1/')
        self.config.commit()

        storage = self.registry.get(ID_LAYER)
        self.assertIn('dir1', storage)
        self.assertEqual(2, len(storage['dir1']))
        self.assertEqual('layer_custom', storage['dir1'][0]['name'])
        self.assertEqual('', storage['dir1'][1]['name'])
