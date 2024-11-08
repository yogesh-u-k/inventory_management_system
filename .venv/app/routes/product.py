from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.schemas.schemas import ProductCreate
from app.crud import products as crud_product
from app.db.database import SessionLocal, engine
from typing import List
from fastapi.templating import Jinja2Templates


router = APIRouter()

templates = Jinja2Templates(directory=".venv/app/templates")

class Config:
    from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@router.post("/products/", response_model=ProductCreate)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = crud_product.create_product(db=db, product=product)
    return db_product

@router.get("/getproducts/")
def get_all_products(request: Request, db: Session = Depends(get_db)):
    products = crud_product.get_products(db=db)
    return templates.TemplateResponse("products.html", {"request": request, "products": products})
# @router.get("/products/{product_id}", response_model=[])
# def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
#     db_product = crud_product.get_product_by_id(db=db, product_id=product_id)
    
#     if db_product is None:
#         raise HTTPException(status_code=404, detail="Product not found")
    
#     return db_product

