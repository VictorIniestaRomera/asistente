from tkinter import *;

import os;
from google import genai;

from dotenv import load_dotenv;

import jsonManager;

def main():
    try:
        if not jsonManager.exists():
            raise Exception("File not found.");
    
        jsonManager.clear();

        load_dotenv();

        GEMINI_KEY = os.getenv("GEMINI_KEY");

        client = genai.Client(api_key = GEMINI_KEY); #Create API key in Google AI Studio.

        root = Tk();
        
        root.title("Welcome to Gemini!");
        root.geometry("500x300");
        
        lbl = Label(root, text = "Input prompt");
        lbl.grid();

        chat = Text(root, wrap = "word", state = "disabled", width = 55, height = 15);
        chat.grid(sticky = "nsew", padx = 3, pady = 1);

        chat.tag_config("user", foreground = "#3498db");
        chat.tag_config("user_name", foreground = "#5c5c5c");
        chat.tag_config("gemini", foreground="#2fc96f");
        chat.tag_config("gemini_name", foreground="#5c5c5c");

        def insertMessage(sender: str, message: str) -> None:
            if sender == "you":
                tag = "user";
            elif sender == "gemini":
                tag = "gamini";
            else:
                tag = "default";

            chat.config(state = "normal");

            chat.insert("end", f"{sender}: ", tag);
            chat.insert("end", f"{message}\n", f"{tag}_name");

            chat.config(state = "disabled");
            chat.see("end");
        
        promptEntry = Entry(root, width = 75);
        promptEntry.grid();

        def requestGemini(prompt: str) -> str:
            try:
                response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt);

                jsonManager.add("gemini", response.text);

                return response.text;
            except Exception as e:
                print("Gemini API error:", e)

                if getattr(e, "code", None) == 503:
                    return "Gemini is temporarily unavailable. Please try again later."

            return f"An error occurred: {e}"
        
        def sendClicked() -> None:
            prompt = promptEntry.get();

            if prompt.strip():
                promptEntry.delete(0, END);

                #User message
                insertMessage("you", prompt);
                jsonManager.add("you", prompt);

                #Temporary message
                insertMessage("gemini", "Thinking...");
                root.update_idletasks();

                answer = requestGemini(prompt);

                chat.config(state = "normal");
                chat.delete("end-2l", "end-1l");

                #Gemini message
                insertMessage("gemini", answer);
        
        sendButton = Button(root, text = "Send", command = sendClicked);
        sendButton.grid(row = 2, column = 1);

        def sendPressed(event) -> None:
            sendClicked();

        root.bind("<Return>", sendPressed);
        
        root.mainloop();
    except Exception as e:
        print("Error ", e);

if __name__ == "__main__":
    main();