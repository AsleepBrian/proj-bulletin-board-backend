from fastapi import Depends
from sqlalchemy.orm import Session

from config.database import get_db
from repositories import models, schemas

UNIT_PER_PAGE = 4


class PostRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get(self, id: int) -> schemas.Post:
        post_model: models.Post = self.db.query(models.Post).filter_by(id=id).first()

        comments = []
        for comment in post_model.comment:
            comments.append(comment.content)

        try:
            post = schemas.Post(
                id=id,
                subject=post_model.subject,
                content=post_model.content,
                password=post_model.password,
                comments=comments
            )
        except:
            return None
        else:
            return post
        
    def save(self, post: schemas.PostCreate) -> int:
        post_model = models.Post(
            subject=post.subject,
            content=post.content,
            password=post.password
        )
        self.db.add(post_model)
        self.db.flush()
        self.db.commit()

        return post_model.id

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

    def delete(self, id:int):
        self.db.query(models.Post).filter_by(id=id).delete()
        self.db.commit()

    def search(self, keyword: str, page: int) -> list[schemas.PostMeta]:
        offset = page * UNIT_PER_PAGE
        post_model = self.db.query(models.Post)\
            .filter(models.Post.subject.like(f"%{keyword}%"))\
            .order_by(models.Post.id)\
            .offset(offset)\
            .limit(UNIT_PER_PAGE)

        post_meta_list = []
        for record in post_model:
            post_meta_list.append(
                schemas.PostMeta(
                    id=record.id,
                    subject=record.subject
                )
            )

        return post_meta_list
