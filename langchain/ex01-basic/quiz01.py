import os
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatBedrockConverse(
    model=os.getenv('BEDROCK_MODEL_ID'),
    region_name=os.getenv('AWS_DEFAULT_REGION')
)

while True:
    print('말투를 선택하세요.(1(강아지 말투), 2(고양이 말투), 3(정중한 말투)): ', end='')

    choice = input()

    if choice == '1':
        mode = '강아지 말투'
    elif choice == '2':
        mode = '고양이 말투'
    elif choice == '3':
        mode = '정중한 말투'
    else:
        print('잘못된 선택입니다. 종료합니다.')
        break
    
    user_input = input('나(종료: exit): ')

    if user_input == 'exit':
        print('종료합니다.')
        break

    messages = [
        SystemMessage(content=f'선택한 상황에 맞는 말투로, 짧고 간결하게 질문에만 대답해: {mode}'),
        HumanMessage(content=user_input)
    ]
    res = llm.stream(messages)

    print('AI: ', end='')

    for chunk in res:
        print(chunk.text, end='')
    print('\n')