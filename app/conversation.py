import google.generativeai as genai
from config import getKey
from collections import deque


class Conversation:
    def __init__(self, context):
        self.context = context
        self.key = getKey()
        self.history = deque(maxlen=5) 

    def converse(self, prompt):
        genai.configure(api_key=self.key)
        
        try:
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            response = model.generate_content(f"You are PaperPal, the best research paper analyzer. Ensure you respond only in plain text which is in readable format, no markdown. If user asks about how to exit tell them to type 'quit'. Here's the research paper text we're analyzing: {self.context} Here's history of previous chat: {self.history} The user has a query, respond to the query as accurately as possible from the given paper and history but keep it natural. Query: {prompt}")

            self.history.append(f"User: {prompt}\nPaperPal: {response.text}")

            return response.text
        
        except:
            return "Some error occured during fetching response :("