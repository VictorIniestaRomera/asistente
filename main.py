from tkinter import *;

import os;
from google import genai;

def main():
    try:
        #client = genai.Client(api_key = os.environ["GEMINI_API_KEY"]); #Create API key in Google AI Studio.
        root = Tk();
        
        root.title("Welcome to Gemini!");
        root.geometry("500x300");
        
        lbl = Label(root, text = "Input prompt");
        lbl.grid();

        chat = Text(root, wrap = "word", state = "disabled", width = 55, height = 15);
        chat.grid(sticky = "nsew", padx = 3, pady = 1);

        def insertMessage(sender: str, message: str) -> None:
            if sender == "you":
                chat.config(state="normal", fg = "black");
            elif sender == "gemini":
                chat.config(state="normal", fg = "gray");
            
            chat.insert("end", f"{sender}: {message}\n");
            chat.config(state="disabled");
            chat.see("end");
        
        promptEntry = Entry(root, width = 75);
        promptEntry.grid();
        
        def sendClicked() -> None:
            prompt = promptEntry.get();
            if prompt is not None and prompt != "":
                promptEntry.delete(0, END);

                insertMessage("you", prompt);

                #response = client.models.generate_content(model = "gemini-2.5-flash", contents = prompt);

                #insertMessage("gemini", response.text);
        
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