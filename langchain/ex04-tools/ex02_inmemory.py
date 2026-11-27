import time

from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache
from llm_config import get_llm

set_llm_cache(InMemoryCache())

llm = get_llm()

q = 'LCEL을 50자 이내의 한 문장으로 간결하게 설명해줘.'
print('--'*50)

for i in range(2):
    t = time.time()
    out = llm.invoke(q).content

    print(f'{i+1}회 {time.time() - t: .2f}s > {out}')