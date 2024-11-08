from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from app.db.database import SessionLocal, Base , engine
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Text, ForeignKey, DECIMAL
from sqlalchemy.orm import Session

class  Category(Base):
    __tablename__="category"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)
    description = Column(String(100), index=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    
   

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    category = Column(String(50))
    description = Column(Text)
    supplier_id = Column(Integer, ForeignKey("supplier.supplier_id"))
    sku = Column(String(50), unique=True, nullable=False)
    unit_price = Column(DECIMAL(10, 2))
    cost_price = Column(DECIMAL(10, 2))
    
    
    
class Supplier(Base):
    __tablename__="supplier"
    supplier_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    contact_email = Column(String(100), unique=True)
    phone = Column(String(15))
    address = Column(String(255))
    city = Column(String(50))
    state = Column(String(50))
    postal_code = Column(String(10))

  

class Inventory(Base):
    __tablename__ = "inventory"  
    inventory_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id")) 
    product_name = Column(String(100), nullable=False)
    description = Column(Text)
    quantity_in_stock = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey("supplier.supplier_id"))  
    unit_price = Column(DECIMAL(10, 2))
    total_value = Column(DECIMAL(10, 2))
    

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)