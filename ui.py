import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import ChatOpenAI

load_dotenv()

db = SQLDatabase.from_uri("sqlite:///data.db")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

st.title("🤖 AI SQL Assistant")

question = st.text_input("Ask your question")

if st.button("Run Query"):
    if question:
        result = db_chain.run(question)
        st.success("Result")
        st.write(result)
    else:
        st.warning("Enter a question")