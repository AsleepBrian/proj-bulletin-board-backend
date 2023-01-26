from fastapi import APIRouter, Header, Depends

from services.post_service import PostService
from repositories.schemas import PostCreate, PostUpdate

router = APIRouter(prefix="/posts")


@router.post("/create")
def create_post(post: PostCreate, post_service: PostService = Depends()):
    return post_service.create_post(post)


@router.get("/search")
def search_post(keyword: str, page: int, post_service: PostService = Depends()):
    return post_service.search_post(keyword, page)


@router.get("/{id}")
def read_post(id: int, post_service: PostService = Depends()):
    return post_service.read_post(id)


@router.post("/{id}/update")
def update_post(id: int, post: PostUpdate, post_service: PostService = Depends()):
    return post_service.update_post(post, id)


@router.delete("/{id}/delete")
def delete_post(id: int, password: str, post_service: PostService = Depends()):
    return post_service.delete_post(id, password)
