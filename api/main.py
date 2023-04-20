from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import json 
from fastapi.responses import JSONResponse

origins = ["*"]
app = FastAPI()

app.add_middleware(
    
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('../cleaned_data/years_all.json') as f:
  data = json.load(f)


@app.get('/')
async def get_all_posts():
    return JSONResponse(content=data)

@app.get('/{id}')
async def get_one_post(id:int):
    post = [post for post in data if post['id'] == id]
    return post[0]