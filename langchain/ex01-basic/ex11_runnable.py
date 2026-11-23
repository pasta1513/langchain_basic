from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

def preprocess(d):
    q = d['question'].strip().lower()
    return {'question': q}

def postprocess(text):
    text['result'] = f'[답변] {text['result'].strip().upper()}'
    return text

llm = get_llm()
prompt = ChatPromptTemplate([
    ('system', '답변은 한 문장으로 최대한 짧고 간결하게 한다.'),
    ('human', '{question}')
])

chain = preprocess | RunnableParallel(
    result = prompt | llm | StrOutputParser(),
    original = RunnablePassthrough()
) | postprocess
print(chain.invoke({'question':"       LLM이 뭐야?   "}))