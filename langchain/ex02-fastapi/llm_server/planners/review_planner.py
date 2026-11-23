from langchain_core.runnables import RunnableParallel

from agents.sentiment_agent import original_chain, sentiment_chain, summary_chain, keyword_chain


review_chain = RunnableParallel(
    original = original_chain,
    sentiment = sentiment_chain,
    summary = summary_chain,
    keyword = keyword_chain
)