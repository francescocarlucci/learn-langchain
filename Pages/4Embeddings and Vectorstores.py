import openai
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings

st.header('📈 Embeddings and Vectorstores')

st.write('''
Embeddings are not a concept that belongs to LangChain, but more in general are a very important
element in the AI ecosystem and more specifically in Natural Language Processing systems. Every
content that has to be "understood" and processed by a LLM, has to be converted in an embedding,
which in short is a vector/numerical rappresentation of that content.

As usual, let's make it practical with an example:
''')

openai_key = st.text_input("OpenAI Api Key")

with st.form("embedding"):

    text = st.text_input("Insert some text to be converted into an embedding")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

        embeddings_model = OpenAIEmbeddings(openai_api_key=openai_key)

        response = embeddings = embeddings_model.embed_query(text)

        st.json(response)