from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

llm = get_llm(temperature=0.5)

prompt = ChatPromptTemplate.from_messages([
    ('system', '답변은 짧고 간결하게. 물어본 것에 대해서만 한 문장 내에 대답한다.'),
    MessagesPlaceholder('history'),
    ('human', '{question}')
])
h = []
chain = prompt | llm | StrOutputParser()

while True:
    q = input('나(종료: exit): ').strip()

    if q.lower() == 'exit':
        print('종료합니다.')
        break

    res = chain.invoke({'question': q, 'history': h})
    h.append(HumanMessage(content=q))
    h.append(AIMessage(content=res))

    print('AI 답변 :', res)
    print('대화 기록: ', len(h))
    print('--'*60)