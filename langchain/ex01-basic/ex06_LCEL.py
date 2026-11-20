from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content='답변은 한 문장으로 작성한다.'),
    HumanMessage(content='llm이 뭐야?')
])
chain = prompt | llm | StrOutputParser()
res = chain.invoke({})
print(res)
print(type(res))