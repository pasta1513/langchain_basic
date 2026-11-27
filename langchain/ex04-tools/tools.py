from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    '''입력된 도시의 현재 날씨를 반환한다.'''
    print('---=== get_weather 호출 ===---')
    return {'서울':'맑음 12도', '부산':'흐림 5도'}.get(city, '정보 없음')