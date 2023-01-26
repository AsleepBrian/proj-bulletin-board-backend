from fastapi import APIRouter, Header, Depends

from services.post_service import PostService
from repositories.schemas import PostCreate

router = APIRouter(prefix="/posts")


@router.post("/create")
def create_post(post: PostCreate, post_service: PostService = Depends()):
    return post_service.create_post(post)