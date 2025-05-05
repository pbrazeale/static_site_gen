class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        
        if self.tag is None:
            return self.value
        
        if self.props is None:
            open_tag = self.tag
        else:
            open_tag = f'{self.tag}{self.props_to_html()}'
        
        return f'<{open_tag}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        
        if self.children is None or not self.children:
            raise ValueError("All children nodes must have a value")
        
        children_html = "".join([child.to_html() for child in self.children])

        if self.props is None:
            open_tag = self.tag
        else:
            open_tag = f'{self.tag}{self.props_to_html()}'

        return f"<{open_tag}>{children_html}</{self.tag}>"