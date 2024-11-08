from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine
from app.schemas.schemas import CategoryCreate
from app.crud import category as crud_category

router = APIRouter()

class Config:
    from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories/", response_model=CategoryCreate)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud_category.create_category(db=db, category=category)

@router.get("/categories/{category_id}", response_model=CategoryCreate)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud_category.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/categories/{category_id}", response_model=CategoryCreate)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud_category.delete_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
