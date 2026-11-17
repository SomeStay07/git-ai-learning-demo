"""Structural check only; the actual mobile layout is checked in Chrome."""
from html.parser import HTMLParser
from pathlib import Path
import unittest


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.viewports = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'meta' and attributes.get('name') == 'viewport':
            self.viewports.append(attributes.get('content', ''))


class MobileViewportTest(unittest.TestCase):
    def test_page_declares_device_width(self):
        parser = PageParser()
        parser.feed(Path(__file__).with_name('index.html').read_text())
        self.assertEqual(parser.viewports, ['width=device-width, initial-scale=1'])


if __name__ == '__main__':
    unittest.main()
