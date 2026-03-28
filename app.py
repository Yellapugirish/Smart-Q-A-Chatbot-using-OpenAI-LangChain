import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import openai

##langSmith Tracing
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true" 
os.environ['LANGCHAIN_PROJECT']="Q&A Chatbot with OpenAI"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an helpful assistant. Please respond to user request with an live example"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    model = ChatOpenAI(
        model=llm,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
    output_parser = StrOutputParser()
    chain = prompt | model | output_parser
    answer = chain.invoke({"question": question})
    return answer

##Streamlit app
st.title("Q&A Chatbot with OpenAI")

## Sidebar
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your OpenAI API:",type="password")

## Dropdwon to select models
llm=st.sidebar.selectbox("select an OpenAI model",["gpt-4o","gpt-4-turbo","gpt-4"])

##Adjust Parameters
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.4)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=400,value=150)

## Main Interface
st.write("Ask any Question?")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the Query")

