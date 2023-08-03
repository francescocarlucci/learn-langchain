import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

st.set_page_config(
    page_title="Learn LangChain | Prompts and Parsers",
    page_icon="📝"
)

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
- Clarity: some prompts can be long and detailed, setting them up as template will make your code better.
- Reusability: many times you will be able to reuse existing templates with a few code changes.
- Simplicity: LangChain has some pre-built templates for common operations (We'll have a look at this later on).
- Security: by limiting user control to the needed inputs, we minimize the risk of misusing our LLM.
- Output: you can instruct the LLM to return data with specific keywords, and parse the output as structured data instead of plain text to fit you app needs.

This last point brings us to the next LangChain component: output parsers.
''')

st.subheader('Output Parsers')

st.write('''
By default, LLMs return responses as plain text which is not very useful when developing complex applications
that have to interpret the data and take decisions based on those outputs. Fortunately, LangChain provides 
useful output parser classes which play well with prompts templates and can convert text data in any format we
need based on custom lofic and instructions. Let's see an example:
''')

st.code('''
import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

satisfied = ResponseSchema(name="satisfied", description="Was the customer satisfied with the service provided? Answer True if yes, False if no, null if unclear.")
keywords = ResponseSchema(name="keywords", description="Extract any adjective to satisfaction, dissatisfaction, value provided, issues related to the service provided, and output them as a comma separated list. Please, limit this list to the 3 most relevant.")
response_schemas = [satisfied, keywords]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

review_template = """\
The following text is a review from a customer reviewing a service
provided by a developer, extract the following information:

satisfied: Was the customer satisfied with the service provided? \
Answer True if yes, False if no, null if unclear.

keywords: Extract any adjective to satisfaction, dissatisfaction, value provided, \
issues related to the service provided, and output them as a comma separated list. \
Please, limit this list to the 3 most relevant.

Format the output as JSON with the following keys:
satisfied
keywords

text: {text}

{format_instructions}
"""

prompt_template = ChatPromptTemplate.from_template(template=review_template)

chat = ChatOpenAI(temperature=0, openai_api_key=openai_key)

format_template = prompt_template.format_messages(text=review_text, format_instructions=format_instructions)

response = chat(format_template)

output_dict = output_parser.parse(response.content)
''')

st.write('''
In this demo, we are asking our AI to act as our Q&A department. His duties are to evaluate if
our customer is happy with the service provided by reading his review, extract the 3 most relevant
keywords related to the service provided and most importantly, return the data as structured JSON
to be usable in our application logic.
''')

satisfied = ResponseSchema(name="satisfied", description="Was the customer satisfied with the service provided? Answer True if yes, False if no, null if unclear.")

keywords = ResponseSchema(name="keywords", description="Extract any adjective to satisfaction, dissatisfaction, value provided, issues related to the service provided, and output them as a comma separated list. Please, limit this list to the 3 most relevant.")

response_schemas = [satisfied, keywords]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

with st.form("output_parsers"):

    review_template = """\
    The following text is a review from a customer reviewing a service
    provided by a developer, extract the following information:

    satisfied: Was the customer satisfied with the service provided? \
    Answer True if yes, False if no, null if unclear.

    keywords: Extract any adjective to satisfaction, dissatisfaction, value provided, \
    issues related to the service provided, and output them as a comma separated list. \
    Please, limit this list to the 3 most relevant.

    Format the output as JSON with the following keys:
    satisfied
    keywords

    text: {text}

    {format_instructions}
    """

    prompt_template = ChatPromptTemplate.from_template(template=review_template)

    review_text = st.text_area("Customer review")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

        chat = ChatOpenAI(temperature=0, openai_api_key=openai_key)

        format_template = prompt_template.format_messages(text=review_text, format_instructions=format_instructions)

        response = chat(format_template)

        output_dict = output_parser.parse(response.content)

        st.json(output_dict)

st.divider()

st.write('A project by [Francesco Carlucci](https://francescocarlucci.com) - \
Need AI training / consulting? [Get in touch](mailto:info@francescocarlucci.com)')
