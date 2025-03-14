import google.generativeai as genai
from config import getKey
import itertools
import sys
import time
import threading

class Summarizer:
    def __init__(self, text):
        genai.configure(api_key=getKey())
        self.summary = self.summarise(text)

    def spinner(self, stopEvent):
        spinner = itertools.cycle(["-", "\\", "|", "/"])

        while not stopEvent.is_set():
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")
        sys.stdout.write(" \b")
        sys.stdout.flush()

    def summarise(self, text):
        stopEvent = threading.Event()
        spinnerThread = threading.Thread(target=self.spinner, args=(stopEvent,), daemon=True)
        spinnerThread.start()

        try:
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            response = model.generate_content(f'Please summarize the following text in a nice manner: {text}')

        except:
            return "Some error occured during summarization :("
        
        stopEvent.set()
        spinnerThread.join()

        return response.text