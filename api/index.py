from fastapi import FastAPI, Form, Request, Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.exceptions import HTTPException



app = FastAPI(
    docs_url="/docs",  # 명시적으로 docs URL 설정
    redoc_url="/redoc",  # ReDoc URL도 설정
)

# app.mount("/data", StaticFiles(directory="data"), name="data")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})