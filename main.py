from parser import DocParser

class PaperPal:
    def __init__(self):
        print("Hey welcome to PaperPal! You can give me your files in PDF, Docx, txt and even images! I'll do my best to help you understand :)")

    def run(self):
        path = input("\nPlease enter the file path of your file: ").strip()
        document = DocParser(path)
        text = document.extractText()
        print(f"\nThis is the text I found in your file\n\n{text}")

        if text == "":
            print("I think the file path was invalid or the permissions weren't enough or the file doesn't even exist")
            print("Please double check or try some other formats :)")


if __name__ == "__main__":
    app = PaperPal()
    app.run()