from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services import chatbot_service
from schemas.chatbot_schema import ChatReq, ChatRes

router_chatbot = APIRouter(tags=['chatbot'], prefix='/chatbot')

@router_chatbot.post('/stream', response_model=ChatRes)
async def chatbot(req: ChatReq):
    return StreamingResponse(
        chatbot_service.chatbot_stream(req.human_msg),
        media_type='text/plain; charset=utf-8'
    )