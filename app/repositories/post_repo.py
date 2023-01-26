from fastapi import Depends
from sqlalchemy.orm import Session

from common.database import get_db
from repositories.models import Post


class PostRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def save(self, subject: str, content: str, password: str):
        post = Post(subject=subject, content=content, password=password)
        self.db.add(post)
        self.db.commit()
