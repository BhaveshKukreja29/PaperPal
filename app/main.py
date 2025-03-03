from parser import DocParser
from summarizer import Summarizer

class PaperPal:
    def __init__(self):
        print("Hey welcome to PaperPal! You can give me your files in PDF, Docx, txt and even images! I'll do my best to help you understand :)")

    def run(self):
        path = input("\nPlease enter the file path of your file: ").strip()
        print()

        document = DocParser(path)

        if document.text == "":
            print("I think the file path was invalid or the permissions weren't enough or the file doesn't even exist")
            print("Please double check or try some other formats :)")

        else:
            summary = Summarizer(document.text)
            print(summary.summary)

if __name__ == "__main__":
    app = PaperPal()
    app.run()