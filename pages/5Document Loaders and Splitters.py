import os
import openai
import tempfile
import streamlit as st
from langchain.text_splitter import Language
from langchain.document_loaders import CSVLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

st.set_page_config(
    page_title="Learn LangChain | Document Loaders and Text Splitters",
    page_icon="✂️"
)

st.header('✂️ Document Loaders and Text Splitters')

st.write('''
One of the most revolutionary concept in the AI world, is having LLM to interact with our proprietary
data. In the previous section we have seen how LLM applications need content to be provided in the
form of embeddings, and to generate embeddings we need to first load content into our app. LangChain
provides convenient classes and methods to load various types of documents and transform them to fit
our application's needs.
''')

st.subheader('Document Loaders')

st.write('''
To handle different types of documents in a straightforward way, LangChain provides several document
loader classes. With document loaders we are able to load external files in our application, and we
will heavily rely on this feature to implement AI systems that work with our own proprietary data,
which are not present within the model default training. To load a document, usually we just need
a few lines of code, for example: 
''')

st.code('''
from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader('sample-csv-file.csv')
data = loader.load()
''')

st.code('''
from langchain.document_loaders import UnstructuredHTMLLoader

loader = UnstructuredHTMLLoader("index.html")
data = loader.load()
''')

st.write('''
Let's see these and a few more loaders in action to really understand the purpose and the value
of using document loaders in comparison to other built-in Python methods.
''')

st.subheader('TextLoader')

sample_txt_file = st.file_uploader("Upload a TXT file", type=["txt"])

if sample_txt_file is not None:

    with tempfile.NamedTemporaryFile(delete=False) as temporary_file:

        temporary_file.write(sample_txt_file.read())

    loader = TextLoader(temporary_file.name)

    st.write(loader.load())

    # clean-up the temporary file
    os.remove(temporary_file.name)

st.subheader('CSVLoader')

sample_csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

if sample_csv_file is not None:

    with tempfile.NamedTemporaryFile(delete=False) as temporary_file:

        temporary_file.write(sample_csv_file.read())

    loader = CSVLoader(temporary_file.name)

    st.write(loader.load())

    # clean-up the temporary file
    os.remove(temporary_file.name)

st.subheader('PyPDFLoader')

sample_pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if sample_pdf_file is not None:

    with tempfile.NamedTemporaryFile(delete=False) as temporary_file:

        temporary_file.write(sample_pdf_file.read())

    loader = PyPDFLoader(temporary_file.name)

    st.write(loader.load())

    # clean-up the temporary file
    os.remove(temporary_file.name)

st.write('''
If you tried to load all the different file formats, you may have noticed that the LangChain
loader basically turns the document into an object with the following structure:
''')

st.code('''
Document(page_content='the document content', metadata={'key': 'value'})
''')

st.write('''
And this is very important because having a **standardized format** for many types of documents,
allows us to easly work with many input sources at the same time, like a built-in normalization
layer. We can also see that different formats have different type of meta, so the CSV loader
preserves, row numbers, the PDF has page numbers, and most importantly we can see that CSVs
and PDFs already gets splitted into multiple documents corresponding to the number of rows/pages.
And this brings us to the next topic: Text Splitters.
''')

st.info('''
For the full list of LangChain document loaders, please consult the official documentation:
https://python.langchain.com/docs/integrations/document_loaders/
''')

st.subheader('Text Splitters')

st.write('''
Before we deep dive into Text Splitters, is important to understand why this step is critical
to work properly with custom data. Especially when we deal with unstructured data (txt, web pages,
audio transripts), we have a massive amount of content that cannot be processed by an LLM efficiently.
So we need to split it up into chunks, and also make sure that those chunks are **semantically relevant**
to get proper responses from AI systems. When we are using Vectorstores over a large dataset, our app
will need to search for the most relevant chunk(s) to pass to the LLM based on the task, and when we 
use specific LangChain [chains](https://langchain-summarization.streamlit.app/#the-map-reduce-chain)
(eg. map_reduce, refine, map_rerank), LangChain iterates over all the chunks but needs to have the
document properly split, otherwise those chains will not work.
''')

st.write('''
As simple as it seems to be, splitting is clearly a very important step and we need to master it to
build effective LangChain applications. Let's now see some Text Splitters in action, starting from the
most basic one:
''')

st.subheader('CharacterTextSplitter')

st.code('''
from langchain.text_splitter import CharacterTextSplitter

# the chunk size/overlap are deliberately low for demo purposes
text_splitter = CharacterTextSplitter(
    separator = ' ',
    chunk_size=50,
    chunk_overlap=5,
    length_function=len,
)

# simply split the text
splits = text_splitter.split_text(text)
''')

with st.form("char_textsplitter"):

    text = st.text_area("Insert some text")

    execute = st.form_submit_button("✂️ Split")

    if execute:

        text_splitter = CharacterTextSplitter(
            separator = ' ',
            chunk_size=50,
            chunk_overlap=5,
            length_function=len,
        )

        splits = text_splitter.split_text(text)

        st.write(splits)

st.subheader('RecursiveCharacterTextSplitter')

st.write('''
RecursiveCharacterTextSplitter is the recommended way to split unstructured text, because it tries
to keep all paragraphs and sentences together. Of course, we can adjust the chunk overlap based
on the type of content our app is processing.
''')

st.code('''
from langchain.text_splitter import RecursiveCharacterTextSplitter

# the chunk size/overlap are deliberately low for demo purposes
text_splitter = RecursiveCharacterTextSplitter(
    separators=["\\n\\n", "\\n", " ", ""],
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
)

# create documents back from text chunks, as LangChain default format
docs = text_splitter.create_documents([text])
''')

with st.form("recursive_textsplitter"):

    text = st.text_area("Insert some text")

    execute = st.form_submit_button("✂️ Split")

    if execute:

        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", " ", ""],
            chunk_size=100,
            chunk_overlap=20,
            length_function=len,
        )

        docs = text_splitter.create_documents([text])

        st.write(docs)

st.subheader('Language')

st.write('''
We can use the RecursiveCharacterTextSplitter in conjuction with language separators to 
properly split code and structure them into documents to perform, for example, code analysis
tasks.
''')

st.code('''
sample_php_code = """
<?php

function display_date() {
  echo date("Y-m-d");
}

function display_timestamp() {
  echo time();
}
?>
"""

php_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PHP,
    chunk_size=50,
    chunk_overlap=0
)

docs = php_splitter.create_documents([sample_php_code])
''')

st.subheader('Load and Split')

st.write('''
Remember that LangChain is all about simplicity and abstraction, in fact, we also have a convenient
`load_and_split()` method to load and generically split content at the same time. It does not work
well all the times (sepending on the source), but it's a useful one-liner to remmeber and try.
''')

st.code('''
from langchain.document_loaders import WebBaseLoader

web_loader = WebBaseLoader(url)

docs = web_loader.load_and_split()
''')

with st.form("load_and_split"):

    url = st.text_input("Insert an URL to load", placeholder="https://francescocarlucci.com/blog/thoughts-on-artificial-intelligence")

    execute = st.form_submit_button("✂️ Load and Split")

    if execute:

        web_loader = WebBaseLoader(url)

        docs = web_loader.load_and_split()

        st.write(docs)

st.divider()

st.write('A project by [Francesco Carlucci](https://francescocarlucci.com) - \
Need AI training / consulting? [Get in touch](mailto:info@francescocarlucci.com)')
