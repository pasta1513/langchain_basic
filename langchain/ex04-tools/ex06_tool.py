from langchain_core.tools import tool

@tool   # 일반적인 함수가 아닌, llm에서 사용하기 위한 tool
def add(a: int, b: int) -> int:
    '''두 정수 a와 b를 더한 값을 반환한다.'''
    return a+b

@tool
def get_length(text: str) -> int:
    '''주어진 문자열의 글자 수를 반환한다.'''
    return len(text)

print('이름:', add.name)
print('설명:', add.description)
print('인자:', add.args)

print(add(10, 20))      # error
print(add.invoke({10, 20}))     # error
print('직접 호출:', add.invoke({'a':10, 'b':20}))

print('직접 호출:', get_length.invoke({'test1234'}))
print('직접 호출:', get_length.invoke({'text':'test1234'}))