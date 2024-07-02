from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    tn = TextNode("This is a text node", "link", "https://boot.dev")

    hn = HTMLNode("p", "I like turtles", [], {"href": "https://www.google.com", "target": "_blank"})

    # Testing regular usage of leafnode object
    ln = LeafNode("p", "hello!", {"href": "https://www.google.com", "target": "_blank"})




if __name__ == "__main__":
    main()
