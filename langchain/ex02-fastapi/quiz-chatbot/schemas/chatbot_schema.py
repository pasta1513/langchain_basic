from pydantic import BaseModel

class ChatReq(BaseModel):
    userid: str
    human_msg: str

class ChatRes(BaseModel):
    ai_msg: str
    history_len: int