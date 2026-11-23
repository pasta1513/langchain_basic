from fastapi import APIRouter

from core.llm import get_llm
from services import review_service

router = APIRouter(prefix='/review', tags=['review'])

@router.post('')
async def review(req: str):
    'planner 전체를 한 번에 실행하여 완성된 결과를 반환'
    # return get_llm().invoke(req)
    return await review_service.review(req)