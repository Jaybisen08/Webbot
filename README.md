# 🤖 Groq QnA ChatBot

<div align="center">

✨ *An AI-powered chatbot built using Streamlit & Groq API* ✨

</div>

---

## 📌 Description

**Groq QnA ChatBot** is a simple yet powerful AI chatbot that allows users to ask questions and receive instant AI-generated responses through an interactive chat interface.  

Built using **Python**, **Streamlit**, and **Groq API**, this project is beginner-friendly and demonstrates how Large Language Models (LLMs) can be integrated into modern web applications.

---

# 🚀 Features

✨ Interactive Chat Interface  
⚡ Fast AI Responses using Groq API  
🧠 AI-powered Question Answering  
🎨 Clean and Beginner-Friendly UI  
💻 Lightweight & Easy to Run  

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| 🐍 Python | Backend Logic |
| 🎈 Streamlit | Web Interface |
| 🤖 Groq API | AI Model Integration |

---

# 📂 Project Structure

```bash
📦 Groq-QnA-ChatBot
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

---

## 2️⃣ Create Virtual Environment (Optional)

### 🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 🐧 Linux / 🍎 Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a `requirements.txt` file and add:

```txt
streamlit
groq
```

---

# 🔑 Setup API Key

Replace this line:

```python
api_key=api_key
```

with your actual Groq API key:

```python
api_key="YOUR_API_KEY"
```

🔗 Get your API key here:  
https://console.groq.com/keys

---

# ▶️ Run the Application

```bash
streamlit run webbot.py
```

---

# 💻 Source Code

```python
import streamlit as st
from groq import Groq

llm = Groq(api_key=api_key)

st.subheader("Grooq QnA ChatBot")

query = st.chat_input(placeholder="ask anything....")

if query:
    st.chat_message("user").markdown(query)

    response = llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role":"user", "content": query}
        ]
    )

    finalAnswer = response.choices[0].message.content
    st.chat_message("ai").markdown(finalAnswer)
```

---

# 🌟 Future Improvements

🔹 Add Chat History  
🔹 Multiple AI Model Support  
🔹 Voice Input Support  
🔹 Better UI/UX Design  
🔹 Dark Mode  

---

# 📸 Screenshots

📷 Add your project screenshots here.

---

# 👨‍💻 Author

### Jay Bisen

💡 *Passionate about AI, ML & Web Development*

---

# 📄 License

📝 This project is licensed under the **MIT License**.

---

<div align="center">

⭐ If you like this project, don't forget to star the repository! ⭐

</div>
