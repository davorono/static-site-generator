from leafnode import LeafNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_code = "code"
text_type_italic = "italic"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text="", text_type="", url=""):
        self.text = text
        self.text_type = text_type
        self.url = url

    def get_text(self):
        return self.text

    def get_text_type(self):
        return self.text_type
    
    def get_url(self):
        return self.url

    def __eq__(self, other):
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.get_text_type() == text_type_text:
        return LeafNode(value=text_node.get_text())
    elif text_node.get_text_type() == text_type_bold:
        return LeafNode(tag="b", value=text_node.get_text())
    elif text_node.get_text_type() == text_type_italic:
        return LeafNode(tag="i", value=text_node.get_text())
    elif text_node.get_text_type() == text_type_code:
        return LeafNode(tag="code", value=text_node.get_text())
    elif text_node.get_text_type() == text_type_link:
        return LeafNode(tag="a", value=text_node.get_text(), props={"href": text_node.get_url()})
    elif text_node.get_text_type() == text_type_image:
        return LeafNode(tag="img", value="", props={"src": text_node.get_url(), "alt": text_node.get_text()})
    else:
        raise ValueError(f"Invalid text type: {text_node.get_text_type()}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        split_delimiter = []

        if old_node.get_text_type() != text_type_text:
            new_nodes.append(old_node)
            continue
        
        split_delimiter.extend(old_node.get_text().split(delimiter))

        # If there aren't an odd amount of nodes, you must be missing a closing delimiter
        if len(split_delimiter) % 2 == 0:
            raise ValueError(f"Missing closing {delimiter}")

        # Elements at even indices must be text nodes and at odd indices they must be $text_type nodes. Think about it.
        for i in range(len(split_delimiter)):
            if split_delimiter[i] == "":
                continue
            if (i % 2 == 0):
                new_nodes.append(TextNode(split_delimiter[i], "text"))
            else:
                new_nodes.append(TextNode(split_delimiter[i], text_type))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.get_text_type() != text_type_text:
            new_nodes.append(old_node)
            continue

        text_strings = re.split(r"!\[.*?\]\(.*?\)", old_node.get_text())
        image_tuples = extract_markdown_images(old_node.get_text())

        for i in range(len(image_tuples)):
            new_nodes.append(TextNode(text_strings.pop(0), text_type_text))
            image_tuple = image_tuples.pop(0)
            new_nodes.append(TextNode(image_tuple[0], text_type_image, image_tuple[1]))

        # Append the remaining possible text strings, if its not an empty node (image node was at the end of the text string)
        if text_strings[0] != "":
            new_nodes.append(TextNode(text_strings[0], text_type_text))

        # Because of how the split occurs when declaring text_strings, it is possible for an empty string to exist at either the beginning or end of the list in the case that the splitting delimiter is at the end or beginning of the string. These cases are handled with the above if statement and the following one.
        if new_nodes[0].get_text() == "":
            new_nodes.pop(0)
        
    return new_nodes

        




def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.get_text_type() != text_type_text:
            new_nodes.append(old_node)
            continue
        
        text_strings = re.split(r"\[.*?\]\(.*?\)", old_node.get_text())
        link_tuples = extract_markdown_links(old_node.get_text())
        
        for i in range(len(link_tuples)):
            new_nodes.append(TextNode(text_strings.pop(0), text_type_text))
            link_tuple = link_tuples.pop(0)
            new_nodes.append(TextNode(link_tuple[0], text_type_link, link_tuple[1]))
        
        if text_strings[0] != "":
            new_nodes.append(TextNode(text_strings[0], text_type_text))

        # Because of how the split occurs when declaring text_strings, it is possible for an empty string to exist at either the beginning or end of the list in the case that the splitting delimiter is at the end or beginning of the string. These cases are handled with the above if statement and the following one.
        if new_nodes[0].get_text() == "":
            new_nodes.pop(0)

    return new_nodes
            




















