from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

from llm_config import get_llm

llm = get_llm()

class BusinessCard(BaseModel):
    name: str
    company: str
    phone: str
    email: str

parser = PydanticOutputParser(pydantic_object=BusinessCard)
prompt = ChatPromptTemplate.from_messages([
    ('system', '너는 명함 출력기야. 반드시 아래 형식의 JSON으로만 대답해. 회사명에 부서명은 필요 없어.\n{test_format}'),
    ('human', '{business_card}')
]).partial(test_format=parser.get_format_instructions())
chain = prompt | llm | parser
card = chain.invoke({'business_card':'홍길동 남성 ABC컴퍼니 마케팅팀 010-1234-5678 kim@abc.com'})

print('이름:', card.name)
print('회사:', card.company)
print('전화번호:', card.phone)
print('이메일:', card.email)