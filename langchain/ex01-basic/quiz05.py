from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from llm_config import get_llm

def preprocess(d):
    q = d['question'].strip().lower()
    return {'question': q}

def postprocess(text):
    return f'[답변] {text.strip().upper()}'

print('--- 전처리 확인 ---')
chain = RunnableLambda(preprocess)
print(chain.invoke({'question':'        LLM이 모야?   '}))

print('--- 후처리 확인 ---')
chain = RunnableLambda(postprocess)
print(postprocess('        llm이 모야?   '))

llm = get_llm()
prompt = ChatPromptTemplate([
    ('system', '답변은 한 문장으로 작성한다.'),
    ('human', '{question}')
])

print('--- 전처리, prompt, llm, str, 후처리 ---')
chain = RunnableLambda(preprocess) | prompt | llm | StrOutputParser() | RunnableLambda(postprocess)
print(chain.invoke({'question':'        LLM이 모야?   '}))