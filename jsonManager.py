import json;
import os;

def exists() -> bool:
    return os.path.isfile("./chat.json");

def clear() -> None:
    try:    
        with open("chat.json", "w", encoding="utf-8") as file:
            json.dump([], file, indent=4);
    except Exception as e:
        print("Error", e);

def add(role: str, txt: str) -> None:
    try:
        with open("chat.json", "r", encoding="utf-8") as file:
            chatHistory = json.load(file);

        chatHistory.append({"role": role, "content": txt});

        with open("chat.json", "w", encoding="utf-8") as file:
            json.dump(chatHistory, file, indent=4, ensure_ascii=False);
    except Exception as e:
        print("Error", e);