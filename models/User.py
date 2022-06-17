import pydantic

class User(pydantic.BaseConfig):
    fname: str
    lname: str
    email: str
    
# u1 = User('jean', 'paul', 'rf')
# u1.fname