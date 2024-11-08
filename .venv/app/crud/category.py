from sqlalchemy.orm import Session
from app.db.models.models import Category
from app.schemas.schemas import CategoryCreate

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.category_id == category_id).first()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.category_id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category
