import base64

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path

from llm_config import get_llm

llm = get_llm()
img_file = Path(__file__).parent / 'card' / '강아지.jpg'
img_b64 = base64.b64encode(img_file.read_bytes()).decode('utf-8')

# print(len(img_file.read_bytes()))
# print(img_file.read_bytes()[:10])
# print(len(img_b64))
# print(img_b64[:10])

# message = HumanMessage(content=[
#     {'type':'text', 'text':'이 사진을 설명해줘'},
#     {'type':'image', 'base64':img_b64, 'mime_type':'image/jpeg'}
# ])
# result = llm.invoke([message])
# print(result.content)

prompt = ChatPromptTemplate.from_messages([
    ('system', '이미지에 대한 설명을 한다. 희망을 전달하는 방식으로 설명한다.'),
    ('human', [
        {'type':'text', 'text':'{msg}'},
        # {'type':'image', 'base64':'{b64}', 'mime_type':'image/jpeg'},
        {'type':'image_url', 'image_url':{'url':'data:image/jpeg;base64, {b64}'}}
    ])
])
chain = prompt | llm | StrOutputParser()
print(chain.invoke({'msg':'사진 설명해줘', 'b64':img_b64}))