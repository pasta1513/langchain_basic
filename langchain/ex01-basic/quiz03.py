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

while True: 
    q = input('영어 단어 입력(종료: exit): ')

    if q.lower() == 'exit':
        break

    messages.append(HumanMessage(content=q))
    res = llm.invoke(messages)
    messages.append(res)
    print(res.content)