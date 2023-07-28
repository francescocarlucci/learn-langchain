import openai
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings

st.header('📈 Embeddings and Vector stores')

st.write('''
Embeddings are not a concept that belongs to LangChain, but more in general are a very important
element in the AI ecosystem and more specifically in Natural Language Processing. Every piece of
content has to be converted in an embedding in order to be "understood and processed" by a LLM.
We can think to embeddings as vector/numerical rappresentation of some content.

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

st.subheader('Document Loaders')

st.write('''
To handle different types of documents in a straightforward way, LangChain provides several document
loader classes. With document loaders we are able to load external files in our application, adn we
will heavly rely on this feature to implement AI systems that work with our own proprietary data,
which are not existing within the model default training.

For now, let's just learn how to use Document Loaders: 
''')

st.code('''
from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path='./sample-csv-file.csv')
data = loader.load()
''')

st.code('''
from langchain.document_loaders import UnstructuredHTMLLoader

loader = UnstructuredHTMLLoader("index.html")
data = loader.load()
''')

st.write('''
For the full list of LangChain document loaders, please consult the official documentation:
https://python.langchain.com/docs/integrations/document_loaders/
''')

st.subheader('Vector stores')

st.write('''
Another very important concept in LangChain is the vector store. Just like embedding are vector
rappresentaion of data, vector stores are ways to store embeddings and interact with them running
queries and operations. Vector sotres can be databases (eg: Chroma, Pinecone) or simply in-memory
indexes (eg: DocArrayInMemorySearch). Vecotr databases are ofter referred as "long term memory"
for Artificial Intelligence.
''')

st.write('''
In the "Demo Projects" xection, we will see some sample application which makes good use of
embeddings, document loaders and vector stores.
''')