import six
from weblib.etree import get_node_text, render_html
from weblib.text import normalize_space as normalize_space_func
from weblib.const import NULL
from weblib.error import DataNotFound

from selection.base import Selector
from selection.error import SelectionRuntimeError

__all__ = ['XpathSelector', 'PyquerySelector']
XPATH_CACHE = {}
REGEXP_NS = 'http://exslt.org/regular-expressions'


class LxmlNodeSelector(Selector):
    __slots__ = ()

    def is_text_node(self):
        return isinstance(self.node(), six.string_types)

    def select(self, query=None):
        if self.is_text_node():
            raise SelectionRuntimeError('Text node selectors do not '
                                        'allow select method')
        return super(LxmlNodeSelector, self).select(query)

    def html(self, encoding='unicode'):
        if self.is_text_node():
            return self.node()
        else:
            return render_html(self.node(), encoding=encoding)

    def attr(self, key, default=NULL):
        if self.is_text_node():
            raise SelectionRuntimeError('Text node selectors do not '
                                        'allow attr method')
        if default is NULL:
            if key in self.node().attrib:
                return self.node().get(key)
            else:
                raise DataNotFound(u'No such attribute: %s' % key)
        else:
            return self.node().get(key, default)

    def text(self, smart=False, normalize_space=True):
        if self.is_text_node():
            if normalize_space:
                return normalize_space_func(self.node())
            else:
                return self.node()
        else:
            return get_node_text(self.node(), smart=smart,
                                 normalize_space=normalize_space)


class XpathSelector(LxmlNodeSelector):
    __slots__ = ()

    def process_query(self, query):
        from lxml.etree import XPath

        if query not in XPATH_CACHE:
            obj = XPath(query, namespaces={'re': REGEXP_NS})
            XPATH_CACHE[query] = obj
        xpath_obj = XPATH_CACHE[query]

        result = xpath_obj(self.node())

        # If you query XPATH like //some/crap/@foo="bar" then xpath function
        # returns boolean value instead of list of something.
        # To work around this problem I just returns empty list.
        # This is not great solutions but it produces less confusing error.
        if isinstance(result, bool):
            result = []

        if isinstance(result, six.string_types):
            result = [result]

        return result


class PyquerySelector(LxmlNodeSelector):
    __slots__ = ()

    def pyquery_node(self):
        from pyquery import PyQuery

        return PyQuery(self.node())

    def process_query(self, query):
        return self.pyquery_node().find(query)


#class CssSelector(XpathSelector):
#    __slots__ = ()
#
#    def process_query(self, query):
#        from cssselect import HTMLTranslator
#
#        xpath_query = HTMLTranslator().css_to_xpath(query) 
#        return super(CssSelector, self).process_query(xpath_query)
