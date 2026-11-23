from langchain_core.runnables import RunnablePassthrough, RunnableLambda

chain = RunnablePassthrough()

print(chain.invoke('안녕'))
print(chain.invoke({'aaa':111}))
print(chain.invoke([1,2,3,4,5]))

def clean(d):
    return {'text':d['text'].lower()}

print(clean({'text':'LangChain'}))

chain = RunnableLambda(clean)
print(chain.invoke({'text':'LangChain'}))

chain = RunnableLambda(clean) | RunnablePassthrough()
print(chain.invoke({'text':'LangChain'}))