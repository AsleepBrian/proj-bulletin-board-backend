from fastapi import Depends
from sqlalchemy.orm import Session

from common.database import get_db
from repositories import models, schemas


class PostRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get(self, id: int):
        post: models.Post = self.db.query(models.Post).filter_by(id=id).first()
        if post is None:
            return None
        
        return schemas.Post(
            id=id,
            subject=post.subject,
            content=post.content,
            password=post.password
        )

    def save(self, post: schemas.PostCreate):
        post = models.Post(
            subject=post.subject,
            content=post.content,
            password=post.password
        )
        self.db.add(post)
        self.db.commit()

        return post

    def update(self, post: schemas.PostUpdate, id:int):
        self.db.query(models.Post)\
            .filter_by(id=id)\
            .update(
            {
                "subject": post.subject,
                "content": post.content
            }
        )
        self.db.commit()

        return post

    def delete(self, id:int):
        self.db.query(models.Post).filter_by(id=id).delete()
        self.db.commit()
