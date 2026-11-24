import os
from langchain_aws import ChatBedrockConverse

def get_llm(max_token: int=512, temperature: float=0.3):
    return ChatBedrockConverse(
        model=os.getenv('BEDROCK_MODEL_ID', 'global.amazon.nova-2-lite-v1:0'),
        region_name=os.getenv('AWS_DEFAULT_REGION', 'ap-northeast-2'),
        max_tokens=max_token,
        temperature=temperature
    )