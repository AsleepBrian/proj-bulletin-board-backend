from fastapi import Depends, HTTPException, status

from repositories.post_repo import PostRepo
from repositories.schemas import PostCreate, PostUpdate, Post


class PostService:
    def __init__(self, post_repo: PostRepo = Depends()):
        self.post_repo = post_repo

    def read_post(self, id: int) -> Post:
        return self.post_repo.get(id)

    def create_post(self, post: PostCreate):
        return self.post_repo.save(post)

    def update_post(self, post: PostUpdate, id: int):
        if self.read_post(id).password != post.password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        return self.post_repo.update(post, id)
