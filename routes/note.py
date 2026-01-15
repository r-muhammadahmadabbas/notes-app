from fastapi import APIRouter
from models.note import Note    
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates


note=APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id" : str(doc["_id"]),
            "title" : doc.get("title",""),
            "desc" : doc.get("desc",""),
            "important" : doc.get("important",False),

            

        })
    return templates.TemplateResponse("index.html",{"request":request , "newDocs": newDocs})


@note.post("/")
async def create_item(request:Request):
    form = await request.form()
    formDict=dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    note= conn.notes.notes.insert_one(formDict)
    return {"Sucess":True}

