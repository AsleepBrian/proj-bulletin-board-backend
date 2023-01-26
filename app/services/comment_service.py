from fastapi import Depends

from repositories.comment_repo import CommentRepo
from repositories.schemas import Comment


class CommentService:
    def __init__(self, comment_repo: CommentRepo = Depends()):
        self.comment_repo = comment_repo

    def create_comment(self, comment: Comment):
        self.comment_repo.save(comment)
