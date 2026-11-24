from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

import uvicorn

from routes import review_route

app = FastAPI(title='Review Analysis API')
app.include_router(review_route.router)
_INDEX_ = Path(__file__).parent / 'static' / 'index.html'

@app.get('/')
async def index():
    return FileResponse(_INDEX_)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)