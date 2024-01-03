import markdown

class MarkdownConvert:
    def __init__(self, content):
        self.content = content
    
    def convert(self):
        return markdown.markdown(self.content)