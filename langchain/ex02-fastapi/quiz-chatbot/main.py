import uvicorn

from fastapi import FastAPI

from routes.chatbot_route import router_chatbot

app = FastAPI(title='ChatBot')
app.include_router(router_chatbot)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8001, reload=True)