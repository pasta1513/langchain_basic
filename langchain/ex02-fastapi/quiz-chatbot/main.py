import uvicorn

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

from routes.chatbot_route import router_chatbot

app = FastAPI(title='ChatBot')
app.include_router(router_chatbot)
_INDEX_ = Path(__file__).parent / 'static' / 'index.html'

@app.get('/')
async def index():
    return FileResponse(_INDEX_)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8001, reload=True)