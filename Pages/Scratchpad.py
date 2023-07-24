import openai
import inspect
import helpers
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

st.set_page_config(
    page_title="Learn LangChain with Frenxi",
    page_icon="📚"
)

st.header('📚 Learn LangChain with Frenxi')

st.write('''
A web app to learn and practice LangChain, a powerful framework to build LLM application faster and better.
As first step, you need to insert your own OpenAI API key as we will use OpenAI language model.
''')

openai_api_key = st.text_input("OpenAI Api Key")

st.code(inspect.getsource(helpers.get_completion))

with st.form("basic_qa"):

    prompt = st.text_input("Prompt", placeholder="What is 2+2?")

    execute = st.form_submit_button("🤓 Execute Code")

    if execute:

        response = helpers.get_completion(prompt, openai_api_key)

        st.code(response)

st.divider()

with st.form("prompt_templates"):

    template_string = """Translate the text \
    that is delimited by triple backticks \
    into a style that is {style}. \
    text: ```{text}```
    """

    prompt_template = ChatPromptTemplate.from_template(template_string)

    style = """American English \
    in a calm and respectful tone
    """

    text = st.text_area("Text to improve")

    execute = st.form_submit_button("🤓 Execute Code")

    if execute:

        chat = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

        customer_messages = prompt_template.format_messages(style=style, text=text)

        response = chat(customer_messages)

        st.code(response.content)

st.write('Built with ❤️ by [Francesco Carlucci](https://francescocarlucci.com/)')