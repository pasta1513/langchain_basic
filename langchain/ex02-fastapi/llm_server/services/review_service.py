from planners.review_planner import review_chain

async def review(req: str):
    return await review_chain.ainvoke({'text': req})