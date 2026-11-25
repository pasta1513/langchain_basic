import base64

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path
from pydantic import BaseModel, Field

from llm_config import get_llm

class BusinessCard(BaseModel):
    company: str = Field(description='회사명')
    name: str = Field(description='이름')
    phone: str = Field(description='전화번호')
    email: str = Field(description='이메일')
    address: str = Field(description='주소')

img_file = Path(__file__).parent / 'card' / '고길동.png'
img_b64 = base64.b64encode(img_file.read_bytes()).decode('utf-8')

llm = get_llm()
prompt = ChatPromptTemplate.from_messages([
    ('system', "이미지에서 정보를 추출한다. 확실하지 않은 정보는 꾸며내지 않고 '확인 불가'로 표시한다."),
    ('human', [
        {'type':'text', 'text':'{msg}'},
        {'type':'image', 'base64':'{b64}', 'mime_type':'image/png'}
    ])
])

chain = prompt | llm.with_structured_output(BusinessCard)
info = chain.invoke({'msg':'이 사진에서 정보를 추출해.', 'b64':img_b64})
# print(info.model_dump())

key_mapping = {
    'company': '상호',
    'name': '이름',
    'phone': '전화',
    'email': '이메일',
    'address': '주소'
}

card_read = '\n'.join(f'{key_mapping[key]}: {value}'
                      for key, value in info.model_dump().items())
print(card_read)