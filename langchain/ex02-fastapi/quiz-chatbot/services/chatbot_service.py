from langchain_core.messages import HumanMessage, AIMessage

from planners.chatbot_planner import chatbot_chain
from agents.chatbot_agent import counselor_chain

h=[]

async def chatbot_stream(human_msg: str):
    # res = await chatbot_chain.ainvoke({'human_msg': human_msg, 'history': h})
    # ai_msg = res['counselor']

    full = ''
    async for chunk in counselor_chain.astream({'human_msg': human_msg, 'history': h}):
        full += chunk
        yield chunk

    h.append(HumanMessage(content=human_msg))
    h.append(AIMessage(content=full))