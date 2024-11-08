
from app.db.database import SessionLocal, Base , engine
from fastapi import FastAPI
from app.db.models.models import  Category, Supplier, Product, Inventory
from app.routes import category, supplier, product, inventory

app= FastAPI()
app.include_router(category.router, prefix="/api")
app.include_router(inventory.router, prefix="/api")
app.include_router(product.router, prefix="/api")
app.include_router(supplier.router, prefix="/api")



