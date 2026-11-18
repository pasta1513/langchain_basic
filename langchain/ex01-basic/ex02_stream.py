import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatBedrockConverse(
    model=os.getenv('BEDROCK_MODEL_ID'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

messages = [
    SystemMessage(content=
                  '너는 친절한 ai비서다.'
                  '모든 내용은 한 줄로 답변한다.'
                  ),
    HumanMessage(content='너는 어떤 모델이야?')
]

res = llm.stream(messages)

# print(next(res))
# print(next(res))
# print(next(res))
print('--'*30)

for chunk in res:
    print(chunk.text, end = '')