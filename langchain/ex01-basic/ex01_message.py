from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage
import os

client = ChatBedrockConverse(
    model=os.getenv('BEDROCK_MODEL_ID'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)
# user = input('추론 값 입력: ')
result = client.invoke([
    SystemMessage(content='반말로만 해'),
    HumanMessage(content='너는 어떤 모델이야?')
])

print('---=== result ===---')
print(type(result))
print(result.content)