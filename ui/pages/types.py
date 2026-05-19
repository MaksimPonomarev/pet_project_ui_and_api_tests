from typing import TypedDict

class Credentials(TypedDict):
    name: str
    password: str
    email: str

class UserInfo(TypedDict):
    first_name: str
    last_name: str
    company: str
    address: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str

class SignupData(TypedDict):
    name: str
    email: str