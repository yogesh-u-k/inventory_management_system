# In your CRUD file
from sqlalchemy.orm import Session
from app.db.models.models import Inventory, Product
from app.schemas.schemas import InventoryCreate  

def create_inventory(db: Session, inventory: InventoryCreate):
    
    db_inventory = Inventory(
        
        product_id=inventory.product_id,
        quantity_in_stock=inventory.quantity_in_stock,
        total_value=inventory.total_value,
        unit_price=inventory.unit_price,
        supplier_id=inventory.supplier_id,
        product_name=inventory.product_name,
        description=inventory.description
    )
    db.add(db_inventory) 
    db.commit()  
    db.refresh(db_inventory)  
    return db_inventory

def get_inventory(db: Session):
    return db.query(Inventory).all()


def get_inventory_by_id(db: Session, inventory_id: int):
    return db.query(Inventory).filter(Inventory.inventory_id == inventory_id).first()

def get_inventory_with_product_details(db: Session):
    
    result = db.query(Product.product_name, Inventory.quantity_in_stock, Inventory.total_value) \
               .join(Inventory, Product.product_id == Inventory.product_id) \
               .all()
    
    return result

