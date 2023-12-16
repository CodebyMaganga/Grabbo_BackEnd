from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres://admin:oQpfu6lfN0g6hBtOCjC6gwOBsxekjPRS@dpg-cluf91md3nmc7383oro0-a.frankfurt-postgres.render.com/grabbo')

local_session = sessionmaker(bind=engine)

#method to get db
def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()