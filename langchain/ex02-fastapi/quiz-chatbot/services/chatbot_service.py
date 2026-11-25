from agents.chatbot_agent import counselor_chain

from services.history import get_history, add_turn

async def chatbot_stream(userid: str, human_msg: str):
    # res = await chatbot_chain.ainvoke({'human_msg': human_msg, 'history': h})
    # ai_msg = res['counselor']

    ai_msg = ''
    async for chunk in counselor_chain.astream({'human_msg': human_msg, 'history': get_history(userid)}):
        ai_msg += chunk
        yield chunk

    add_turn(userid, human_msg, ai_msg)