from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

from llm_config import get_llm

llm = get_llm()

class Review(BaseModel):
    sentiment: str
    score: int
    keywords: list[str]
    content: str

parser = PydanticOutputParser(pydantic_object=Review)
print(parser.get_format_instructions())

prompt = ChatPromptTemplate.from_messages([
    ('system', '너는 리뷰 분석가야. 반드시 아래 형식의 JSON으로만 대답해.\n{test_format}'),
    ('human', '{review}')
]).partial(test_format=parser.get_format_instructions())

chain = prompt | llm | parser
r = chain.invoke({'review':'배송은 빨랐지만 포장이 부실해 모서리가 찌그러졌어요. 성능은 만족해요.'})

print(type(r))
print(r)
print('--'*30)
print('감정: ', r.sentiment)
print('점수: ', r.score)
print('키워드: ', r.keywords)
print('내용: ', r.content)