from parser import DocParser
from summarizer import Summarizer
from conversation import Conversation

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
            return

        else:
            summary = Summarizer(document.text)
            print(summary.summary)

        choice = input("Do you want to talk about this paper more? (Y/N):").strip()

        if choice.lower() == 'y':
            print("\nYou can type 'quit' to exit the conversation. Enter your queries and I'll answer them :)\n")

            response = Conversation(document.text)

            while True:
                prompt = input("You: ")

                if prompt == "quit": break

                print("\n\nPaperPal:", response.converse(prompt))
            

        print("PaperPal: Bye, Have a good day!")
        return
        

if __name__ == "__main__":
    app = PaperPal()
    app.run()