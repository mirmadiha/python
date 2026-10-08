from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  #default value

Product_one = Product({'id':1, 'name':'Shawl', 'price':100.0, 'in_stock': False})

Product_two = Product({'id':2, 'name':'sweater', 'price':210.1})

