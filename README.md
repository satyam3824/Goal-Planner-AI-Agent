# 🌟 Goal Planner AI Agent

An AI-powered assistant built with **Gemini 1.5 Flash**, **Streamlit**, and **LangChain** to help users set, track, and stay motivated on their goals.

---

## 🔧 Features

- ✅ AI-generated personalized goal plans  
- ✅ Memory: Tracks and shows your recent interactions  
- ✅ Clean, responsive Streamlit interface  
- ✅ Uses Google Gemini 1.5 Flash  
- ✅ Modular structure (`agent.py`, `app.py`, `memory.py`)

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Google Gemini API](https://ai.google.dev/)
- Python 3.8+

---

## 🚀 Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Goal-Planner-AI-Agent.git
cd Goal-Planner-AI-Agent
```

2. **Create and activate a virtual environment**
```bash
# Windows
python -m venv my_virtual
my_virtual\Scripts\activate

# macOS/Linux
python3 -m venv my_virtual
source my_virtual/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file and add your Gemini API key**
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

5. **Run the app**
```bash
streamlit run app.py
```

---

## 🧠 Memory Feature

- User input and AI responses are saved to `memory.json`
- Memory can be cleared from the app
- File is excluded from Git using `.gitignore`

---

## 📁 Project Structure

```
Goal-Planner-AI-Agent/
├── app.py               # Streamlit UI
├── agent.py             # LLM logic using LangChain + Gemini
├── memory.py            # Save/load chat memory
├── memory.json          # Stores conversation history
├── requirements.txt     # Python dependencies
├── .env                 # Your Gemini API key (DO NOT COMMIT)
└── README.md
```

---

## 🧾 License

This project is licensed under the **MIT License** — feel free to use and modify.

---

## ✨ Author

Built by [Your Name](https://www.linkedin.com/in/yourprofile) with 💡 using Gemini & Streamlit.
