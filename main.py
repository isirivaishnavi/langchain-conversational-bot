from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv("conversational.env")

llm = ChatOpenAI(temperature=0)

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory
)

print("Chatbot ready! Type 'exit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = conversation.run(user_input)
    print("Bot:", response)
