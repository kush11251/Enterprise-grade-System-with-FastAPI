from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://user:password@host:port/dbname')
db_session = sessionmaker(bind=engine)()
