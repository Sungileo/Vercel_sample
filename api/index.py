from fastapi import FastAPI, Form, Request, Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.exceptions import HTTPException
import os
import pymysql

app = FastAPI()

def get_db_connection():
    try:
        conn = pymysql.connect(
            host='runink.c3om8wy2ed7d.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='runink1011^^',
            database='playground',
            cursorclass=pymysql.cursors.DictCursor)
        return conn
    except pymysql.Error as e:
        print(f"데이터베이스 연결 오류: {e}")
        return None


# templates 디렉토리 경로를 절대 경로로 설정
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/login_action")
async def register_user(request: Request, username:str = Form(...), text:str = Form(...)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO new_table (username, text) VALUES (%s, %s)",(username, text))
    conn.commit()
    print("success!")
    conn.close()
    return RedirectResponse(url="/", status_code=303)
