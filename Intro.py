import streamlit as st

st.set_page_config(
    page_title="Learn LangChain with Frenxi",
    page_icon="📚"
)

st.header('📚 Learn LangChain with Frenxi')

st.subheader('Intro')

st.write('''
LangChain is a framework to develop AI (artificial intelligence) applications in a
better and faster way. You can think about it as a modular abstraction layer designed
to  interact with various LLM (large language models), process and persist data,
take actions and interact with the app environment. 
''')

st.subheader('Core Components')

st.write('''
The main components/tools that we will use to develop AI applications using LangChain are:

- LLMs (Large Language Models)
- Prompts / Parsers
- Chains
- Loaders
- Memory
- Agents 

It's available fomr Python and JavaScript, but in this guide we will focus on the Python package.
''')

st.subheader('Why LangChain')

st.write('''
In my opinion, any technology that was adopted on a large scale it's been facilitated
in some way. We are all using credit cards online but no one implements credit card
processing from scratch, most companies uses Stripe/PayPal/Bank Gateways. 90% of websites
are based on frameworks and not on plain PHP, Python, Ruby, whatever. The same goes with
AI, we are building tools to lower the learning curve and allow a faster adoption.
''')

st.divider()

st.write('Built with ❤️ by [Francesco Carlucci](https://francescocarlucci.com/)')