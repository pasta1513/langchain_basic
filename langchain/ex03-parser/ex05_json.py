from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

from llm_config import get_llm

class Ingerdient(BaseModel):
    name: str = Field(description='재료명')
    amount: str = Field(description='분량')

class Recipe(BaseModel):
    dish: str = Field(description='요리명')
    ingerdient: list[Ingerdient] = Field(description='재료 목록')
    minutes: int = Field(description='소요 시간(분)')

llm = get_llm()
parser = JsonOutputParser(pydantic_object=Recipe)
prompt = ChatPromptTemplate.from_messages([
    ('system', '너는 레시피 도우미야. 반드시 아래 형식의 JSON으로만 답해.\n{test_format}'),
    ('human', '{food} 레시피 알려줘.')
]).partial(test_format=parser.get_format_instructions())

chain = prompt | llm | parser
result = chain.invoke({'food':'김치볶음밥'})

print(result)
print('--'*40)
print(f'요리: {result['dish']}')
print('재료:' , end='')
# for ing in result['ingerdient']:
#     print(f'{ing['name']} {ing['amount']}', end=', ')
ingredients = ', '.join(
    f'{ing["name"]} {ing["amount"]}'
    for ing in result['ingerdient']
)
print(ingredients)
print(f'시간: {result['minutes']}분')