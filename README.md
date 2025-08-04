# Melon AI – Your Personal Writing Assistant

Melon AI is a personal writing assistant trained on my real tone, personality, and communication style. It was built using Streamlit and OpenAI, and designed to help me write emails, captions, messages, and replies that sound exactly like me.

## 🔧 Tech Stack
- Python
- Streamlit
- OpenAI GPT-3.5 API

## 💡 Features
- Generates emails, captions, DMs, and job messages in my tone
- Uses real WhatsApp data to train the writing voice
- Web-based UI built with Streamlit
- Can be extended with memory, scheduling, and voice input

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run ai.py
```

## ⚠️ API Key

To use this, create a `.streamlit/secrets.toml` file with your own OpenAI key:

```toml
openai_api_key = "your-api-key-here"
```

## 👨🏾‍💻 Built by Kalif Abu  
LinkedIn: [@kalifabu](https://linkedin.com/in/kalifabu)