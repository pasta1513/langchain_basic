from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from llm_config import get_llm

class MailInfo(BaseModel):
    sender: str = Field(description='보낸 사람')
    request: str = Field(description='핵심 요청')
    due: str = Field(description='기한(없으면 미정)')

llm = get_llm()
prompt = ChatPromptTemplate.from_messages([
    ('system', '이메일에서 정보를 추출해라'),
    ('human', '{email}')
])
email = '김부장입니다. 다음주 월요일까지 3분기 보고서 초안을 보내주세요.'

chain = prompt | llm.with_structured_output(MailInfo)
info = chain.invoke({'email':email})
print(info)
print(info.model_dump())
print('--'*50)

data = info.model_dump()
data['name'] = "홍길동"
data['message'] = "기한내에 완료 가능하다. 답장 만들어줘"
reply_prompt = ChatPromptTemplate.from_messages([
    ('system', '답변 작성자 이름 {name}이고, 정중하게 작성한다.'),
    ('human', '''{sender}님의 요청.
                {request}, 기한 {due}에 대한 정중한 답장 초안을 만든다.
                {message}''')
])

reply_chain = reply_prompt | llm
print(reply_chain.invoke(data).content)