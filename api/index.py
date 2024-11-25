from fastapi import FastAPI

app = FastAPI(
    docs_url="/docs",  # 명시적으로 docs URL 설정
    redoc_url="/redoc",  # ReDoc URL도 설정
)

@app.get("/")
async def root():
    return {"message": "Hello World"}