from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

from llm_config import get_llm

llm = get_llm()
parser = CommaSeparatedListOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ('system', '''부연 설명은 일체 하지 않는다.
                한국어만 사용하고, 입력에 해당하는 내용만을 콤마를 이용해 목록으로 출력한다.'''),
    ('human', '{q}')
])
chain = prompt | llm | parser

result = chain.invoke({'q':input('입력: ')})
print('--'*50)
print(result)
print('--'*50)
for i, item in enumerate(result):
    print(f'{i+1}. {item}')