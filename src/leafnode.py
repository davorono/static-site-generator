from htmlnode import HTMLNode

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
        

