from fastapi import Depends
from sqlalchemy.orm import Session

from common.database import get_db
from repositories.models import Post
from repositories.schemas import PostCreate, PostUpdate


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

    def update(self, post: PostUpdate):
        self.db.query(Post)\
            .filter_by(id=post.id)\
            .update(
            {
                "subject": post.subject,
                "content": post.content
            }
        )
        self.db.commit()

        return post
