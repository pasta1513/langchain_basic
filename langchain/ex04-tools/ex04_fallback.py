from langchain_core.messages import SystemMessage, HumanMessage

from llm_config import get_llm

primary = get_llm(model='BEDROCK_MODEL_FAIL')
backup = get_llm(model='BEDROCK_MODEL_ID2')

robust = primary.with_fallbacks([backup])
res = robust.invoke([HumanMessage(content='안녕')])
print('모델 확인: ', res.response_metadata['model_name'])
print(res.content)