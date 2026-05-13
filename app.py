import os
from dotenv import load_dotenv

from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_openai import ChatOpenAI

load_dotenv()

# DB connect
db = SQLDatabase.from_uri("sqlite:///data.db")

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

# SQL chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

print("🔥 AI SQL Assistant Started")

while True:
    question = input("\nAsk question: ")

    if question.lower() == "exit":
        break

    result = db_chain.run(question)
    print("\nResult:\n", result)