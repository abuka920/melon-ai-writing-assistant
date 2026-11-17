"""Melon AI: a writing assistant that drafts messages in Kalif's voice.

Run with:  streamlit run ai.py
"""

import os

import streamlit as st
from openai import OpenAI

MODEL = "gpt-4o-mini"

VOICE = (
    "You are Melon AI, a writing assistant that writes like Kalif Abu. "
    "Kalif's voice is calm, direct, honest and confident. "
    "Use short declarative sentences and plain conversational words. "
    "No fluff, no hype, no exaggeration, no em dashes, no corporate filler. "
    "Return only the finished text, ready to send."
)

FORMATS = {
    "Email": "Write an email. Start with a subject line on its own line as 'Subject: ...'.",
    "Caption": "Write a social media caption. Keep it under 60 words.",
    "DM Reply": "Write a short direct message reply. Two to four sentences.",
    "Job Message": "Write a short message to a recruiter or hiring manager. Under 120 words.",
    "LinkedIn Post": "Write a LinkedIn post. Short paragraphs, no hashtag spam (three at most).",
    "Custom": "Write whatever format best fits the request.",
}

LENGTHS = {"Short": 150, "Medium": 300, "Long": 600}


def get_api_key():
    """Look for a key in Streamlit secrets, then the environment, then the sidebar."""
    try:
        key = st.secrets.get("openai_api_key")
    except Exception:  # no secrets.toml file
        key = None
    return key or os.getenv("OPENAI_API_KEY")


def build_messages(writing_type, context, tone_note):
    request = f"{FORMATS[writing_type]}\n\nContext:\n{context.strip()}"
    if tone_note.strip():
        request += f"\n\nExtra direction: {tone_note.strip()}"
    return [
        {"role": "system", "content": VOICE},
        {"role": "user", "content": request},
    ]


def generate(api_key, messages, max_tokens):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=MODEL, messages=messages, temperature=0.7, max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()


st.set_page_config(page_title="Melon AI", page_icon="🍈", layout="centered")
st.title("🍈 Melon AI")
st.caption("Your personal writing assistant. Drafts that sound like you, not like a robot.")

api_key = get_api_key()
with st.sidebar:
    st.header("Settings")
    if not api_key:
        api_key = st.text_input("OpenAI API key", type="password", help="Never stored.")
    else:
        st.success("API key loaded")
    length = st.radio("Length", list(LENGTHS), index=1, horizontal=True)

writing_type = st.selectbox("What are you writing?", list(FORMATS))
context = st.text_area("What's the context or goal?", height=150,
                       placeholder="e.g. Follow up with a recruiter I spoke to last week about the security analyst role")
tone_note = st.text_input("Anything else? (optional)", placeholder="e.g. a bit warmer, mention I'm available Monday")

if st.button("Generate", type="primary"):
    if not context.strip():
        st.warning("Give Melon some context to work with.")
    elif not api_key:
        st.error("Add your OpenAI API key in the sidebar first.")
    else:
        with st.spinner("Writing..."):
            try:
                output = generate(api_key, build_messages(writing_type, context, tone_note), LENGTHS[length])
                st.session_state["output"] = output
            except Exception as exc:
                st.error(f"Something went wrong: {exc}")

if st.session_state.get("output"):
    st.subheader("Melon's draft")
    st.write(st.session_state["output"])
    st.code(st.session_state["output"], language=None)  # code block has a copy button
