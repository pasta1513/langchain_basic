import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage

TONS = {
    "1":"너는 노련한 요리사다. 쉬운 레시피를 친근하게 제안한다",
    "2":"너는 동기부여 운동 코치다. 따뜻하지만 단호하게 행동을 제안한다",
}

llm = ChatBedrockConverse(
    model=os.getenv("BEDROCK_MODEL_ID"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)
llm_nova = ChatBedrockConverse(
    model=os.getenv("BEDROCK_MODEL_ID2"),
    region_name=os.getenv("AWS_DEFAULT_REGION"),
)

print("=== exit 종료 ===")

while True:
    print() #단순 엔터 적용
    tone = TONS.get(input("말투 선택(1.요리사, 2.운동): "))
    q = input("나 입력(종료: exit): ")

    if q.lower() == "exit":
        print("종료")
        break

    messages = [
        SystemMessage(content=f"""
            너는 친절한 AI 비서다
            {tone}
            반드시 tone에 작성된 내용으로 답변한다
        """),
        HumanMessage(content=q)
    ]

    print('---=== nova 2 ===---')
    result = llm.stream(messages)
    for chunk in result:
        print(chunk.text , end="")

    print('\n---=== nova 1 ===---')
    result = llm_nova.invoke(messages)
    print(result.content)