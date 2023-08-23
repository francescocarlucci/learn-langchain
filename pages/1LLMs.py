import openai
import streamlit as st
from langchain.llms import OpenAI
from langchain.llms import DeepInfra

st.set_page_config(
    page_title="Learn LangChain ! Large Language Models",
    page_icon="🤖"
)

st.header('🤖 Large Language Models (LLMs)')

st.write('''
Large Language Models (LLMs) are a type of neural network trained on a vast
amount of text data, designed to understand and generate human-like text based
on inputs received, and they are the backbone LangChain. The framework allows us
to connect and interact with all the most popular LLMs such as OpenAI, Cohere,
Hugging Face, any model hosted on Replicate, and many more.
''')

st.subheader('OpenAI LLM')

st.write('''
In this first tutorial we will see a basic example connecting with the OpenAI model
(aka ChatGPT), probably the most popular model at the time of writing. We will
instanciate it and perform a basic interaction.
''')

st.code('''
import openai
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key=openai_key, temperature=0.5)

response = llm(your_prompt)

print(response)
''')

st.info("You need your own keys to run commercial models", icon="ℹ️")

openai_key = st.text_input("OpenAI Api Key")

with st.form("openai_llm"):

    prompt = st.text_input("Prompt", placeholder="What is 2+2?")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

        llm = OpenAI(openai_api_key=openai_key, temperature=0.5)

        response = llm(prompt)

        st.code(response)

st.write('''
While it may seem trivial to abstract a simple API call to OpenAI GPT model, this
is just a basic example which serves as foundation to the most valuable LangChain
tools that will allow to build far more complex workflows. For now, let's appreciate
how we set it up using only 5 lines of code, and how easy is to plug in another model.
''')

st.subheader('DeepInfra LLM')

st.write('''
In this example, we will use the same LangChain functions but plug in a different model.
More specifically, we will use DeepInfra, which allows to run several model in the cloud.
This is why we are specifying the model_id as parameter.
''')

st.code('''
import openai
from langchain.llms import DeepInfra

llm = DeepInfra(deepinfra_api_token=deepinfra_token, model_id=model_id)

response = llm(your_prompt)

print(response)
''')

deepinfra_token = st.text_input("DeepInfra Api Key")

model_id = st.selectbox(
    'Model',
    ('google/flan-t5-small', 'databricks/dolly-v2-12b')
)

with st.form("deepinfra_llm"):

    prompt = st.text_input("Prompt", placeholder="I like salads. What do we eat today?")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

        with st.spinner('Processing your request...'):

            llm = DeepInfra(deepinfra_api_token=deepinfra_token, model_id=model_id)

            response = llm(prompt)        

            st.code(response)

st.write('''
Take some time to play with prompts and observe how different LLMs provide us so
different responses. This is why is very important to choose the right model based
on our specific needs.
''')

st.subheader('LLMs vs ChatModels')

st.write('''
LLMs in LangChain refer to text completion models (text-in/text-out). However,
some models require a more complex interface, they are trained specifically to
have conversations and they take a list of chat messages as an input. These
messages are usually labeled with the speaker (one of "System", "AI", and "Human").
For example, GPT-4 is trained as chat model, while GPT-3 as a LLM. Chat models
work very well with LangChain Prompt Templates, which we will see in the next
section.
''')

st.divider()

st.write('A project by [Francesco Carlucci](https://francescocarlucci.com) - \
Need AI training / consulting? [Get in touch](mailto:info@francescocarlucci.com)')
