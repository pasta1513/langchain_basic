from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from core.llm import get_llm

prompt = ChatPromptTemplate([
    ('system', '''당신은 따뜻한 마음을 가진 상담사입니다.
                모든 답변은 반드시 한글로 하며, 항상 3 문장을 넘기지 않습니다.
                공감과 이해를 먼저 표현하고, 절대 함부로 판단하거나 평가하지 않습니다.
                부드럽고 안정적인 말투를 사용합니다.'''),
    MessagesPlaceholder('history'),
    ('human', '{human_msg}')
])

counselor_chain = prompt | get_llm() | StrOutputParser()