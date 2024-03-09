import datetime
from typing import Optional

from sqlmodel import Field, SQLModel, Session, create_engine, select

from api.util.logging import logger
from api.util.settings import app_settings


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str


engine = create_engine(app_settings.db_connection_string)


def get_session():
    with Session(engine) as session:
        yield session


def init_db() -> None:
    logger.info("Creating tables")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        user = session.exec(
            select(User).where(User.id == 1)
        ).first()
        if not user:
            logger.info("Creating default user")
            session.add(User(id=1, username="default"))
            session.commit()


def get_user(session: Session, user_id: int) -> Optional[User]:
    user = session.exec(
        select(User).where(User.id == user_id)
    ).first()
    return user
