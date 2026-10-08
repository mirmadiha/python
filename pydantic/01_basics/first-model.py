#
from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id':101, 'name':"Madiha", "is_active":True}
user = User(**input_data) # asterics unpacks the dictionaries otherwise this whole will be trated as one datatype !
print(user)