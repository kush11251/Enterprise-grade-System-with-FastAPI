from fastapi import APIRouter
from services import user_service
router = APIRouter()
@router.get("/users")
def read_users():
    return user_service.get_users()
