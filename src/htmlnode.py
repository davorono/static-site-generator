class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            raise ValueError

        html_repr = ""
        for propkey in self.props:
            html_repr = html_repr + f" {propkey}=\"{self.props[propkey]}\""
        return html_repr

    def __repr__(self):
        return f"({self.tag}, {self.value}, {self.children}, {self.props})"
            

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if (self.value == None):
            raise ValueError
        elif (self.tag == None):
            return self.value
        else:
            add_props = ""
            if (self.props != None):
                for key in self.props:
                    add_props = add_props + f" {key}=\"{self.props[key]}\""
                add_props.rstrip(" ")

            return f"<{self.tag}{add_props}>{self.value}</{self.tag}>"

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
