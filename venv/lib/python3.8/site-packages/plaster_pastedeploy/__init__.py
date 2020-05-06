from collections import OrderedDict
import logging
from logging.config import fileConfig
import os
import sys

from paste.deploy import loadapp, loadserver, loadfilter, appconfig
import paste.deploy.loadwsgi as loadwsgi

from plaster import ILoader
from plaster.protocols import IWSGIProtocol

PY2 = sys.version_info[0] == 2

if PY2:
    # We need to import the **same** configparser module that PasteDeploy
    # is using so that we can catch the NoSectionError raised by it.
    #
    # Import the py2 version first to avoid name clash with the configparser
    # module on PyPI.
    # See https://github.com/Pylons/plaster_pastedeploy/issues/5
    from ConfigParser import NoSectionError
else:
    from configparser import NoSectionError


class Loader(IWSGIProtocol, ILoader):
    """
    This is a loader conforming to the required interface defined by
    :class:`plaster.ILoader`. Given a :class:`plaster.PlasterURL` to a
    configuration source, this can load and return WSGI applications,
    servers, filters and settings from .ini files written against the
    PasteDeploy spec.

    :ivar uri: A :class:`plaster.PlasterURL` instance.

    """

    filepath = None

    def __init__(self, uri):
        self.uri = uri
        scheme = get_pastedeploy_scheme(uri)
        if scheme == "config":
            self.filepath = os.path.abspath(uri.path)
        self.pastedeploy_spec = "{0}:{1}".format(scheme, uri.path)
        self.relative_to = os.getcwd()

    def get_sections(self):
        """
        Find all of the sections in the config file.

        :return: A list of the section names in the config file.

        """
        if self.filepath is None:
            return []
        parser = self._get_parser()
        return parser.sections()

    def get_settings(self, section=None, defaults=None):
        """
        Gets a named section from the configuration source.

        :param section: a :class:`str` representing the section you want to
            retrieve from the configuration source. If ``None`` this will
            fallback to the :attr:`plaster.PlasterURL.fragment`.
        :param defaults: a :class:`dict` that will get passed to
            :class:`configparser.ConfigParser` and will populate the
            ``DEFAULT`` section.
        :return: A :class:`plaster_pastedeploy.ConfigDict` of key/value pairs.

        """
        # This is a partial reimplementation of
        # ``paste.deploy.loadwsgi.ConfigLoader:get_context`` which supports
        # "set" and "get" options and filters out any other globals
        section = self._maybe_get_default_name(section)
        if self.filepath is None:
            return {}
        parser = self._get_parser(defaults)
        defaults = parser.defaults()

        try:
            raw_items = parser.items(section)
        except NoSectionError:
            return {}

        local_conf = OrderedDict()
        get_from_globals = {}
        for option, value in raw_items:
            if option.startswith("set "):
                name = option[4:].strip()
                defaults[name] = value
            elif option.startswith("get "):
                name = option[4:].strip()
                get_from_globals[name] = value
                # insert a value into local_conf to preserve the order
                local_conf[name] = None
            else:
                # annoyingly pastedeploy filters out all defaults unless
                # "get foo" is used to pull it in
                if option in defaults:
                    continue
                local_conf[option] = value
        for option, global_option in get_from_globals.items():
            local_conf[option] = defaults[global_option]
        return ConfigDict(local_conf, defaults, self)

    def get_wsgi_app(self, name=None, defaults=None):
        """
        Reads the configuration source and finds and loads a WSGI
        application defined by the entry with name ``name`` per the
        PasteDeploy configuration format and loading mechanism.

        :param name: The named WSGI app to find, load and return. Defaults to
            ``None`` which becomes ``main`` inside
            :func:`paste.deploy.loadapp`.
        :param defaults: The ``global_conf`` that will be used during app
            instantiation.
        :return: A WSGI application.

        """
        name = self._maybe_get_default_name(name)
        defaults = self._get_defaults(defaults)
        return loadapp(
            self.pastedeploy_spec,
            name=name,
            relative_to=self.relative_to,
            global_conf=defaults,
        )

    def get_wsgi_server(self, name=None, defaults=None):
        """
        Reads the configuration source and finds and loads a WSGI server
        defined by the server entry with the name ``name`` per the PasteDeploy
        configuration format and loading mechanism.

        :param name: The named WSGI server to find, load and return. Defaults
            to ``None`` which becomes ``main`` inside
            :func:`paste.deploy.loadserver`.
        :param defaults: The ``global_conf`` that will be used during server
            instantiation.
        :return: A WSGI server runner callable which accepts a WSGI app.

        """
        name = self._maybe_get_default_name(name)
        defaults = self._get_defaults(defaults)
        return loadserver(
            self.pastedeploy_spec,
            name=name,
            relative_to=self.relative_to,
            global_conf=defaults,
        )

    def get_wsgi_filter(self, name=None, defaults=None):
        """Reads the configuration soruce and finds and loads a WSGI filter
        defined by the filter entry with the name ``name`` per the PasteDeploy
        configuration format and loading mechanism.

        :param name: The named WSGI filter to find, load and return. Defaults
            to ``None`` which becomes ``main`` inside
            :func:`paste.deploy.loadfilter`.
        :param defaults: The ``global_conf`` that will be used during filter
            instantiation.
        :return: A callable that can filter a WSGI application.
        """
        name = self._maybe_get_default_name(name)
        defaults = self._get_defaults(defaults)
        return loadfilter(
            self.pastedeploy_spec,
            name=name,
            relative_to=self.relative_to,
            global_conf=defaults,
        )

    def get_wsgi_app_settings(self, name=None, defaults=None):
        """
        Return an :class:`collections.OrderedDict` representing the
        application config for a WSGI application named ``name`` in the
        PasteDeploy config file specified by ``self.uri``.

        ``defaults``, if passed, should be a dictionary used as variable
        assignments like ``{'http_port': 8080}``.  This is useful if e.g.
        ``%(http_port)s`` is used in the config file.

        If the ``name`` is None, this will attempt to parse the name from
        the ``config_uri`` string expecting the format ``inifile#name``.
        If no name is found, the name will default to "main".

        :param name: The named WSGI app for which to find the settings.
            Defaults to ``None`` which becomes ``main``
            inside :func:`paste.deploy.loadapp`.
        :param defaults: The ``global_conf`` that will be used during settings
            generation.
        :return: A :class:`plaster_pastedeploy.ConfigDict` of key/value pairs.

        """
        name = self._maybe_get_default_name(name)
        defaults = self._get_defaults(defaults)
        conf = appconfig(
            self.pastedeploy_spec,
            name=name,
            relative_to=self.relative_to,
            global_conf=defaults,
        )
        return ConfigDict(conf.local_conf, conf.global_conf, self)

    def setup_logging(self, defaults=None):
        """
        Set up logging via :func:`logging.config.fileConfig`.

        Defaults are specified for the special ``__file__`` and ``here``
        variables, similar to PasteDeploy config loading. Extra defaults can
        optionally be specified as a dict in ``defaults``.

        :param defaults: The defaults that will be used when passed to
            :func:`logging.config.fileConfig`.
        :return: ``None``.

        """
        if "loggers" in self.get_sections():
            defaults = self._get_defaults(defaults)
            fileConfig(self.uri.path, defaults, disable_existing_loggers=False)

        else:
            logging.basicConfig()

    def _get_defaults(self, defaults=None):
        result = {"__file__": self.filepath}
        if self.filepath is None:
            result["here"] = os.getcwd()
        else:
            result["here"] = os.path.dirname(self.filepath)
        result.update(self.uri.options)
        if defaults:
            result.update(defaults)
        return result

    def _get_parser(self, defaults=None):
        defaults = self._get_defaults(defaults)
        loader = loadwsgi.ConfigLoader(self.uri.path)
        loader.update_defaults(defaults)
        return loader.parser

    def _maybe_get_default_name(self, name):
        """Checks a name and determines whether to use the default name.

        :param name: The current name to check.
        :return: Either None or a :class:`str` representing the name.
        """
        if name is None and self.uri.fragment:
            name = self.uri.fragment
        return name

    def __repr__(self):
        return 'plaster_pastedeploy.Loader(uri="{0}")'.format(self.uri)


def get_pastedeploy_scheme(uri):
    scheme = "config"
    if uri.scheme.endswith("egg"):
        scheme = "egg"
    #    elif uri.scheme.startswith('call'):
    #        scheme = 'call'
    return scheme


class ConfigDict(OrderedDict, loadwsgi.AttrDict):
    def __init__(self, local_conf, global_conf, loader):
        super(ConfigDict, self).__init__(local_conf)
        self.global_conf = global_conf
        self.loader = loader

    def __reduce__(self):
        initargs = list(self.items()), self.global_conf, self.loader
        return self.__class__, initargs

    def copy(self):
        callable, args = self.__reduce__()
        return callable(*args)
