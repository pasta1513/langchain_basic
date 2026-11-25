from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from llm_config import get_llm

class Task(BaseModel):
    title: str = Field(description='분야')
    owner: str = Field(description='담당자')
    due: str = Field(description='기한')

class Plan(BaseModel):
    project: str = Field(description='프로젝트명')
    task: list[Task] = Field(description='할 일')

llm = get_llm()
parser = PydanticOutputParser(pydantic_object=Plan)
prompt = ChatPromptTemplate.from_messages([
    ('system', '너는 프로젝트 일정 출력기야. 반드시 아래 형식의 JSON으로만 답해. \n{test_format}'),
    ('human', '{memo}')
]).partial(test_format=parser.get_format_instructions())

chain = prompt | llm | parser
result = chain.invoke({'memo':'신체품 출시 프로젝. 디자인은 길동이가 수요일까지, 개발은 지은이가 금요일까지.'})
print(result)
print('--'*50)
print('프로젝트:', result.project)
print('=='*50)
tasks = ('\n' + '--'*50 + '\n').join(
    '\n'.join(f'{key}: {value}' for key, value in t.model_dump().items())
    for t in result.task
)
print(tasks)