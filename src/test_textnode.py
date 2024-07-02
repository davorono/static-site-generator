import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node3 = TextNode("foo", "bar")
        node4 = TextNode("foo", "bar", "baz");
        self.assertNotEqual(node3, node4)

    def test_text_to_html(self):
        tn = TextNode("test", "text")
        self.assertEqual(text_node_to_html_node(tn).to_html(), "test")

    def test_bold_to_html(self):
        tn = TextNode("test", "bold")
        self.assertEqual(text_node_to_html_node(tn).to_html(), "<b>test</b>")

    def test_italic_to_html(self):
        tn = TextNode("test", "italic")
        self.assertEqual(text_node_to_html_node(tn).to_html(), "<i>test</i>")

    def test_code_to_html(self):
        tn = TextNode("test", "code")
        self.assertEqual(text_node_to_html_node(tn).to_html(), "<code>test</code>")

    def test_link_to_html(self):
        tn = TextNode("test", "link", "dog.jpg")
        self.assertEqual(text_node_to_html_node(tn).to_html(), "<a href=\"dog.jpg\">test</a>")

    def test_invalid_to_html(self):
        tn = TextNode("test", "something wrong", "dog.jpg")
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn).to_html()

    def test_missing_closing_split_nodes_delimiter(self):
        tn = TextNode("test**", "text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter([tn], "**", "bold")

    def test_basic_split_nodes_delimiter(self):
        basic_str = "this is just a text string"
        tn = TextNode(basic_str, "text")
        self.assertEqual(split_nodes_delimiter([tn], "*", "italic"), [
            TextNode(basic_str, "text")
        ])

    def test_all_bold_split_nodes_delimiter(self):
        bold_str = "this is a bold string"
        tn = TextNode(bold_str, "bold")
        self.assertEqual(split_nodes_delimiter([tn], "**", "bold"), [
            TextNode(bold_str, "bold")
        ])

    def test_many_markdown_elements_split_nodes_delimeter(self):
        bold_str = "this **is** my text with **several** bolded **elements** alright?"
        tn = TextNode(bold_str, "text")
        self.assertEqual(split_nodes_delimiter([tn], "**", "bold"), [
            TextNode("this ", "text"),
            TextNode("is", "bold"),
            TextNode(" my text with ", "text"),
            TextNode("several", "bold"),
            TextNode(" bolded ", "text"),
            TextNode("elements", "bold"),
            TextNode(" alright?", "text")
        ])

    def test_many_markdown_elements_split_nodes_delimeter_code(self):
        code_str = "this 'is' my text with **several** code 'elements' alright?"
        tn = TextNode(code_str, "text")
        self.assertEqual(split_nodes_delimiter([tn], "'", "code"), [
            TextNode("this ", "text"),
            TextNode("is", "code"),
            TextNode(" my text with **several** code ", "text"),
            TextNode("elements", "code"),
            TextNode(" alright?", "text")
        ])

    def test_end_with_markdown_split_nodes_delimiter(self):
        ends_bold_str = "this is **text** and **bold**"
        tn = TextNode(ends_bold_str, "text")
        self.assertEqual(split_nodes_delimiter([tn], "**", "bold"), [
            TextNode("this is ", "text"),
            TextNode("text", "bold"),
            TextNode(" and ", "text"),
            TextNode("bold", "bold")
        ])

    def test_extract_image(self):
        self.assertEqual(extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"),
        [('image', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')])

    def test_extract_image_empty_str(self):
        self.assertEqual(extract_markdown_images(""), [])

    def test_extract_links(self):
        self.assertEqual(extract_markdown_links("this text supposedly has [a link](https://google.com) matter of fact it has [two links](https://mynuts.com)"),
                         [('a link', 'https://google.com'), ('two links', 'https://mynuts.com')])

    def test_extract_links_empty_str(self):
        self.assertEqual(extract_markdown_links(""), [])

    def test_split_nodes_image(self):
        tn = TextNode("this has an ![image](https://pppick.png)", "text")
        self.assertEqual(split_nodes_image([tn]), [
            TextNode("this has an ", "text"),
            TextNode("image", "image", "https://pppick.png")
        ])

    def test_split_nodes_more_image(self):
        tn = TextNode("![image here](https://test.png) and also has ![another](https://test2.png) right here!", "text")
        self.assertEqual(split_nodes_image([tn]), [
            TextNode("image here", "image", "https://test.png"),
            TextNode(" and also has ", "text"),
            TextNode("another", "image", "https://test2.png")
        ])

    def test_split_nodes_non_text(self):
        tn = TextNode("hold on this is **bold**", "bold")
        self.assertEqual(split_nodes_image([tn]), [tn])

    def test_split_nodes_only_text(self):
        tn = TextNode("wait this is just text", "text")
        self.assertEqual(split_nodes_image([tn]), [tn])


if __name__ == "__main__":
    unittest.main()
