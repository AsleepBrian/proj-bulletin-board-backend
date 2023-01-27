from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

from common.database import Base, engine


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    password = Column(String, nullable=False)


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", backref="comment")


# Base.metadata.create_all(bind=engine)