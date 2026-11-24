from langchain_core.runnables import RunnableParallel
from operator import itemgetter

from agents.review_agent import original_chain, sentiment_chain, summary_chain, keyword_chain

review_chain = RunnableParallel(
    original = itemgetter('text'),
    sentiment = sentiment_chain,
    summary = summary_chain,
    keyword = keyword_chain
)