from langchain_core.runnables import RunnableParallel

from agents.chatbot_agent import counselor_chain

chatbot_chain = RunnableParallel(
    counselor = counselor_chain
)

