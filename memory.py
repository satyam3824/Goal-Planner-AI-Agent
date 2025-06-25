import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_to_memory(user_input, response):
    memory = load_memory()
    memory.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user_input,
        "ai": response
    })
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

def get_recent_memories(limit=5):
    memory = load_memory()
    return memory[-limit:]

def clear_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)
