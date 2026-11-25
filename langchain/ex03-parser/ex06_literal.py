from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
from pydantic import BaseModel, Field

from llm_config import get_llm

class Satiscation(BaseModel):
    level: Literal['매우 만족', '만족', '보통', '불만족', '매우 불만족']

parser = PydanticOutputParser(pydantic_object=Satiscation)
llm = get_llm()
prompt = ChatPromptTemplate.from_messages([
    ('system', '''너는 고객 리뷰의 만족도를 분류하는 분류가다.
                반대의 아래 형식의 JSON으로만 대답한다.
                {format}'''),
    ('human', '{review}')
]).partial(format=parser.get_format_instructions())

chain = prompt | llm | parser
reviews = [
    '기대 이상이에요! 정말 최고의 제품입니다.',
    '괜찮게 잘 쓰고 있어요.',
    '그냥 그래요. 가격 값은 합니다.',
    '배송이 너무 느렸고 품질도 그냥 그래요.',
    '최악입니다. 환불 받고 싶어요.'
]
result = chain.invoke({'review':reviews[0]})
print(result)
print('--'*50)
for review in reviews:
    result = chain.invoke({'review':review})
    print(f'[{result.level}]: {review}')