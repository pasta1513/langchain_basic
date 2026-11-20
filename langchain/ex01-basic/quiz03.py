import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatBedrockConverse(
    model=os.getenv('BEDROCK_MODEL_ID'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)
messages = [
    SystemMessage(content='물어보는 것에만 단답으로 대답한다. 영단어를 물어보면 한국어로 번역한다.')
]

question = input('영어 단어 입력(종료: exit): ')
messages.append(HumanMessage(content=question))
res = llm.invoke(messages)
print(res.content)

question2 = input('영어 단어 입력(종료: exit): ')
messages.append(HumanMessage(content=question2))
res = llm.invoke(messages)
print(res.content)