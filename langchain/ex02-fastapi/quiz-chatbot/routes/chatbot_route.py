from fastapi import APIRouter

from services import chatbot_service
from schemas.chatbot_schema import ChatReq, ChatRes

router_chatbot = APIRouter(tags=['chatbot'], prefix='/chatbot')

@router_chatbot.post('', response_model=ChatRes)
async def chatbot(req: ChatReq):
    return await chatbot_service.chatbot(req.human_msg)