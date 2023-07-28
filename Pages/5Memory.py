import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

st.header('💡 Memory')

st.write('''
LLMs are stateless by default, meaning that they have no built-in memory. But sometimes
we need memory to implement applications such like conversational systems, which may have
to remember previous information provided by the user. Fortunately, LangChain provides
several memory management solutions, suitable for different use cases.

We have seen beofre as vectorstores are referred as long-term memory, instead, the methods
we will see in this secion are considered short-term memory, as they do not persist after
the interactions are complete.
''')

st.subheader('ConversationBufferMemory')

st.write('''
This is the most basic mempry class and basically what it does, is to include previous messages
in the new LLM prompt.
''')

st.info("In the following example, we will use the ConversationChain, another LangChain built-in chain", icon="ℹ️")

openai_key = st.text_input("OpenAI Api Key")

prompt = st.chat_input("How can I help you today?")

if prompt:

    if "conversation" not in st.session_state:

        memory = ConversationBufferMemory()
        
        llm = ChatOpenAI(openai_api_key=openai_key, temperature=0.0)
        
        chain = ConversationChain(llm=llm, memory = memory)
        
        st.session_state.conversation = chain

    response = st.session_state.conversation.predict(input=prompt)

    st.write(response)






