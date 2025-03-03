import google.generativeai as genai
import os

API_KEY = os.getenv("LLM_API_KEY")

class Summarizer:
    def __init__(self, text):
        self.summary = self.summarise(text)

    def summarise(self, text):
        genai.configure(api_key=API_KEY)

        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        response = model.generate_content(f'Please summarize the following text in a nice manner: {text}')

        return response.text