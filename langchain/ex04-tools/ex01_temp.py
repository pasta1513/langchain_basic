from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage

from llm_config import get_llm

fact_llm = get_llm(temperature=0.0)
idea_llm = get_llm(temperature=1.0)

sysMsg = SystemMessage(content='답변은 간략하게 한 줄로 요약한다.')
prompt = ChatPromptTemplate([
    sysMsg, HumanMessage(content='카페 이름 3개만 추천해줘.')
])
parser = StrOutputParser()

fact_chain = prompt | fact_llm | parser
print(f'[사실] {fact_chain.invoke({})}')

idea_chain = prompt | idea_llm | parser
print(f'[창의적] {fact_chain.invoke({})}')