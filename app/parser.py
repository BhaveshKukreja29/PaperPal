from os import path
import docx
import pymupdf

class DocParser:
    def __init__(self, path):
        self.path = path
        self.text = self.extractText()
    
    def extractText(self):
        if not path.exists(self.path):
            return ""

        if self.path.endswith(".pdf") or self.path.endswith(".txt"):
            doc = pymupdf.open(self.path)
            output = ""
            for page in doc:
                output += page.get_text()
            
            return output
        
        if self.path.endswith(".docx"):
            doc = docx.Document(self.path)
            fullText = []

            for para in doc.paragraphs:
                fullText.append(para.text)

            return '\n'.join(fullText)
