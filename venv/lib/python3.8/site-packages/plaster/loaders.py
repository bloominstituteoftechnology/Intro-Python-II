import pkg_resources

from .exceptions import (
    LoaderNotFound,
    MultipleLoadersFound,
)
from .interfaces import ILoaderInfo
from .uri import parse_uri


def get_sections(config_uri):
    """
    Load the list of named sections.

    .. code-block:: python

        sections = plaster.get_sections('development.ini')
        full_config = {
            section: plaster.get_settings('development.ini', section)
            for section in sections
        }

    :param config_uri: Anything that can be parsed by
        :func:`plaster.parse_uri`.

    :returns: A list of section names in the config file.

    """
    loader = get_loader(config_uri)
    return loader.get_sections()


def get_settings(config_uri, section=None, defaults=None):
    """
    Load the settings from a named section.

    .. code-block:: python

        settings = plaster.get_settings(...)
        print(settings['foo'])

    :param config_uri: Anything that can be parsed by
        :func:`plaster.parse_uri`.

    :param section: The name of the section in the config file. If this is
        ``None`` then it is up to the loader to determine a sensible default
        usually derived from the fragment in the ``path#name`` syntax of the
        ``config_uri``.

    :param defaults: A ``dict`` of default values used to populate the
        settings and support variable interpolation. Any values in ``defaults``
        may be overridden by the loader prior to returning the final
        configuration dictionary.

    :returns: A ``dict`` of settings. This should return a dictionary object
        even if no data is available.

    """
    loader = get_loader(config_uri)
    return loader.get_settings(section, defaults)


def setup_logging(config_uri, defaults=None):
    """
    Execute the logging configuration defined in the config file.

    This function should, at least, configure the Python standard logging
    module. However, it may also be used to configure any other logging
    subsystems that serve a similar purpose.

    :param config_uri: Anything that can be parsed by
        :func:`plaster.parse_uri`.

    :param defaults: A ``dict`` of default values used to populate the
        settings and support variable interpolation. Any values in ``defaults``
        may be overridden by the loader prior to returning the final
        configuration dictionary.

    """
    loader = get_loader(config_uri)
    return loader.setup_logging(defaults)


def get_loader(config_uri, protocols=None):
    """
    Find a :class:`plaster.ILoader` object capable of handling ``config_uri``.

    :param config_uri: Anything that can be parsed by
        :func:`plaster.parse_uri`.

    :param protocols: Zero or more :term:`loader protocol` identifiers that
        the loader must implement to match the desired ``config_uri``.

    :returns: A :class:`plaster.ILoader` object.
    :raises plaster.LoaderNotFound: If no loader could be found.
    :raises plaster.MultipleLoadersFound: If multiple loaders match the
        requested criteria. If this happens, you can disambiguate the lookup
        by appending the package name to the scheme for the loader you wish
        to use. For example if ``ini`` is ambiguous then specify
        ``ini+myapp`` to use the ini loader from the ``myapp`` package.

    """
    config_uri = parse_uri(config_uri)
    requested_scheme = config_uri.scheme

    matched_loaders = find_loaders(requested_scheme, protocols=protocols)

    if len(matched_loaders) < 1:
        raise LoaderNotFound(requested_scheme, protocols=protocols)

    if len(matched_loaders) > 1:
        raise MultipleLoadersFound(
            requested_scheme, matched_loaders, protocols=protocols)

    loader_info = matched_loaders[0]
    loader = loader_info.load(config_uri)
    return loader


def find_loaders(scheme, protocols=None):
    """
    Find all loaders that match the requested scheme and protocols.

    :param scheme: Any valid scheme. Examples would be something like ``ini``
        or ``ini+pastedeploy``.

    :param protocols: Zero or more :term:`loader protocol` identifiers that
        the loader must implement. If ``None`` then only generic loaders will
        be returned.

    :returns: A list containing zero or more :class:`plaster.ILoaderInfo`
        objects.

    """
    # build a list of all required entry points
    matching_groups = ['plaster.loader_factory']
    if protocols:
        matching_groups += [
            'plaster.{0}_loader_factory'.format(proto)
            for proto in protocols
        ]
    scheme = scheme.lower()

    # if a distribution is specified then it overrides the default search
    parts = scheme.split('+', 1)
    if len(parts) == 2:
        try:
            distro = pkg_resources.get_distribution(parts[0])
        except pkg_resources.DistributionNotFound:
            pass
        else:
            ep = _find_ep_in_dist(distro, parts[1], matching_groups)

            # if we got one or more loaders from a specific distribution
            # then they override everything else so we'll just return them
            if ep:
                return [EntryPointLoaderInfo(ep, protocols)]

    # find any distributions supporting the default loader protocol
    possible_entry_points = [
        ep
        for ep in pkg_resources.iter_entry_points('plaster.loader_factory')
        if scheme is None or scheme == ep.name.lower()
    ]
    distros = {ep.dist for ep in possible_entry_points}
    matched_entry_points = list(filter(None, [
        _find_ep_in_dist(distro, scheme, matching_groups)
        for distro in distros
    ]))
    return [
        EntryPointLoaderInfo(ep, protocols=protocols)
        for ep in matched_entry_points
    ]


def _find_ep_in_dist(distro, scheme, groups):
    # find the scheme's entry point in each group
    matched_entry_points = list(filter(None, [
        distro.get_entry_info(group, scheme)
        for group in groups
    ]))

    # verify that the entry point from each group points to the same factory
    if len({str(ep) for ep in matched_entry_points}) == 1:
        return matched_entry_points[0]


class EntryPointLoaderInfo(ILoaderInfo):
    def __init__(self, ep, protocols=None):
        self.entry_point = ep
        self.scheme = '{0}+{1}'.format(ep.dist.project_name, ep.name)
        self.protocols = protocols

        self._factory = None

    @property
    def factory(self):
        if self._factory is None:
            self._factory = self.entry_point.load()
        return self._factory

    def load(self, config_uri):
        config_uri = parse_uri(config_uri)
        return self.factory(config_uri)
