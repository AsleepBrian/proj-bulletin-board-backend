from fastapi import Depends

from repositories.post_repo import PostRepo


class PostService:
    def __init__(self, post_repo: PostRepo = Depends()):
        self.post_repo = post_repo

    def create_post(self, subject: str, content: str, password: str):
        self.post_repo.save(subject, content, password)
