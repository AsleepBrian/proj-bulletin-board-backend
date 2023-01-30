from pydantic import BaseModel


class PostMeta(BaseModel):
    id: str
    subject: str


class PostSearchResponse(BaseModel):
    posts: list[PostMeta]


class PostReadResponse(BaseModel):
    id: int
    subject: str
    content: str
    password: str
    comments: list[str] | None = None
