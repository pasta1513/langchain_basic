import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

prompt = [
    '새로 여는 동네 카페 이름을 하나만 추천해줘. 이름만 답변해.',
    '가을을 한 문장으로 표현해줘.',
    "'고양이'로 시작하는 짧은 이야기 첫 문장을 써줘."
]
messages = [
    SystemMessage(content='답변은 한 문장으로 요약한다.'),
    HumanMessage(content=prompt)
]

for t in [0.0, 1.0]:
    llm = ChatBedrockConverse(
        model=os.getenv('BEDROCK_MODEL_ID'),
        region_name=os.getenv('AWS_DEFAULT_REGION'),
        temperature=t
    )

    for i in range(3):
        res = llm.invoke(messages)
        print(f'temp: {t} => {res.content}')

    print('--'*30)