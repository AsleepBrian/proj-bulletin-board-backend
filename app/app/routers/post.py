import logging

from fastapi import APIRouter, Depends, Body

from services.post_service import PostService
from services.comment_service import CommentService
from routers.schemas.post_requests import PostCreateRequest, PostUpdateRequest
from routers.schemas.post_response import PostSearchResponse, PostMeta, PostReadResponse

router = APIRouter(prefix="/posts")

logging.config.fileConfig('config/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@router.post("/create")
def create_post(post: PostCreateRequest, post_service: PostService = Depends()):
    logger.info(f"body: {post}")
    id = post_service.create_post(post)

    return {"id": id}


@router.get("/search")
def search_post(keyword: str, page: int = 0, post_service: PostService = Depends()):
    logger.info(f"body: keyword={keyword} page={page}")
    post_meta_list = post_service.search_post(keyword, page)
    post_search_response = PostSearchResponse(
        posts=[]
    )

    for post_meta in post_meta_list:
        post_search_response.posts.append(
            PostMeta(
                id=post_meta.id,
                subject=post_meta.subject
            )
        )

    return post_search_response


@router.get("/{id}")
def read_post(id: int, post_service: PostService = Depends()):
    logger.info(f"body: id={id}")
    post = post_service.read_post(id)

    return PostReadResponse(
        id=post.id,
        subject=post.subject,
        content=post.content,
        password=post.password,
        comments=post.comments
    )


@router.post("/{id}")
def update_post(id: int, post: PostUpdateRequest, post_service: PostService = Depends()):
    logger.info(f"body: id={id} {post}")
    post_service.update_post(post, id)

    return {"detail": "success"}


@router.delete("/{id}")
def delete_post(id: int, password: str = Body(embed=True), post_service: PostService = Depends()):
    logger.info(f"body: id={id}, password={password}")
    post_service.delete_post(id, password)

    return {"detail": "success"}


@router.post("/{id}/comment")
def create_comment(id: int, content: str = Body(embed=True), comment_service: CommentService = Depends()):
    logger.info(f"body: {content}")
    comment_service.create_comment(id, content)

    return {"detail": "success"}
