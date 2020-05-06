import os
import mock
import sys
import shutil
import tempfile
from pyramid.compat import NativeIO
from player import script as layer
from player.layer import ID_LAYER

from base import BaseTestCase


class TestPlayerCommand(BaseTestCase):

    def setUp(self):
        super(TestPlayerCommand, self).setUp()

        self.dir = tempfile.mkdtemp()
        self.stdout = sys.stdout
        sys.stdout = self.out = NativeIO()

    def tearDown(self):
        shutil.rmtree(self.dir)
        sys.stdout = self.stdout
        super(TestPlayerCommand, self).tearDown()

    @mock.patch('player.script.bootstrap')
    def test_no_params(self, m_bs):
        m_bs.return_value = {'registry': self.registry}

        sys.argv[:] = ['player', 'player.ini']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('[-l [LAYERS [LAYERS ...]]]', val)
        self.assertIn('[-lt [TEMPLATES [TEMPLATES ...]]]', val)

    @mock.patch('player.script.bootstrap')
    def test_list_categories_no_layers(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.registry[ID_LAYER] = {}

        sys.argv[:] = ['player', 'player.ini', '-l']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('No layers are found.', val)

    @mock.patch('player.script.bootstrap')
    def test_list_categories(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.config.add_layer(
            'test1', path='player:tests/dir1/')
        self.config.add_layer(
            'test2', path='player:tests/bundle/')

        sys.argv[:] = ['player', 'player.ini', '-l']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('* Layer: test1', val)
        self.assertIn('* Layer: test2', val)

    @mock.patch('player.script.bootstrap')
    def test_list_categories_limit(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.config.add_layer(
            'test1', path='player:tests/dir1/')
        self.config.add_layer(
            'test2', path='player:tests/bundle/')

        sys.argv[:] = ['player', 'player.ini', '-l', 'test2']

        layer.main()

        val = self.out.getvalue()
        self.assertNotIn('* Layer: test1', val)
        self.assertIn('* Layer: test2', val)

    @mock.patch('player.script.bootstrap')
    def test_list_templates(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.config.add_layer(
            'test1', path='player:tests/dir1/')
        self.config.add_layer(
            'test2', path='player:tests/bundle/')

        def test(): pass

        self.config.add_tmpl_filter(
            'test1:actions', test)

        sys.argv[:] = ['player', 'player.ini', '-lt']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('* Layer: test1', val)
        self.assertIn('player:tests/dir1/', val)
        self.assertIn('actions: .jinja2 (test_script.py: test)', val)
        self.assertIn('* Layer: test2', val)

    @mock.patch('player.script.bootstrap')
    def test_list_templates_limit(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.config.add_layer(
            'test1', path='player:tests/dir1/')
        self.config.add_layer(
            'test2', path='player:tests/bundle/')

        sys.argv[:] = ['player', 'player.ini', '-lt', 'test1']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('* Layer: test1', val)
        self.assertIn('player:tests/dir1/', val)
        self.assertIn('actions: .jinja2', val)
        self.assertNotIn('* Layer: test2', val)

    @mock.patch('player.script.bootstrap')
    def test_list_templates_no_layers(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.registry[ID_LAYER] = {}

        sys.argv[:] = ['player', 'player.ini', '-lt']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('No layers are found.', val)

    @mock.patch('player.script.bootstrap')
    def test_customize_template_fmt_bad(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.registry[ID_LAYER] = {}

        sys.argv[:] = ['player', 'player.ini', '-c', 'test', './']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('Template format is wrong.', val)

    @mock.patch('player.script.bootstrap')
    def test_customize_template_no_layers(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.registry[ID_LAYER] = {}
        sys.argv[:] = ['player', 'player.ini', '-c', 'test:template.lt', './']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('Layer "test" could not be found.', val)

    @mock.patch('player.script.bootstrap')
    def test_customize_template_no_template(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.config.add_layer(
            'test', path='player:tests/dir1/')

        sys.argv[:] = ['player', 'player.ini', '-c', 'test:template.lt', './']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('Template "test:template.lt" could not be found.', val)

    @mock.patch('player.script.bootstrap')
    def test_customize_template_no_dest(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.config.add_layer(
            'test', path='player:tests/dir1/')

        sys.argv[:] = ['player', 'player.ini', '-c',
                       'test:view.lt', './blah-blah-blah']

        layer.main()

        val = self.out.getvalue()
        self.assertIn('Destination directory is not found.', val)

    @mock.patch('player.script.bootstrap')
    def test_customize_success(self, m_bs):
        m_bs.return_value = {'registry': self.registry}
        self.config.add_layer(
            'test', path='player:tests/dir1/')

        sys.argv[:] = ['player', 'player.ini', '-c', 'test:view.lt', self.dir]

        layer.main()

        self.assertTrue(os.path.join(self.dir, 'view.jinja2'))
