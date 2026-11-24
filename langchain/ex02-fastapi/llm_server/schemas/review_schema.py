from pydantic import BaseModel

class ReviewReq(BaseModel):
    text: str

class ReviewRes(BaseModel):
    original: str
    sentiment: str
    summary: str
    keyword: str