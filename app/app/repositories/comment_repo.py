from fastapi import Depends
from sqlalchemy.orm import Session

from config.database import get_db
from repositories import models, schemas


class CommentRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def save(self, comment: schemas.Comment):
        comment_model = models.Comment(
            content=comment.content,
            post_id=comment.post_id
        )
        self.db.add(comment_model)
        self.db.flush()
        self.db.commit()

    def delete(self, post_id: int):
        self.db.query(models.Comment).filter_by(post_id=post_id).delete()
        self.db.commit()
