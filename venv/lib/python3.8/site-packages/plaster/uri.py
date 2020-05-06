from collections import OrderedDict
import os.path

from .compat import (
    urlencode,
    urlparse,
)
from .exceptions import InvalidURI


class PlasterURL(object):
    """
    Represents the components of a URL used to locate a
    :class:`plaster.ILoader`.

    :ivar scheme: The name of the loader backend.

    :ivar path: The loader-specific path string.
        This is the entirety of the ``config_uri`` passed to
        :func:`plaster.parse_uri` without the scheme, fragment and options.
        If this value is falsey it is replaced with an empty string.

    :ivar options: A dictionary of options parsed from the query string as
        url-encoded key=value pairs.

    :ivar fragment: A loader-specific default section name.
        This parameter may be used by loaders in scenarios where they provide
        APIs that support a default name. For example, a loader that provides
        ``get_wsgi_app`` may use the fragment to determine the name of the
        section containing the WSGI app if none was explicitly defined.
        If this value is falsey it is replaced with an empty string.

    """

    def __init__(self, scheme, path='', options=None, fragment=''):
        self.scheme = scheme
        if not path:
            path = ''
        self.path = path
        if options is None:
            options = {}
        self.options = options
        if not fragment:
            fragment = ''
        self.fragment = fragment

    def __str__(self):
        result = '{0.scheme}://{0.path}'.format(self)
        if self.options:
            result += '?' + urlencode(self.options)
        if self.fragment:
            result += '#' + self.fragment
        return result

    def __repr__(self):
        return 'PlasterURL(\'{0}\')'.format(self)


def parse_uri(config_uri):
    """
    Parse the ``config_uri`` into a :class:`plaster.PlasterURL` object.

    ``config_uri`` can be a relative or absolute file path such as
    ``development.ini`` or ``/path/to/development.ini``. The file must have
    an extension that can be handled by a :class:`plaster.ILoader`
    registered with the system.

    Alternatively, ``config_uri`` may be a :rfc:`1738`-style string.

    """
    if isinstance(config_uri, PlasterURL):
        return config_uri

    # force absolute paths to look like a uri for more accurate parsing
    # we throw away the dummy scheme later and parse it from the resolved
    # path extension
    isabs = os.path.isabs(config_uri)
    if isabs:
        config_uri = 'dummy://' + config_uri

    # check if the uri is actually a url
    parts = urlparse.urlparse(config_uri)

    # reconstruct the path without the scheme and fragment
    path = urlparse.ParseResult(
        scheme='',
        netloc=parts.netloc,
        path=parts.path,
        params='',
        query='',
        fragment='',
    ).geturl()
    # strip off leading //
    if path.startswith('//'):
        path = path[2:]

    if parts.scheme and not isabs:
        scheme = parts.scheme

    else:
        scheme = os.path.splitext(path)[1]
        if scheme.startswith('.'):
            scheme = scheme[1:]

        # tag uris coming from file extension as file+scheme
        if scheme:
            scheme = 'file+' + scheme

    query = parts.query if parts.query else None
    options = OrderedDict()
    if query:
        options.update(urlparse.parse_qsl(query))
    fragment = parts.fragment if parts.fragment else None

    if not scheme:
        raise InvalidURI(config_uri, (
            'Could not determine the loader scheme for the supplied '
            'config_uri "{0}"'.format(config_uri)))

    return PlasterURL(
        scheme=scheme,
        path=path,
        options=options,
        fragment=fragment,
    )
