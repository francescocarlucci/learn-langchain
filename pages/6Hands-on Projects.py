import streamlit as st

st.set_page_config(
    page_title="Learn LangChain | Hands-on Projects",
    page_icon="🙌"
)

st.header('🙌 Hands-on Projects')

st.write('''
There is no better way to learn a new language or framework than going hands-on and build
your own tools using LangChain and Artificial Intelligence! Theory is never enough, you
need to confront yourself with real-life use cases, write code, get stuck and figure out
solutions. In this section you will find some demo project I built specifically for this
course, that resemble scenarios that may come useful for many companies, or can be extended
to create interesting tools!

All the projects are open-source and you will find a link to the code on GitHub!
''')

st.info('This section is constantly updated with new projects! Make sure to come here often \
or [write me](https://twitter.com/francecarlucci) to suggest new interesting projects to build!', icon="ℹ️")

st.subheader('Demo Project #1 | Invoice Data Extractor')

st.write('https://invoice-data-extractor.streamlit.app/')

st.write('''
Manual processing for invoices belongs to the past! Just drop an invoice in this app and get
the data extracted and formatted as JSON.
''')

st.divider()

st.subheader('Demo Project #2 | Basic QA Over Custom Data')

st.write('https://langchain-basic-qna.streamlit.app/')

st.write('''
AIs know lots of information, but they do not have access to our private archives, email
conversations, chats, work documents, etc... In this demo we will see how to build a system
the can "learn" and interact with our custom data.
''')

st.divider()

st.write('A project by [Francesco Carlucci](https://francescocarlucci.com) - \
Need AI training / consulting? [Get in touch](mailto:info@francescocarlucci.com)')
