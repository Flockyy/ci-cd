import pydantic

class User(pydantic.BaseConfig):
    fname: str
    lname: str
    email: str
