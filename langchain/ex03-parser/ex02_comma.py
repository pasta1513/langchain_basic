from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

from llm_config import get_llm

llm = get_llm()
parser = CommaSeparatedListOutputParser()
prompt = ChatPromptTemplate.from_template('{x}를 콤마로 구분해 나열해줘.')

chain = prompt | llm | parser
result = chain.invoke({'x':'파이썬의 자료형에 대해 설명해줘.'})

print(type(result))
print(result)
print(result[0])