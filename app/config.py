import os
import json

CONFIG_DIR = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def getKey():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)

            if "API_KEY" in config:
                return config["API_KEY"] 
    
    API_KEY = input("Paste your Gemini API key: ").strip()
    with open(CONFIG_FILE, "w") as f:
        json.dump({"API_KEY": API_KEY}, f)
    
    return API_KEY