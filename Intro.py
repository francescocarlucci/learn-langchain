import streamlit as st

st.set_page_config(
    page_title="LangChain Crash Course",
    page_icon="📚"
)

st.header('📚 LangChain Crash Course')

st.subheader('Build apps with AI and learn by doing!')

st.write('''
LangChain is a framework to develop AI (artificial intelligence) applications in a
better and faster way. You can think about it as an abstraction layer designed to
interact with various LLM (large language models), process and persist data,
perform complex tasks and take actions using with various APIs. 
''')

st.subheader('Core Components')

st.write('''
The main components/tools that LangCHain offers to develop AI applications using LangChain are:

- LLMs (Large Language Models)
- Prompts / Parsers
- Chains
- Embeddings / Vectorstores
- Memory
- Agents 

LangChain is available for Python and JavaScript, but in this guide we will focus on the Python version.
''')

st.subheader('Why LangChain')

st.write('''
In my opinion, any technology that was adopted on a large scale it's been simplified
in some way. We are all using credit cards online but no one implements credit card
processing from scratch, most companies uses Stripe/PayPal/3rd party gateways. 90% of
websites are based on frameworks and not on plain PHP, Python, Ruby, whatever. Most
of the tech that we use today is an encapsulation layer of some other lower level
technolology, and the same goes with AI, we are building tools to lower the learning
curve and allow a faster and smoother adoption. LangChain is one if these tools!
''')

st.subheader('To learn better')

st.write('''
To better enjoy this LangChain course, you should have a basic understanding of software
development fundamentals, and ideally some experience with python. If you don't, you can
check these FreeCodeCamp resources to skill yourself up and come back!


- [Learn Python](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/)
- [Intro to Programming](https://youtu.be/zOjov-2OZ0E)
''')

st.subheader('Credits')

st.write('''
All the frameworks used in this mini-course belong to their owners:

- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [DeepInfra](https://deepinfra.com/)
''')

st.divider()

st.write('A project by [Francesco Carlucci](https://francescocarlucci.com) - \
Need AI training / consulting? [Get in touch](mailto:info@francescocarlucci.com)')
