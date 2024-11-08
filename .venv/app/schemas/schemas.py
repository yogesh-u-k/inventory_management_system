
from fastapi import FastAPI


from pydantic import BaseModel
from typing import Optional
# from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Text, ForeignKey, DECIMAL
from decimal import Decimal

class CategoryCreate(BaseModel):
    category_id: int
    name: str
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class SupplierCreate(BaseModel):
    name: str
    supplier_id: int   
    contact_email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None

class ProductCreate(BaseModel):
    product_name: str
    product_id: int
    category: Optional[str] = None
    description: Optional[str] = None
    supplier_id: int
    sku: str
    unit_price: Decimal
    supplier_id: int
    cost_price: Optional[float] = None



    # db_product = Product(
    #     product_name=product.product_name,
    #     category=product.category,
    #     description=product.description,
    #     supplier_id=product.supplier_id,
    #     sku=product.sku,
    #     unit_price=product.unit_price,
    #     product_id=product.product_id
    #     # cost_price=product.cost_price
    # )



class InventoryCreate(BaseModel):
    product_id: int
    quantity_in_stock: int
    supplier_id: int
    unit_price: float
    total_value: Optional[float] = None
    product_name: str
    description : str

    
