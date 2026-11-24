from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from core.llm import get_llm

prompt1 = ChatPromptTemplate([
    ('system', '리뷰의 감정을 긍정/부정/중립 중 하나로만 표현한다. 단어 이외의 첨언은 하지 않는다.'),
    ('human', '배송은 이틀 만에 왔고 품질도 기대 이상이라 재구매할 생각이에요.'),
    ('ai', '긍정'),
    ('human', '{text}')
])
prompt2 = ChatPromptTemplate([
    ('system', '한 문장으로 최대한 짧고 간결하게 요약한다.'),
    ('human', '배송은 이틀 만에 왔고 품질도 기대 이상이라 재구매할 생각이에요.'),
    ('ai', '빠른 배송과 기대 이상의 품질로 재구매 의사가 있다.'),
    ('human', '{text}')
])
prompt3 = ChatPromptTemplate([
    ('system', '핵심 키워드 3개만 쉼표로 구분하여 나열한다. 키워드 이외의 첨언은 하지 않는다.'),
    ('human', '배송은 이틀 만에 왔고 품질도 기대 이상이라 재구매할 생각이에요.'),
    ('ai', '배송, 품질, 재구매'),
    ('human', '{text}')
])

original_chain = RunnablePassthrough()
sentiment_chain = prompt1 | get_llm() | StrOutputParser()
summary_chain = prompt2 | get_llm() | StrOutputParser()
keyword_chain = prompt3 | get_llm() | StrOutputParser()