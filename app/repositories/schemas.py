from pydantic import BaseModel


class PostBase(BaseModel):
    subject: str
    content: str
    password: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
