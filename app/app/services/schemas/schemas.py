from pydantic import BaseModel


class PostCreate(BaseModel):
    subject: str
    content: str
    password: str


class PostUpdate(BaseModel):
    id: int
    subject: str
    content: str


class Post(BaseModel):
    id: int
    subject: str
    content: str
    password: str
    comments: list[str] | None = None


class PostMeta(BaseModel):
    id: str
    subject: str


class Comment(BaseModel):
    post_id: int
    content: str
