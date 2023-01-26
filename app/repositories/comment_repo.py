from fastapi import Depends
from sqlalchemy.orm import Session

from common.database import get_db
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
