from langchain_core.prompts import ChatPromptTemplate

from llm_config import get_llm

llm = get_llm()
chain = ChatPromptTemplate.from_template(
    '{x}를 한 문장으로 설명해.'
) | llm

result = chain.invoke({'x':'api가 뭐야?'})

print('type: ', type(result))
print('--'*30)

print('result: ', result)
print('--'*30)

print('content: ', result.content)
print('--'*30)