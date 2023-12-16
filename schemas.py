from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    price: str
    rating: str
    category: str