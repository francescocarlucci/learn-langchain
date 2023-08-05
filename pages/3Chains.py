import openai
import streamlit as st
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain

st.set_page_config(
    page_title="Learn LangChain | Chains",
    page_icon="🔗"
)

st.header('🔗 Chains')

st.write('''
Now that we have a good understanding of LLMs and Prompt Templates, we are ready to
introduce chains, the most important core component of LangChain. Chains are pre-built
classes that allow us to combine LLMs and Prompts together, with a modular approach
designed to facilitate the creation of complex language processing pipelines while
keeping our codebase solid and readable.

LangChain provides chains for the most
common operations (routing, sequential execution, document analysis) as well as
advanced chains for working with custom data, handling memory and so on. Also, we
will see more advanced LangChain features (tokenizers, transformers, embeddings)
that are much easier to use with chains.
''')

st.subheader('Our first basic Chain')

st.code('''
llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.9)

prompt = ChatPromptTemplate.from_template(\'''
I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}?\
The name should honor the film story as it is. Please limit your answer to the name only.\
If you don't know the movie, answer: "I don't know this movie"
\''')

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run(movie)
''')

openai_key = st.text_input("OpenAI Api Key")

with st.form("basic_chain"):

    movie = st.text_input("Movie", placeholder="The Green Mile")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

    	with st.spinner('Processing your request...'):

	        llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.9)

	        prompt = ChatPromptTemplate.from_template('''
	        I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}?\
	        The name should honor the film story as it is. Please limit your answer to the name only.\
	        If you don't know the movie, answer: "I don't know this movie"
	        ''')

	        chain = LLMChain(llm=llm, prompt=prompt)

	        response = chain.run(movie)

	        st.code(response)

st.write('''
This basic Chain is not very different from the Prompt Template approach, but let's move forward to
some more complex example where we can explore the adavntages and the simplicity that chains bring us.
''')

st.subheader('Sequential Chain')

st.write('''
What about if we want to use multiple LLMs interactions and use the output of the first run as the
input for the second chain? This is a perfect scenario to use the Sequential Chain.

In this new example, we will ask our LLM to write a brief advertisement of our newly generated movie
title, using the movie title as an input.
''')

st.code('''
llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.9)

first_prompt = ChatPromptTemplate.from_template(\'''
I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}?\
The name should honor the film story as it is. Please limit your answer to the name only.\
If you don't know the movie, answer: "I don't know this movie"
\''')

first_chain = LLMChain(llm=llm, prompt=first_prompt, output_key="movie_title")

second_prompt = ChatPromptTemplate.from_template(\'''
Can you write a short advertisement of this new movie including his title {movie_title}?\
Please limit it to 20 wprds and return only the advertisement copy.
\''')

second_chain = LLMChain(llm=llm, prompt=second_prompt, output_key="trailer")

sequential_chain = SequentialChain(
    chains=[first_chain, second_chain],
    input_variables=["movie"],
    output_variables=["movie_title", "trailer"],
    verbose=True
)

response = sequential_chain(movie)
''')

with st.form("sequential_chain"):

    movie = st.text_input("Movie", placeholder="The Green Mile")

    execute = st.form_submit_button("🚀 Execute")

    if execute:

    	with st.spinner('Processing your request...'):

	        llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.9)

	        first_prompt = ChatPromptTemplate.from_template('''
	        I want you to act as a movie creative. Can you come up with an alternative name for the movie {movie}?\
	        The name should honor the film story as it is. Please limit your answer to the name only.\
	        If you don't know the movie, answer: "I don't know this movie"
	        ''')

	        first_chain = LLMChain(llm=llm, prompt=first_prompt, output_key="movie_title")

	        second_prompt = ChatPromptTemplate.from_template('''
	        Can you write a short advertisement of this new movie including his title {movie_title}?\
	        Please limit it to 20 wprds and return only the advertisement copy.
	        ''')

	        second_chain = LLMChain(llm=llm, prompt=second_prompt, output_key="trailer")

	        sequential_chain = SequentialChain(
			    chains=[first_chain, second_chain],
			    input_variables=["movie"],
			    output_variables=["movie_title", "trailer"]
			)

	        response = sequential_chain(movie)

	        st.json(response)

st.info("Couldn't we just ask for the title and the description in the first chain?", icon="❓")

st.write('''
We could, but implementing it in steps offer several advantages:
- better debugging and more control over the LLM responses
- better responses due to more concise and specific prompts
- more flexibility if we want dynamically assign new steps to different chains (Router Chain)
''')

st.subheader('To keep in mind:')

st.write('''
LangChain provides an impressive amount of chains with several level of complexity and different
purposes. Studying them all can be overwhelming, but we will be using several of them in our
hands-on tutorials, making it more fun to learn in a more practical context.
''')

st.divider()

st.write('A project by [Francesco Carlucci](https://francescocarlucci.com) - \
Need AI training / consulting? [Get in touch](mailto:info@francescocarlucci.com)')
