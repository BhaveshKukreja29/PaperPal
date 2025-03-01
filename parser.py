from os import path
import pymupdf
import docx

class DocParser:
    def __init__(self, path):
        self.path = path
    
    def extractText(self):
        if not path.exists(self.path):
            return ""

        if self.path.endswith(".pdf") or self.path.endswith(".txt"):

            doc = pymupdf.open(self.path)
            output = ""
            for page in doc:
                output += page.get_text()
            
            return output