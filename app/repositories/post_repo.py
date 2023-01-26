from fastapi import Depends
from sqlalchemy.orm import Session

from common.database import get_db
from repositories import models, schemas

UNIT_PER_PAGE = 4


class PostRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get(self, id: int):
        result: models.Post = self.db.query(models.Post).filter_by(id=id).first()
        if result is None:
            return None
        
        return schemas.Post(
            id=id,
            subject=result.subject,
            content=result.content,
            password=result.password
        )

    def save(self, post: schemas.PostCreate):
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

    def search(self, keyword: str, page: int):
        offset = page * UNIT_PER_PAGE
        result = self.db.query(models.Post)\
            .filter(models.Post.subject.like(f"%{keyword}%"))\
            .order_by(models.Post.id)\
            .offset(offset)\
            .limit(UNIT_PER_PAGE)

        post_meta_list = []
        for record in result:
            post_meta_list.append(
                schemas.PostMeta(
                    id=record.id,
                    subject=record.subject
                )
            )

        return post_meta_list
