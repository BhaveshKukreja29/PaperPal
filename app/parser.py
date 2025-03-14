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
            with pymupdf.open(self.path) as doc:
                output = ""
                for page in doc:
                    output += page.get_text()
            
            #print("\nFile ka maal: ", output, "\n\n")
            return output
        
        if self.path.endswith(".docx"):
            with docx.Document(self.path) as doc:
                fullText = []

                for para in doc.paragraphs:
                    fullText.append(para.text)

            return '\n'.join(fullText)
