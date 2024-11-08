# app/routes/supplier.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import SessionLocal, engine

from app.crud import supplier as crud_supplier
from app.schemas.schemas import SupplierCreate

router = APIRouter()

class Config:
    from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        



@router.post("/suppliers/", response_model=SupplierCreate)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    return crud_supplier.create_supplier(db=db, supplier=supplier)

@router.get("/getsuppliers/")
def get_suppliers( db: Session = Depends(get_db)):
    return crud_supplier.get_suppliers(db=db)

@router.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud_supplier.get_supplier_by_id(db=db, supplier_id=supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

