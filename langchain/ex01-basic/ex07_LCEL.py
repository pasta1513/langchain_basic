from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ('system', '답변은 영어로 한다.'),
    ('human', '{question}')
])

chain = prompt | llm | StrOutputParser()
res = chain.invoke({'question':'오늘 날씨가 좋아.'})
print(res)
print('--'*60)

res = chain.invoke({'question':'파이썬 설명해줘.'})
print(res)