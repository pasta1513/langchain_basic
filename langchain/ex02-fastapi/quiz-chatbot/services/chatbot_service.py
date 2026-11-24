from langchain_core.messages import HumanMessage, AIMessage

from planners.chatbot_planner import chatbot_chain

h=[]

async def chatbot(human_msg: str):
    # return await chatbot_chain.invoke({'human_msg'})

    res = await chatbot_chain.ainvoke({'human_msg': human_msg, 'history': h})
    ai_msg = res['counselor']

    h.append(HumanMessage(content=human_msg))
    h.append(AIMessage(content=ai_msg))

    return {'ai_msg': ai_msg, 'history_len': len(h)}