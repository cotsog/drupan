#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))
from drupan import url


class ContentObject(object):
    """test object"""
    def __init__(self):
        self.slug = None
        self.meta = {
            'title': "-This! Is? A#/ Test\&   Slug-",
            'date': datetime.now(),
            'bar': "bar",
        }
        self.path = "foo/bar/"
        self.foo = "foo"
        self.url_scheme = "%foo/$bar"


class ValidURLTest(unittest.TestCase):
    def test_slug(self):
        co = ContentObject()
        slug = "this-is-a-test-slug"
        url._generate_slug(co)
        self.assertEqual(slug, co.slug)

    def test_url(self):
        co = ContentObject()
        base = "http://www.domain.tld/"
        final_url = "http://www.domain.tld/foo/bar/"
        url._generate_url(co, base)
        self.assertEqual(final_url, co.url)

    def test_path(self):
        co = ContentObject()
        final_path = "foo/bar/"
        url._generate_path(co)
        self.assertEqual(final_path, co.path)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
