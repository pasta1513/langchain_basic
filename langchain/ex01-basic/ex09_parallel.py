import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()
from llm_config import get_llm

llm_01 = get_llm(temperature=0.0)
prompt_01 = ChatPromptTemplate([
    ('system', '반말로 답한다.'),
    ('human', '{text01}')
])
chain_01 = prompt_01 | llm_01 | StrOutputParser()
start = time.time()

print(chain_01.invoke({'text01':'안녕'}))
print('--'*50)

llm_02 = get_llm(temperature=0.9)
prompt_02 = ChatPromptTemplate([
    ('system', '반말로 답한다.'),
    ('human', '{text02}')
])
chain_02 = prompt_02 | llm_02 | StrOutputParser()

print(chain_02.invoke({'text02':'안녕'}))
end = time.time() - start
print(f'실행 시간: {end:.3f} 초')

chain = RunnableParallel(
    user_key01 = chain_01,
    user_key02 = chain_02
)

start = time.time()
answer = chain.invoke({'text01':'안녕', 'text02':'안녕'})
end = time.time() - start

print(answer)
print(f'걸린 시간: {end:.3f} 초')
print(answer['user_key01'])