from pydantic import BaseModel


class PostCreateRequest(BaseModel):
    subject: str
    content: str
    password: str


class PostUpdateRequest(BaseModel):
    subject: str
    content: str
    password: str


class CommentCreateRequest(BaseModel):
    post_id: int
    content: str
