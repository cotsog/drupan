# -*- coding: utf-8 -*-
import unittest

from drupan.config import Config
from drupan.site import Site
from drupan.inout.filesystem import Reader, ImageParser


class TestReader(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.config.reader = "filesystem"
        self.config.options = {
            "reader": {
                "directory": "foo",
                "extension": "md"
            }
        }

        self.site = Site()

    def test_parse_file(self):
        """should add an entity to site.entities"""
        reader = Reader(self.site, self.config)

        # test input - meta["foo"] = "bar" and raw = "baz"
        raw = """
        foo: bar
        ---
        baz"""

        reader.parse_file(raw)
        entity = self.site.entities[0]

        self.assertEqual(entity.meta["foo"], "bar")
        self.assertEqual(entity.raw, "baz")

    def test_init(self):
        """should add a dot before the extension"""
        reader = Reader(self.site, self.config)
        self.assertEqual(reader.extension, ".md")


class TestImageParser(unittest.TestCase):
    def test_parsing(self):
        parser = ImageParser()
        parser.feed('<p><img src="foo.jpg" /></p>')

        self.assertEqual(len(parser.images), 1)
        self.assertEqual(parser.images[0], "foo.jpg")
