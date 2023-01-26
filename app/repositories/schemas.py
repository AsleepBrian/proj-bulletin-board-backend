from pydantic import BaseModel


class PostBase(BaseModel):
    subject: str
    content: str
    password: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase):
    id: int


class PostMeta(BaseModel):
    id: str
    subject: str


class Comment(BaseModel):
    post_id: int
    content: str
