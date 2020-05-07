# coding: utf-8
from __future__ import absolute_import
from unittest import TestCase
from lxml.html import fromstring
from lxml.etree import fromstring as xml_fromstring

from item.error import ItemRuntimeError
from item.item import Item
from item import func_field
from item.field import IntegerField, StringField, DateTimeField, FuncField
from weblib.etree import parse_html
from selection import XpathSelector

XML = b"""<?xml version='1.0' encoding='utf-8'?>
<bbapi version='1'>
    <player id='26982032' retrieved='2012-09-11T07:38:44Z'>
        <firstname>Ardeshir</firstname>
        <lastname>Lohrasbi</lastname>
        <nationality id='89'>Pakistan</nationality>
        <age>19</age>
        <height>75</height>
        <dmi>14300</dmi>
        <comment>abc</comment>
        <comment_cdata><![CDATA[abc]]></comment_cdata>
        <games>
            <game name="quake1"></game>
            <game name="quake2"></game>
        </games>
    </player>
</bbapi>
"""


def calculated_func2(item, sel):
    if not hasattr(item, 'count2'):
        item.count2 = 1
    else:
        item.count2 += 1
    return sel.select('//height').text() + '-zoo2-' + str(item.count2)


class Player(Item):
    id = IntegerField('//player/@id')
    first_name = StringField('//player/firstname')
    retrieved = DateTimeField('//player/@retrieved', '%Y-%m-%dT%H:%M:%SZ')
    comment = StringField('//player/comment')
    comment_cdata = StringField('//player/comment_cdata')

    data_not_found = StringField('//data/no/found')

    @func_field()
    def calculated(item, sel):
        if not hasattr(item, 'count'):
            item.count = 1
        else:
            item.count += 1
        return sel.select('//height').text() + '-zoo-' + str(item.count)

    calculated2 = FuncField(calculated_func2, pass_item=True)

    @func_field()
    def height1(item, sel):
        return sel.select('//height').number()

    height2 = FuncField(lambda sel: sel.select('//height').number())


class GameItem(Item):
    class Meta:
        find_query = '//games/game'

    name = StringField('@name')
    names = StringField('@name', multiple=True)


class ItemTestCase(TestCase):
    def get_item(self):
        return Player(xml_fromstring(XML))

    def test_integer_field(self):
        player = self.get_item()
        self.assertEquals(26982032, player.id)

    def test_string_field(self):
        player = self.get_item()
        self.assertEquals('Ardeshir', player.first_name)

    def test_datetime_field(self):
        player = self.get_item()
        self.assertEquals('2012-09-11 07:38:44', str(player.retrieved))

    def test_item_cache_feature(self):
        player = self.get_item()

        self.assertEquals('75-zoo-1', player.calculated)
        # should got from cache
        self.assertEquals('75-zoo-1', player.calculated)

        # test assigning value
        player.calculated = 'baz'
        self.assertEquals('baz', player.calculated)

        # test FuncField
        self.assertEquals('75-zoo2-1', player.calculated2)
        # should got from cache
        self.assertEquals('75-zoo2-1', player.calculated2)

    def test_func_field_decorator(self):
        player = self.get_item()
        self.assertEquals(75, player.height1)

    def test_func_field(self):
        player = self.get_item()
        self.assertEquals(75, player.height2)

    def test_get_function(self):
        func = Player.get_function('height1')
        html = '<html><body><height>3'
        self.assertEquals(3, func(XpathSelector(parse_html(html))))

        func = Player.get_function('height2')
        html = '<html><body><height>3'
        self.assertEquals(3, func(XpathSelector(parse_html(html))))

    def test_func_field_warning(self):
        """
        Test that usage of func_field decorators without "()"
        raises exception.
        """

        def foo():
            class TestItem(Item):
                @func_field
                def foo(self, sel):
                    return 'test'

        self.assertRaises(ItemRuntimeError, foo)

        def foo():
            class TestItem(Item):
                @func_field()
                def foo(self, sel):
                    return 'test'

            return TestItem(fromstring('<div></div>')).foo

        self.assertEqual('test', foo())

    def test_unknown_selector_type(self):
        class TestItem(Item):
            pass

        TestItem(None)

        self.assertRaises(ItemRuntimeError, TestItem,
                          None, selector_type='Batman Selector')

    def test_find(self):
        games = list(GameItem.find(xml_fromstring(XML)))
        self.assertEqual(['quake1', 'quake2'],
                         [x.name for x in games])

    def test_stringfield_multiple(self):
        class GameItem(Item):
            names = StringField('//game/@name', multiple=True)

        game = GameItem(xml_fromstring(XML))
        self.assertEqual(['quake1', 'quake2'], game.names)

    def test_item_inheritance(self):
        class BaseItem(Item):
            class Meta:
                find_query = '//player'

            name = StringField('firstname')
            age = IntegerField('age')

        class ChildItem(BaseItem):
            name = StringField('lastname')

        items = list(BaseItem.find(xml_fromstring(XML)))
        self.assertEqual(items[0].name, 'Ardeshir')
        self.assertEqual(items[0].age, 19)
        self.assertEqual(set(['name', 'age']), set(items[0]._fields.keys()))

        items = list(ChildItem.find(xml_fromstring(XML)))
        self.assertEqual(items[0].age, 19)
        self.assertEqual(set(['name', 'age']), set(items[0]._fields.keys()))
