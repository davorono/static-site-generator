import unittest
from block_markdown import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic(self):
        md = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        self.assertEqual(markdown_to_blocks(md), [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ])
    def test_ends_in_newlines(self):
        md = "\n\nText\n\nhere\n\n"
        self.assertEqual(markdown_to_blocks(md), [
            "Text",
            "here"
        ])


