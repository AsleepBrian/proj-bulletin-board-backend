from fastapi import Depends

from repositories.post_repo import PostRepo
from repositories.schemas import PostCreate, PostUpdate


class PostService:
    def __init__(self, post_repo: PostRepo = Depends()):
        self.post_repo = post_repo

    def create_post(self, post: PostCreate):
        return self.post_repo.save(post)

    def update_post(self, post: PostUpdate):
        return self.post_repo.update(post)
