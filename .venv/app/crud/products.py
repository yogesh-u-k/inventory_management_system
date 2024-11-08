# In your CRUD file
from sqlalchemy.orm import Session
from app.db.models.models import Product
from app.schemas.schemas import ProductCreate  

def create_product(db: Session, product: ProductCreate):
    
    db_product = Product(
        product_name=product.product_name,
        category=product.category,
        description=product.description,
        supplier_id=product.supplier_id,
        sku=product.sku,
        unit_price=product.unit_price,
        product_id=product.product_id,
        cost_price=product.cost_price
    )
    
    
    db.add(db_product)
    db.commit()
    db.refresh(db_product)  
    return db_product


def get_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()
