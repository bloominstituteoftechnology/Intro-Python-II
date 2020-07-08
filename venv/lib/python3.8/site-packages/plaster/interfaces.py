import abc

from .compat import add_metaclass


@add_metaclass(abc.ABCMeta)
class ILoader(object):
    """
    An abstraction over an source of configuration settings.

    It is required to implement ``get_sections``, ``get_settings`` and
    ``setup_logging``.

    Optionally, it may also implement other :term:`loader protocol` interfaces
    to provide extra functionality. For example,
    :class:`plaster.protocols.IWSGIProtocol` which requires ``get_wsgi_app``,
    and ``get_wsgi_server`` for loading WSGI configurations. Services that
    depend on such functionality should document the required functionality
    behind a particular :term:`loader protocol` which custom loaders can
    implement.

    :ivar uri: The :class:`plaster.PlasterURL` object used to find the
        :class:`plaster.ILoaderFactory`.

    """

    @abc.abstractmethod
    def get_sections(self):
        """
        Load the list of section names available.

        """

    @abc.abstractmethod
    def get_settings(self, section=None, defaults=None):
        """
        Load the settings for the named ``section``.

        :param section: The name of the section in the config file. If this is
            ``None`` then it is up to the loader to determine a sensible
            default usually derived from the fragment in the ``path#name``
            syntax of the ``config_uri``.

        :param defaults: A ``dict`` of default values used to populate the
            settings and support variable interpolation. Any values in
            ``defaults`` may be overridden by the loader prior to returning
            the final configuration dictionary.

        :returns: A ``dict`` of settings. This should return a dictionary
            object even if the section is missing.
        :raises ValueError: If a section name is missing and cannot be
            determined from the ``config_uri``.

        """

    @abc.abstractmethod
    def setup_logging(self, defaults=None):
        """
        Execute the logging configuration defined in the config file.

        This function should, at least, configure the Python standard logging
        module. However, it may also be used to configure any other logging
        subsystems that serve a similar purpose.

        :param defaults: A ``dict`` of default values used to populate the
            settings and support variable interpolation. Any values in
            ``defaults`` may be overridden by the loader prior to returning
            the final configuration dictionary.

        """


@add_metaclass(abc.ABCMeta)
class ILoaderFactory(object):
    @abc.abstractmethod
    def __call__(self, uri):
        """
        A factory which accepts a :class:`plaster.PlasterURL` and returns a
        :class:`plaster.ILoader` object.

        """


@add_metaclass(abc.ABCMeta)
class ILoaderInfo(object):
    """
    An info object describing a specific :class:`plaster.ILoader`.

    :ivar scheme: The full scheme of the loader.
    :ivar protocols: Zero or more supported :term:`loader protocol`
        identifiers.
    :ivar factory: The :class:`plaster.ILoaderFactory`.

    """

    @abc.abstractmethod
    def load(self, config_uri):
        """
        Create and return an :class:`plaster.ILoader` instance.

        :param config_uri: Anything that can be parsed by
            :func:`plaster.parse_uri`.

        """
