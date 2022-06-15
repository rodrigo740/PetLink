from sqlalchemy.orm import Session

from . import models, schemas


def get_client(db: Session, user_id: int):
    return db.query(models.Client).filter(models.Client.id == user_id).first()


def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, user):
    db_user = models.Client(user.userName, user.address, user.contact, user.name, user.birthday,
                            email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
