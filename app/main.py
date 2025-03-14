from parser import DocParser
from summarizer import Summarizer
from conversation import Conversation
from textwrap import fill
from shutil import get_terminal_size

class PaperPal:
    def __init__(self):
        print("\nHey welcome to PaperPal! You can give me your files in .pdf, .txt and even .docx formats! I'll do my best to help you understand :)")

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
            print("\033[91mSummary:\033[0m ",fill(summary.summary, width=(get_terminal_size().columns - 10)))

        del summary

        choice = input("\nDo you want to talk about this paper more? (Y/N): ").strip()

        if choice.lower() == 'y':
            print("\nYou can type 'quit' to exit the conversation. Enter your queries and I'll answer them :)")

            response = Conversation(document.text)

            while True:
                prompt = input("\n\033[94mYou:\033[0m ")

                if prompt == "quit":
                    del response
                    break

                print("\n\033[92mPaperPal:\033[0m", fill(response.converse(prompt), width=(get_terminal_size().columns - 10)))
            

        print("\n\033[92mPaperPal:\033[0m Bye, Have a good day!")
        return
        

if __name__ == "__main__":
    try:
        app = PaperPal()
        app.run()
    except KeyboardInterrupt:
        print("\n\033[92mPaperPal:\033[0m Bye, Have a good day!")