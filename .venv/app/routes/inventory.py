
from sqlalchemy import join
from app.db.models.models import Product, Inventory
from app.db.database import SessionLocal, engine

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas import InventoryCreate
from app.crud import inventory as crud_inventory
from typing import List
router = APIRouter()


class Config:
    from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@router.post("/inventory/", response_model=InventoryCreate)
def create_inventory(inventory: InventoryCreate, db: Session = Depends(get_db)):
    db_inventory = crud_inventory.create_inventory(db=db, inventory=inventory)
    return db_inventory

@router.get("/getinventory/", response_model=List[InventoryCreate])
def get_all_inventory( db: Session = Depends(get_db)):
    inventory_list = crud_inventory.get_inventory(db=db)
    return inventory_list

# @router.get("/inventory/{inventory_id}", response_model=Inventory)
# def get_inventory_by_id(inventory_id: int, db: Session = Depends(get_db)):
#     db_inventory = crud_inventory.get_inventory_by_id(db=db, inventory_id=inventory_id)
    
#     if db_inventory is None:
#         raise HTTPException(status_code=404, detail="Inventory not found")
    
#     return db_inventory
