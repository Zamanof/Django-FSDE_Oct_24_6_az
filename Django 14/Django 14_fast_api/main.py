from fastapi import FastAPI, Form, Depends

from fastapi.responses import HTMLResponse, Response, JSONResponse, FileResponse

from fastapi.encoders import jsonable_encoder

from starlette.staticfiles import StaticFiles

from pydantic import BaseModel

import json

app = FastAPI()

app.mount("/public", StaticFiles(directory='public'), name='public')

@app.get("/")
def root():
    return {"message":"Hello FastAPI"}


@app.get("/hello/{name}")
def say_hello(name:str):
    return {"message":f"Hello {name}"}


@app.get('/index')
def index():
    html = "<h1 style='color:blue;'>Lorem ipsum dolor sit amet.</h1>"
    return HTMLResponse(html)


@app.get("/index-get-text")
def index_get_text():
        html = "<h1 style='color:blue;'>Lorem ipsum dolor sit amet.</h1>"
        return Response(content=html, media_type='text/plain')



@app.get('/get-json')
def get_json():
    data = {
        "name": "Fast API",
        "version": "1.0",
        "description": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints."
    }
    json_data = jsonable_encoder(data)
    return JSONResponse(json_data)
    # return Response(content=json.dumps(data), media_type="application/json")



# @app.get("/get-html")
# def get_html():
#     return FileResponse("public/index.html")


@app.get("/get-html", response_class = FileResponse)
def get_html():
    return "public/index.html"


@app.get('/get-image')
def get_image():
    return FileResponse("public/fastapi.jpg", media_type="image/jpeg")


@app.get('/download-image')
def download_image():
    return FileResponse(
        "public/fastapi.jpg", 
        media_type="application/octet-stream",
        filename="fast.jpg"
        )


class User(BaseModel):
    email:str
    password:str


def as_user_from_form(
    email:str = Form(...),
    password:str = Form(...)
):
    return User(email=email, password=password)


@app.post("/login")
def login(user: User=Depends(as_user_from_form)):
    return{
        "email":user.email,
        "password":user.password

    }