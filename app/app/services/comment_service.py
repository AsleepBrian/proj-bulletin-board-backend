from fastapi import Depends

from repositories.comment_repo import CommentRepo
from repositories.models.models import Comment


class CommentService:
    def __init__(self, comment_repo: CommentRepo = Depends()):
        self.comment_repo = comment_repo

    def create_comment(self, post_id: int, content: str):
        comment = Comment(
            post_id=post_id,
            content=content
        )
        self.comment_repo.save(comment)

    def delete_comment(self, post_id: int):
        self.comment_repo.delete(post_id)
