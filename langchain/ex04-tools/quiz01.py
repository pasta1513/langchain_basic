from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

from llm_config import get_llm
from tools import multify, now

llm = get_llm()
llm_tools = get_llm().bind_tools([multify, now])
tools_dict = {'multify': multify, 'now': now}

robust = llm_tools.with_fallbacks([llm])

qs = [
    '3 곱하기 9는?',
    '지금 몇 시야?',
    '잘 지내?'
]

messages = [
    SystemMessage(content='간결하게 100자 이내의 한 문장으로 답변한다.')
]

for q in qs:
    messages.append(HumanMessage(content=q))
    res = robust.invoke(messages)   # 해당하는 도구가 있으면 AIMessage에 호출할 도구 정보(tool_calls)가 함께 넘어온다
    messages.append(res)

    if res.tool_calls:
        tool_info = res.tool_calls[0]
        tool_name = tool_info['name']
        print(f'도구 호출: {tool_name}')
        tool = tools_dict[tool_name]
        tool_res = tool.invoke(tool_info['args'])
        messages.append(ToolMessage(content=tool_res, tool_call_id=tool_info['id']))
        res = robust.invoke(messages)
        messages.append(res)
    else:
        print(f'자동 답변: {robust.invoke(messages).response_metadata['model_name']}')

    print(res.content)
    print('--'*50)