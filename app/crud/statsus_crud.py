from sqlalchemy.orm import Session
from app import models, schemas


# STATUS CRUD OPERATIONS


def create_status(db: Session, status: schemas.StatusCreate) -> models.Status:
    """Create a new status."""
    db_status = models.Status(**status.model_dump())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def get_status(db: Session, status_id: int) -> models.Status | None:
    """Retrieve status by ID."""
    return db.query(models.status).filter(models.Status.id == status_id).first()


def get_current_status(db: Session) -> models.Status | None:
    """Retrieve latest status."""
    return db.query(models.Status).first()


def get_statuses(db: Session, skip: int = 0, limit: int = 100) -> list[models.Status]:
    """Retrieve a list of statuses."""
    return db.query(models.Status).offset(skip).limit(limit).all()


def update_status(db: Session,status_id: int, status: schemas.StatusCreate) -> models.Status | None:
    """Update the current status."""
    db_status = get_status(db, status_id)

    if not db_status:
        return None

    update_data = status.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_status, field, value)

    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status


def delete_status(db: Session, status_id: int) -> bool:
    """Delete status by ID."""
    db_status = get_status(db, status_id)

    if not db_status:
        return False

    db.delete(db_status)
    db.commit()
    return True