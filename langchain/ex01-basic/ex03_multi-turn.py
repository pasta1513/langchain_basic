import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatBedrockConverse(
    model=os.getenv('BEDROCK_MODEL_ID'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)
messages = [
    SystemMessage(content='답변은 한 줄로 간략하게 작성한다.'),
    HumanMessage(content="내 이름은 '이현'이야.")
]
res = llm.invoke(messages)

print(res.content)
print('--'*30)

llm = ChatBedrockConverse(
    model=os.getenv('BEDROCK_MODEL_ID'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)
messages = [
    SystemMessage(content='답변은 한 줄로 간략하게 작성한다.'),
    HumanMessage(content="내 이름은 '이현'이야."),
    res, # AIMessage(content=res.content)
    HumanMessage(content="내 이름을 기억해?")
]
res = llm.invoke(messages)

print(res.content)
print('--'*30)
print(type(res))
print(res)