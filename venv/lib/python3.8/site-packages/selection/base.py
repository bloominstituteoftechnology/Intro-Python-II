import logging
from weblib.const import NULL
from weblib.error import DataNotFound, RequiredDataNotFound
from weblib.text import normalize_space as normalize_space_func
from weblib.html import decode_entities
from weblib.text import find_number
from weblib import rex as rex_tools

__all__ = ['Selector', 'SelectorList', 'RexResultList']
logger = logging.getLogger('selection.base')
XPATH_CACHE = {}


class Selector(object):
    __slots__ = ('_node',)

    def __init__(self, node):
        self._node = node

    def node(self):
        return self._node

    def select(self, query):
        return self._wrap_node_list(self.process_query(query), query)

    def _wrap_node_list(self, nodes, query):
        selector_list = []
        for node in nodes:
            selector_list.append(self.__class__(node))
        return SelectorList(selector_list, self.__class__, query)

    def is_text_node(self):
        raise NotImplementedError

    def html(self, encoding='unicode'):
        raise NotImplementedError

    def attr(self, key, default=NULL):
        raise NotImplementedError

    def text(self, smart=False, normalize_space=True):
        raise NotImplementedError

    def number(self, default=NULL, ignore_spaces=False,
               smart=False, make_int=True):
        try:
            return find_number(self.text(smart=smart),
                               ignore_spaces=ignore_spaces,
                               make_int=make_int)
        except IndexError:
            if default is NULL:
                raise
            else:
                return default

    def rex(self, regexp, flags=0):
        norm_regexp = rex_tools.normalize_regexp(regexp, flags)
        matches = list(norm_regexp.finditer(self.html()))
        return RexResultList(matches, source_rex=norm_regexp)


class SelectorList(object):
    __slots__ = ('selector_list', 'origin_selector_class', 'origin_query')

    def __init__(self, selector_list, origin_selector_class, origin_query):
        self.selector_list = selector_list
        self.origin_selector_class = origin_selector_class
        self.origin_query = origin_query

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __getitem__(self, x):
        return self.selector_list[x]

    def __len__(self):
        return self.count()

    def count(self):
        return len(self.selector_list)

    def one(self, default=NULL):
        try:
            return self.selector_list[0]
        except IndexError:
            if default is NULL:
                m = 'Could not get first item for %s query of class %s'\
                    % (self.origin_query, self.origin_selector_class.__name__)
                raise DataNotFound(m)
            else:
                return default

    def node(self, default=NULL):
        try:
            return self.one().node()
        except IndexError:
            if default is NULL:
                m = 'Could not get first item for %s query of class %s'\
                    % (self.origin_query, self.origin_selector_class.__name__)
                raise DataNotFound(m)
            else:
                return default

    def text(self, default=NULL, smart=False, normalize_space=True):
        try:
            sel = self.one()
        except IndexError:
            if default is NULL:
                raise
            else:
                return default
        else:
            return sel.text(smart=smart, normalize_space=normalize_space)

    def text_list(self, smart=False, normalize_space=True):
        result_list = []
        for item in self.selector_list:
            result_list.append(item.text(normalize_space=normalize_space,
                                         smart=smart))
        return result_list

    def html(self, default=NULL, encoding='unicode'):
        try:
            sel = self.one()
        except IndexError:
            if default is NULL:
                raise
            else:
                return default
        else:
            return sel.html(encoding=encoding)

    def inner_html(self, default=NULL, encoding='unicode'):
        try:
            sel = self.one()
        except IndexError:
            if default is NULL:
                raise
            else:
                return default
        else:
            result_list = [item.html(encoding=encoding) for item in sel.select('./*')]
            return ''.join(result_list).strip()

    def number(self, default=NULL, ignore_spaces=False,
               smart=False, make_int=True):
        """
        Find number in normalized text of node which matches the given xpath.
        """

        try:
            sel = self.one()
        except IndexError:
            if default is NULL:
                raise
            else:
                return default
        else:
            return sel.number(ignore_spaces=ignore_spaces, smart=smart,
                              default=default, make_int=make_int)

    def exists(self):
        """
        Return True if selector list is not empty.
        """

        return len(self.selector_list) > 0

    def require(self):
        """
        Raise RequiredDataNotFound if selector data does not exist.
        """

        if not self.exists():
            raise RequiredDataNotFound(
                u'Node does not exists, query: %s, query type: %s' % (
                    self.origin_query,
                    self.origin_selector_class.__name__,
                )
            )

    def attr(self, key, default=NULL):
        try:
            sel = self.one()
        except IndexError:
            if default is NULL:
                raise
            else:
                return default
        else:
            return sel.attr(key, default=default)

    def attr_list(self, key, default=NULL):
        result_list = []
        for item in self.selector_list:
            result_list.append(item.attr(key, default=default))
        return result_list

    def rex(self, regexp, flags=0, default=NULL):
        try:
            sel = self.one()
        except IndexError:
            if default is NULL:
                raise
            else:
                return default
        else:
            return sel.rex(regexp, flags=flags)

    def node_list(self):
        return [x.node() for x in self.selector_list]

    def select(self, query):
        result = SelectorList([], self.origin_selector_class,
                              self.origin_query + ' + ' + query)
        for selector in self.selector_list:
            result.selector_list.extend(selector.select(query))
        return result


class RexResultList(object):
    __slots__ = ('items', 'source_rex')

    def __init__(self, items, source_rex):
        self.items = items
        self.source_rex = source_rex

    def one(self):
        return self.items[0]

    def text(self, default=NULL):
        try:
            return normalize_space_func(decode_entities(self.one().group(1)))
        except (AttributeError, IndexError):
            if default is NULL:
                raise DataNotFound
            else:
                return default

    def number(self):
        return int(self.text())
