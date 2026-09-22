from fastapi import FastAPI

from database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Books API",
    version="1.0",
    description="Books API CRUD operations",
)



