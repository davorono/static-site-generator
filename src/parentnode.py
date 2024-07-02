from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if (self.tag == None):
            raise ValueError
        else: 
            html_repr = f"<{self.tag}>"
            for child in self.children:
                html_repr = html_repr + child.to_html()
            html_repr = html_repr + f"</{self.tag}>"
            return html_repr
