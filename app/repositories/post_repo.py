from fastapi import Depends
from sqlalchemy.orm import Session

from common.database import get_db
from repositories.models import Post
from repositories.schemas import PostCreate


class PostRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def save(self, post: PostCreate):
        post = Post(
            subject=post.subject,
            content=post.content,
            password=post.password
        )
        self.db.add(post)
        self.db.commit()

        return post
