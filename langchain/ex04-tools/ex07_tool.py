from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool

from llm_config import get_llm

@tool
def get_weather(city: str) -> str:
    '''입력된 도시의 현재 날씨를 반환한다.'''
    print('---=== get_weather 호출 ===---')
    return {'서울':'맑음 12도', '부산':'흐림 5도'}.get(city, '정보 없음')

llm = get_llm()
llm_tools = llm.bind_tools([get_weather])

qs = ['오늘 서울 날씨 알려줘.', '김치찌개 만드는 방법 알려줘.']

message = [
    SystemMessage(content='친절하게 답변해.'),
    HumanMessage(content=qs[0])
]
res = llm_tools.invoke(message)

# print(res)
print('--'*50)

tools = {'get_weather': get_weather}
msg = []

for q in qs:
    print('사용자 질문:', q)
    # res: AIMessage, q: HumanMessage
    res = llm_tools.invoke(q)

    if res.tool_calls:
        msg.append(HumanMessage(content=q))
        msg.append(res)

        tool_call = res.tool_calls[0]
        # print(tool_call)
        # print(tools.get(tool_call['name']))
        tool = tools.get(tool_call['name'])
        tool_res = tool.invoke(tool_call['args'])
        # print(tool_res)
        
        msg.append(ToolMessage(content=tool_res, tool_call_id=tool_call['id']))
        print(llm_tools.invoke(msg).content)
    else:
        print('직접 답변(tool 없음)')
        # print(res.content)
        # print('아이디어 답변')
        # idea_llm = get_llm(temperature=1.0)
        # print(idea_llm.invoke(q).content)
    print('--'*50)