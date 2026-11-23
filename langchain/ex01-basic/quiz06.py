from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

llm = get_llm()
prompt1 = ChatPromptTemplate([
    ('system', '리뷰의 감정을 긍정/부정/중립 중 하나로만 표현한다. 단어 이외의 첨언은 하지 않는다.'),
    ('human', '{text}')
])
prompt2 = ChatPromptTemplate([
    ('system', '한 문장으로 최대한 짧고 간결하게 요약한다.'),
    ('human', '{text}')
])
prompt3 = ChatPromptTemplate([
    ('system', '핵심 키워드 3개만 쉼표로 구분하여 나열한다. 키워드 이외의 첨언은 하지 않는다.'),
    ('human', '{text}')
])

def format_output(x):
    return (
        f"원문 => {x['original']['text']}\n"
        f"감정 => {x['emotion']}\n"
        f"요약 => {x['review']}\n"
        f"키워드 => {x['keyword']}"
    )

chain = RunnableParallel(
    original = RunnablePassthrough(),
    emotion = prompt1 | llm | StrOutputParser(),
    review = prompt2 | llm | StrOutputParser(),
    keyword = prompt3 | llm | StrOutputParser()
)| format_output

print(chain.invoke({'text':'배송은 빨랐지만 포장이 부실했어요.'}))