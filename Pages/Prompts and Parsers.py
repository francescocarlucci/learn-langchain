import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

st.header('📝  Prompts and Parsers')

st.write('''
Prompts are another key component in LangChain and in general in Large Language Models.
A well structured prompt can make all the difference in getting a quality outcome from
our AI model. LangChain provides a PromptTemplate component which makes easier to
write good prompts and make them reusable using variables.
''')

st.info('Prompts engineering is one of the main reason AI is gaining popularity. As we can now use pre-trained model and take advantage from specific and concise prompts.', icon="ℹ️")

st.write('''
As usual, let's make everything more clear with a code example and a working demo. In
this case, we will set up a prompt template that will make our AI to act as a business
name consultant, and come out with name ideas with any business we want and different
styles.
''')

st.code('''
import openai
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

template = """\
You are a naming consultant for new companies.
What is a good {adjective} name for a company that makes {product}?
"""

prompt_template = ChatPromptTemplate.from_template(template)

chat = ChatOpenAI(temperature=0.9, openai_api_key=openai_key)

format_template = prompt_template.format_messages(adjective=name_type, product=business_type)

response = chat(format_template)

''')

openai_key = st.text_input("OpenAI Api Key")

with st.form("prompt_templates"):

    template = """\
	You are a naming consultant for new companies.
	What is a good {adjective} name for a company that makes {product}?
	Please reply only with the name, no comments attached.
	"""

    prompt_template = ChatPromptTemplate.from_template(template)

    name_type = st.selectbox(
    	'Name type',
    	('funny', 'serious', 'irriverent')
    )

    business_type = st.text_input("Type of business", placeholder="fruit shop, fashion atelier, ...")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

        chat = ChatOpenAI(temperature=0.9, openai_api_key=openai_key)

        format_template = prompt_template.format_messages(adjective=name_type, product=business_type)

        response = chat(format_template)

        st.code(response.content)

st.subheader('Advantages of Prompt Templates')

st.write('''
- Clarity: some prompts can be long and detailed, setting them up as template will make your code better
- Reusability: many times you will be able to reuse existing templates with a few code changes
- Simplicity: LangChain has some pre-built templates for common operations (We'll have a look at this later on)
- Better output: you can instruct the LLM to return data with specific keywords, and parse the output as structured data instead of plain text to fit you app needs
''')
