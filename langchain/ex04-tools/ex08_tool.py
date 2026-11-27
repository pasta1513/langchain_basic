from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

from llm_config import get_llm
from tools import get_weather

llm_tools = get_llm().bind_tools([get_weather])
tools_dict = {'get_weather': get_weather}

messages = [
    SystemMessage(content='간략하게 한 줄로만 답변한다.'),
    HumanMessage(content='오늘 서울 날씨 알려줘.')
]

res = llm_tools.invoke(messages)
# print(type(res))
# print(res)
messages.append(res)

print(res.tool_calls)
if res.tool_calls:
    print('도구 호출')
    tool_info = res.tool_calls[0]
    tool = tools_dict[tool_info['name']]
    tool_res = tool.invoke(tool_info['args'])
    # print(tool_res, type(tool_res))
    messages.append(ToolMessage(content=tool_res, tool_call_id=tool_info['id']))
    result = llm_tools.invoke(messages)
    print(result.content)
else:
    print('호출 없음')