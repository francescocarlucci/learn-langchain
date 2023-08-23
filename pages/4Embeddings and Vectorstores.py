import openai
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings

st.set_page_config(
    page_title="Learn LangChain | Embeddings and Vector Stores",
    page_icon="📈"
)

st.header('📈 Embeddings and Vector Stores')

st.write('''
Embeddings are not a concept that belongs to LangChain, but they are a very important element
in the AI ecosystem and more specifically in Natural Language Processing. Every piece of
content has to be converted in an embedding in order to be "understood and processed" by a LLM.
Even when you use the ChatGPT interface, your inputs get converted (under the hood) into embeddings 
before being processed. We can think to embeddings as vector/numerical rappresentation of content.

As usual, let's make it practical with an example:
''')

st.code('''
from langchain.embeddings import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(openai_api_key=openai_key)

response = embeddings_model.embed_query(text)
''')

openai_key = st.text_input("OpenAI Api Key")

with st.form("embedding"):

    text = st.text_input("Insert some text to be converted into an embedding")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

        embeddings_model = OpenAIEmbeddings(openai_api_key=openai_key)

        response = embeddings_model.embed_query(text)

        st.json(response)

st.write('''
In the previous example, we converted a single piece of text into am embedding, but remember that
LLMs are able to interact with almost any kind of content, as long as we are able to convert it 
into an embedding. We can work with images, videos, PDFs and even 3rd party proprietary formats.
''')

st.subheader('Vector stores')

st.write('''
Another very important concept in LangChain is the vector store. Just like embedding are vector
rappresentaion of data, vector stores are ways to store embeddings and interact with them running
queries and operations. Vector stores can be databases (eg: Pinecone, Vectara) or simply in-memory
indexes (eg: DocArrayInMemorySearch). Vector databases are ofter referred as "long term memory"
for Artificial Intelligence, because of course the data stored is persistent.
''')

st.write('''
In the "Hands-on Projects" section, we will see some sample application which makes good use of
embeddings, document loaders and vector stores.
''')

st.divider()

st.write('A project by [Francesco Carlucci](https://francescocarlucci.com) - \
Need AI training / consulting? [Get in touch](mailto:info@francescocarlucci.com)')