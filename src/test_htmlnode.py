# Tests HTMLNode and all of its child classes
import unittest
from htmlnode import * 

class TestHTMLNode(unittest.TestCase):
    # Testing basic functionality
    def test_props_to_html(self):
        hn = HTMLNode("p", "This is a test", [], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(hn.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_to_html(self):
        hn = HTMLNode("p", "This is a test", [], {"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(NotImplementedError):
            hn.to_html()

    # Edge cases
    def test_empty_htmlnode(self):
        hn = HTMLNode()

        # Check props_to_html behavior
        with self.assertRaises(ValueError):
            hn.props_to_html()


class TestLeafNode(unittest.TestCase):
    # Testing functionality with expected parameters
    def test_to_html(self):
        ln = LeafNode("p", "This is a test", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(ln.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">This is a test</p>")
    
    # Testing edge cases
    def test_to_html_no_value(self):
        ln_no_value = LeafNode("p", props={"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            ln_no_value.to_html()

    def test_to_html_no_tag(self):
        ln_no_tag = LeafNode(value="This is a test", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(ln_no_tag.to_html(), "This is a test")

    def test_to_html_just_value(self):
        ln_just_value = LeafNode(value="This is a test")
        self.assertEqual(ln_just_value.to_html(), "This is a test")


class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        pn_no_tag = ParentNode(children=[], props={"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            pn_no_tag.to_html()

    def test_to_html_with_many_leafnode(self):
        pn_all_leafnode = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text", props={"href": "https://www.google.com", "target": "_blank"}),
            ],
        )
        self.assertEqual(pn_all_leafnode.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_grandchild(self):
        grandchild = LeafNode("b", "grandchild")
        childnode = ParentNode("i", [grandchild])
        parentnode = ParentNode("div", [childnode])

        self.assertEqual(
            parentnode.to_html(),
            "<div><i><b>grandchild</b></i></div>"
        )

        
if __name__ == "__main__":
    unittest.main()
