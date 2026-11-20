from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

llm = get_llm()

prompt = ChatPromptTemplate.from_messages([
    ('system', '답변은 한 줄로 요약한다.'),
    MessagesPlaceholder('history'),
    ('human', '{q}')
])
# input = "내 이름은 '이현'이야!"
# chain = prompt | llm | StrOutputParser()
# res = chain.invoke({'q': input})
h = [
    HumanMessage(content="내 이름은 '이현'이야."),
    AIMessage(content='반가워요, 이현 씨!')
]
input = '내 이름 기억하니?'
chain = prompt | llm | StrOutputParser()
res = chain.invoke({'q': input, 'history': h})
print(res)

h.append(HumanMessage(content=input))
h.append(AIMessage(content=res))
