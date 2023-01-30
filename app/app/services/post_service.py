from fastapi import Depends, HTTPException, status

from repositories.post_repo import PostRepo
from services.schemas.schemas import Post, PostMeta, PostCreate, PostUpdate
from routers.schemas.post_requests import PostCreateRequest, PostUpdateRequest


class PostService:
    def __init__(self, post_repo: PostRepo = Depends()):
        self.post_repo = post_repo

    def read_post(self, id: int) -> Post:
        post = self.post_repo.get(id)
        if post is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        
        return post

    def create_post(self, post: PostCreateRequest) -> int:
        id = self.post_repo.save(
            PostCreate(
                subject=post.subject,
                content=post.content,
                password=post.password
            )
        )
        return id

    def update_post(self, post: PostUpdateRequest, id: int):
        if self.read_post(id).password != post.password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        self.post_repo.update(
            PostUpdate(
                id=id,
                subject=post.subject,
                content=post.content
            )
        )

    def delete_post(self, id: int, password: str):
        if self.read_post(id).password != password:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        self.post_repo.delete(id)

    def search_post(self, keyword: str, page: int) -> list[PostMeta]:
        post_meta_list = self.post_repo.search(keyword, page)
        return post_meta_list
