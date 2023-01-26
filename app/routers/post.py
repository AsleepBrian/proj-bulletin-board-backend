from fastapi import APIRouter, Header, Depends

from services.post_service import PostService
from repositories.schemas import PostCreate, PostUpdate

router = APIRouter(prefix="/posts")


@router.post("/create")
def create_post(post: PostCreate, post_service: PostService = Depends()):
    return post_service.create_post(post)


@router.post("/update")
def update_post(post: PostUpdate, post_service: PostService = Depends()):
    return post_service.update_post(post)
