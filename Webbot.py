
import streamlit as st
from groq import Groq

llm = Groq(api_key=api_key)

st.subheader("Grooq QnA ChatBot")

query = st.chat_input(placeholder="ask anything....")
if query:
    st.chat_message("user").markdown(query)

    response = llm.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages=[
            {"role":"user", "content": query}
        ]
    )
    finalAnswer = response.choices[0].message.content
    st.chat_message("ai").markdown(finalAnswer)
