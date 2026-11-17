# 🍈 Melon AI

**Live demo:** https://kalif-melon-ai.streamlit.app (bring your own OpenAI key)

A personal writing assistant that drafts emails, captions, DMs and job messages in my voice.

I wrote out how I actually talk (calm, direct, short sentences, no fluff) and turned it into a system prompt. Melon uses that to write drafts I can send with little or no editing.

## Features

- Six formats: Email, Caption, DM Reply, Job Message, LinkedIn Post, Custom
- Short, medium or long drafts
- Optional extra direction like "a bit warmer" or "mention I'm free Monday"
- One-click copy of the draft
- Works with a key from secrets, an environment variable, or pasted into the sidebar

## Stack

`Python` `Streamlit` `OpenAI API (gpt-4o-mini)`

## Run it

```bash
pip install -r requirements.txt
streamlit run ai.py
```

Add your OpenAI key one of three ways:

1. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and paste your key
2. Set `OPENAI_API_KEY` in your environment
3. Paste it into the sidebar when the app opens

`secrets.toml` is gitignored, so your key never gets committed.

## Make it sound like you

Edit the `VOICE` text at the top of `ai.py`. Describe how you write and what you avoid.

---

Built by **Kalif Abu** · [LinkedIn](https://linkedin.com/in/kalifabu)
