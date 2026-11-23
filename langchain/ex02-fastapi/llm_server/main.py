from fastapi import FastAPI

import uvicorn

from routes import review_route

app = FastAPI(title='Review Analysis API')
app.include_router(review_route.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)