from sqlalchemy.orm import Session

from database import models


def get_user_by_id(db: Session, user_id: int):
        return db.query(models.Vk).filter(models.Vk.user_id == user_id).first()