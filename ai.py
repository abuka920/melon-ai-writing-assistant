import streamlit as st
import openai

openai.api_key = st.secrets.get("openai_api_key", "YOUR_OPENAI_API_KEY")

st.set_page_config(page_title="Melon AI - Writing Assistant", layout="centered")
st.title("Melon AI - Your Personal Writing Assistant")
st.write("Enter what you want to write and Melon will respond in your tone.")

writing_type = st.selectbox("What are you writing?", ["Email", "Caption", "DM Reply", "Job Message", "Custom"])
context = st.text_area("What's the context or goal?", height=150)

if st.button("Generate"):
    if context.strip() == "":
        st.warning("Please enter some context for Melon to work with.")
    else:
        prompt = f"You are Melon AI, a personal assistant trained to write like Kalif. You write with calm, direct, honest, and confident tone. Keep it clear and natural. No fluff, no exaggeration. Write a {writing_type.lower()} based on the following context:\n\n{context}\n\nRespond in Kalif's voice."

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes in Kalif's voice. Respond clearly and concisely."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            output = response['choices'][0]['message']['content'].strip()
            st.subheader("Melon's Response")
            st.write(output)
            st.code(output, language='markdown')
        except Exception as e:
            st.error(f"Something went wrong: {e}")