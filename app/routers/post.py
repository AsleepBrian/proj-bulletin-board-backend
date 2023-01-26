from fastapi import APIRouter, Header, Depends

from services.post_service import PostService

router = APIRouter(prefix="/posts")


@router.get("/create")
def create_post(subject: str, content: str, password: str, post_service: PostService = Depends()):
    post_service.create_post(subject, content, password)
    return "success"