from pydantic import BaseModel




class Note(BaseModel):
    title: str
    desc: str
    important: bool = None