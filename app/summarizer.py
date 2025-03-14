import google.generativeai as genai
from config import getKey

class Summarizer:
    def __init__(self, text):
        genai.configure(api_key=getKey())
        self.summary = self.summarise(text)

    def summarise(self, text):
        try:
            model = genai.GenerativeModel(model_name='gemini-1.5-flash')
            response = model.generate_content(f'Please summarize the following text in a nice manner: {text}')

            return response.text
        except:
            return "Some error occured during summarization :("