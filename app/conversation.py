import google.generativeai as genai
from config import getKey


class Conversation:
    def __init__(self, context, prompt):
        self.response = self.converse(context, prompt)

    def converse(self, context, prompt):
        API_KEY = getKey()
        genai.configure(api_key=API_KEY)
        
        try:
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            response = model.generate_content(f"You are the best research paper analyzer. Here's the research paper text we're analyzing: {context} The user has a query, respond to the query as accurately as possible from the given context. Query: {prompt}")

            return response.text
        
        except:
            return "Some error occured during fetching response :("