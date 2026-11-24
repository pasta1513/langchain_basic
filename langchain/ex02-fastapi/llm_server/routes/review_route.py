from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from core.llm import get_llm
from services import review_service
from schemas.review_schema import ReviewReq, ReviewRes

router = APIRouter(prefix='/review', tags=['review'])

@router.post('', response_model=ReviewRes)
async def review(req: ReviewReq):
    'planner 전체를 한 번에 실행하여 완성된 결과를 반환'
    # return get_llm().invoke(req)
    return await review_service.review(req.text)

@router.post('/summary-stream')
async def summary_stream(req: ReviewReq):
    return StreamingResponse(
        review_service.summary_stream(req.text),
        media_type='text/plain; charset=utf-8'
    )