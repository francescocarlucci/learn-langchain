import openai
import streamlit as st

def get_completion(prompt, openai_api_key, model="gpt-3.5-turbo"):
    openai.api_key = openai_api_key
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]