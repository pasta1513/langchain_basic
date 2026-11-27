from langchain_core.prompts import ChatPromptTemplate

from llm_config import get_llm

primary = get_llm(model='BEDROCK_MODEL_FAIL')
backup = get_llm(model='BEDROCK_MODEL_ID2')

prompt = ChatPromptTemplate([
    ('system', '답변은 간략하게 한 줄로 한다.'),
    ('human', '{q}')
])

primary_chain = prompt | primary
backup_chain = prompt | backup

robust_chain = primary_chain.with_fallbacks([backup_chain])
res = robust_chain.invoke({'q':'안녕'})

print(f'모델명: {res.response_metadata['model_name']}')
print(res.content)