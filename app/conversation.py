import google.generativeai as genai
from config import getKey
from collections import deque
import itertools
import sys
import time
import threading


class Conversation:
    def __init__(self, context):
        self.context = context
        self.history = deque(maxlen=5) 
        genai.configure(api_key=getKey())

    def spinner(self, stopEvent):
        spinner = itertools.cycle(["-", "\\", "|", "/"])

        while not stopEvent.is_set():
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")
        sys.stdout.write(" \b")
        sys.stdout.flush()


    def converse(self, prompt):
        stopEvent = threading.Event()
        spinnerThread = threading.Thread(target=self.spinner, args=(stopEvent,))
        spinnerThread.start()

        try:
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            response = model.generate_content(f"You are PaperPal, the best research paper analyzer. Ensure you respond only in plain text which is in readable format, no markdown. If user asks about how to exit tell them to type 'quit'. Here's the research paper text we're analyzing: {self.context} Here's history of previous chat: {self.history} The user has a query, respond to the query as accurately as possible from the given paper and history but keep it natural. Query: {prompt}")
        
        except:
            return "Some error occured during fetching response :("
        
        stopEvent.set()
        spinnerThread.join()

        self.history.append(f"User: {prompt}\nPaperPal: {response.text}")
        return response.text
        