from models import Product
from utils import db_session
class ProductRepository:
    def get_products(self):
        return db_session.query(Product).all()
