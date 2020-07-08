import abc

from .compat import add_metaclass


@add_metaclass(abc.ABCMeta)
class IWSGIProtocol(object):
    @abc.abstractmethod
    def get_wsgi_app(self, name=None, defaults=None):
        """
        Create a WSGI application object.

        An example application object may be:

        .. code-block:: python

            def app(environ, start_response):
                start_response(b'200 OK', [(b'Content-Type', b'text/plain')])
                yield [b'hello world\\n']

        :param name: The name of the application referenced in the config.
            If ``None`` then it should default to the
            :attr:`plaster.PlasterURL.fragment`, if available.

        :param defaults: A ``dict`` of default values used to populate the
            settings and support variable interpolation. Any values in
            ``defaults`` may be overridden by the loader prior to returning the
            final configuration dictionary.

        :raises LookupError: If a WSGI application cannot be found by the
            specified name.

        """

    @abc.abstractmethod
    def get_wsgi_app_settings(self, name=None, defaults=None):
        """
        Create a WSGI application object.

        An example application object may be:

        .. code-block:: python

            def app(environ, start_response):
                start_response(b'200 OK', [(b'Content-Type', b'text/plain')])
                yield [b'hello world\\n']

        :param name: The name of the application referenced in the config.
            If ``None`` then it should default to the
            :attr:`plaster.PlasterURL.fragment`, if available.

        :param defaults: A ``dict`` of default values used to populate the
            settings and support variable interpolation. Any values in
            ``defaults`` may be overridden by the loader prior to returning the
            final configuration dictionary.

        :raises LookupError: If a WSGI application cannot be found by the
            specified name.

        """

    @abc.abstractmethod
    def get_wsgi_filter(self, name=None, defaults=None):
        """
        Create a composable WSGI middleware object.

        An example middleware filter may be:

        .. code-block:: python

            class Filter(object):
                def __init__(self, app):
                    self.app = app

                def __call__(self, environ, start_response):
                    return self.app(environ, start_response)

        :param name: The name of the application referenced in the config.
            If ``None`` then it should default to the
            :attr:`plaster.PlasterURL.fragment`, if available.

        :param defaults: A ``dict`` of default values used to populate the
            settings and support variable interpolation. Any values in
            ``defaults`` may be overridden by the loader prior to returning the
            final configuration dictionary.

        :raises LookupError: If a WSGI filter cannot be found by the
            specified name.

        """

    @abc.abstractmethod
    def get_wsgi_server(self, name=None, defaults=None):
        """
        Create a WSGI server runner.

        An example server runner may be:

        .. code-block:: python

            def runner(app):
                from wsgiref.simple_server import make_server
                server = make_server('0.0.0.0', 8080, app)
                server.serve_forever()

        :param name: The name of the application referenced in the config.
            If ``None`` then it should default to the
            :attr:`plaster.PlasterURL.fragment`, if available.

        :param defaults: A ``dict`` of default values used to populate the
            settings and support variable interpolation. Any values in
            ``defaults`` may be overridden by the loader prior to returning the
            final configuration dictionary.

        :raises LookupError: If a WSGI server cannot be found by the
            specified name.

        """
