import uvicorn
from fastapi import FastAPI
from app.api.v1 import group
app = FastAPI(
    docs_url="/api/docs"
)

app.include_router(group.router, prefix="/api/v1/group")

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8005
    )
