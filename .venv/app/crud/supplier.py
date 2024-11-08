from sqlalchemy.orm import Session
from app.db.models.models import Supplier
from app.schemas.schemas import SupplierCreate


def create_supplier(db: Session, supplier: SupplierCreate):
    db_supplier = Supplier(
        name=supplier.name,
        contact_email=supplier.contact_email,
        phone=supplier.phone,
        address=supplier.address,
        city=supplier.city,
        state=supplier.state,
        postal_code=supplier.postal_code,
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_suppliers(db: Session):
    return db.query(Supplier).all()


def get_supplier_by_id(db: Session, supplier_id: int):
    return db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()




def delete_supplier(db: Session, supplier_id: int):
    db_supplier = db.query(Supplier).filter(Supplier.supplier_id == supplier_id).first()
    if db_supplier is None:
        return None

    db.delete(db_supplier)
    db.commit()
    return db_supplier
