from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

followers = Table("followers", Base.metadata,
    Column("user_id", String, ForeignKey("users.user_id")),
    Column("follower_id", String, ForeignKey("users.user_id")),
)

class User(Base):
    __tablename__ = "users"
    user_id = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    date_joined = Column(TIMESTAMP)
    date_updated = Column(TIMESTAMP)


class Profile(Base):
    __tablename__ = "profiles"
    user_id = Column(String, primary_key=True)
    name = Column(String)
    heading = Column(String)
    description = Column(String)
    image_url = Column(String)
    followers = relationship("")


class Post(Base):
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    title = Column(String)
    description = Column(String)
    nft_token = Column(String)
    nft_url = Column(String)


# class Reply(Base)
#     __tablename__ = "replies"
#     reply_id = Column(Integer, primary_key=True)
#     user_id = Column(String, ForeignKey("users.user_id"))
#     post_id = Column(Integer, ForeignKey("posts.post_id"))
#     replied_at = Column(DateTime)
#     text = Column(String)

