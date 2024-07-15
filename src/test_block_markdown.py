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


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "this is just a paragraph block"
        self.assertEqual(block_to_block_type(block), "paragraph")
    def test_heading(self):
        block = "### this is a triple heading block"
        self.assertEqual(block_to_block_type(block), "heading")
    def test_code(self):
        block = "```this\nis\na\ncode block```"
        self.assertEqual(block_to_block_type(block), "code")
    def test_code(self):
        block = "> this is a quote block"
        self.assertEqual(block_to_block_type(block), "quote")
    def test_unordered_list(self):
        block = "* this is an unordered list\n- this is the second line\n* this is the third line\n- this is the fourth line"
        self.assertEqual(block_to_block_type(block), "unordered_list")
    def test_bad_unordered_list(self):
        block = "* this is a deceptive\nunordered list because its actually not"
        self.assertEqual(block_to_block_type(block), "paragraph")
    def test_ordered_list(self):
        block = "1. This is 1\n2. This is 2\n3. This is 3\n4. This is 4"
        self.assertEqual(block_to_block_type(block), "ordered_list")
