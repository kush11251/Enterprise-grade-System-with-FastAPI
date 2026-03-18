from fastapi import APIRouter
from services import product_service
router = APIRouter()
@router.get("/products")
def read_products():
    return product_service.get_products()
