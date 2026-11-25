from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

from llm_config import get_llm

class Inquiry(BaseModel):
    summary: str = Field(description='문의 요약')
    categery: Literal['결제', '배송', '환불', '기타']
    priority: Literal['높음', '보통', '낮음']
    keywords: list[str]

parser = PydanticOutputParser(pydantic_object=Inquiry)
llm = get_llm()
prompt = ChatPromptTemplate.from_messages([
    ('system', '''당신은 문의 분류가다.
                고객의 문의에 대해 반드시 형식의 JSON 형태로 답한다.
                {format}'''),
    ('human', '{mail}')
]).partial(format=parser.get_format_instructions())

chain = prompt | llm | parser
mails = [
    '결제는 정상적으로 했는데 상품이 아직도 안 왔어요. 환불해주세요.',
    '어제 주문한 상품 언제쯤 도착하나요? 빨리 받고 싶어요.',
    '카드 결제가 두 번 됐어요! 당장 처리해주세요.',
    '단순 변심으로 반품하고 환불받고 싶습니다.',
    '회원 등급은 어떻게 올리나요? 궁금해서 문의 드려요.'
]

# result = chain.invoke({'mail':mails[0]})
# print(result)
# print(result.model_dump())

key_mapping = {
    'summary': '문의 요약',
    'categery': '문의 유형',
    'priority': '우선순위',
    'keywords': '핵심 키워드'
}

tasks = ('\n' + '--'*50 + '\n').join(
    f'[{i+1}] {mail}\n' +
    '\n'.join(f'- {key_mapping[key]}: {value}'
              for key, value in chain.invoke({'mail':mail}).model_dump().items())
    for i, mail in enumerate(mails)
)
print(tasks)