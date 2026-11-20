import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatBedrockConverse(
    model=os.getenv('BEDROCK_MODEL_ID'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

EXAMPLES = [
    ("결제가 계속 실패해요, 카드 문제인가요?", "PAY-P1"),
    ("택배가 일주일째 안 와요", "SHP-P2"),
    ("비밀번호 변경은 어디서 하나요?", "ACC-P3"),
    ("주문한 거 환불해주세요", "PAY-P2"),
    ("다른 사람이 제 계정에 로그인한 것 같아요", "ACC-P1"),
    ("배송 조회는 어디서 해요?", "SHP-P3"),
]
messages = [
    SystemMessage(content='''
                  고객 문의를 '팀코드-우선순위' 형식으로만 답한다.
                  우선 순위
                  - 돈이 빠졌거나 보안 문제 = P1
                  - 처리 지연, 요청 = P2
                  - 가능 여부, 방법 문의 = P3
                  '''),
    # HumanMessage(content=EXAMPLES[0][0]),
    # AIMessage(content=EXAMPLES[0][1])
]

for q, a in EXAMPLES:
    messages.append(HumanMessage(content=q))
    messages.append(AIMessage(content=a))

TESTS = [("배송지 변경 가능한가요?", "SHP-P3"),]
messages.append(
    HumanMessage(content=TESTS[0][0])
)
res = llm.invoke(messages)
print(res.content)