import google.generativeai as genai
from config import getKey


class Conversation:
    def __init__(self, context):
        self.context = context
        self.key = getKey()

    def converse(self, prompt):
        genai.configure(api_key=self.key)
        
        try:
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            response = model.generate_content(f"You are the best research paper analyzer. Ensure you respond only in plain text which is in readable format, no markdown. Here's the research paper text we're analyzing: {self.context} The user has a query, respond to the query as accurately as possible from the given context. Query: {prompt}")

            return response.text
        
        except:
            return "Some error occured during fetching response :("