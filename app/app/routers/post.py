from fastapi import APIRouter, Depends

from services.post_service import PostService
from services.comment_service import CommentService
from repositories.schemas import PostCreate, PostUpdate, Comment

router = APIRouter(prefix="/post")


@router.post("/create")
def create_post(post: PostCreate, post_service: PostService = Depends()):
    return {"id": post_service.create_post(post)}


@router.get("/search")
def search_post(keyword: str, page: int = 0, post_service: PostService = Depends()):
    return post_service.search_post(keyword, page)


@router.get("/{id}")
def read_post(id: int, post_service: PostService = Depends()):
    return post_service.read_post(id)


@router.post("/{id}/update")
def update_post(id: int, post: PostUpdate, post_service: PostService = Depends()):
    post_service.update_post(post, id)
    return {"detail": "success"}


@router.post("/{id}/comment")
def create_comment(comment: Comment, comment_service: CommentService = Depends()):
    comment_service.create_comment(comment)
    return {"detail": "success"}


@router.delete("/{id}/delete")
def delete_post(id: int, password: str, post_service: PostService = Depends(), comment_service: CommentService = Depends()):
    post_service.delete_post(id, password)
    comment_service.delete_comment(id)
    return {"detail": "success"}
