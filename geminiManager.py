import os;
from google import genai;

from dotenv import load_dotenv;

import jsonManager;

load_dotenv();

GEMINI_KEY = os.getenv("GEMINI_KEY");
CLIENT = genai.Client(api_key = GEMINI_KEY);

def requestGemini(prompt: str) -> str:
    try:
        response = CLIENT.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt);

        jsonManager.add("gemini", response.text);

        return response.text;
    except Exception as e:
        print("Gemini API error:", e);

        if getattr(e, "code", None) == 503:
            return "Gemini is temporarily unavailable. Please try again later.";

    return f"An error occurred: {e}";