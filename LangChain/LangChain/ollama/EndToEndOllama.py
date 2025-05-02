import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
LANGCHAIN_API_KEY=os.getenv('LANGCAHIN_API_KEY')
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_PROJECT=os.getenv('LANGCHAIN_PROJECT')

prompt=ChatPromptTemplate.from_messages(
  [
    ("system","You are a helpful assistant.Please respond to the question asked"),
    ("user","Question:{question}")
  ]
)

## Streamlit framework

st.title("Langchain Deamo with Llama Model")
input_text=st.text_input("What question you have in mind?")

print(input_text)
## Ollama Llama2 model
llm=Ollama(model="llama3")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser
if input_text:
  st.write(chain.invoke({"question":input_text}))

