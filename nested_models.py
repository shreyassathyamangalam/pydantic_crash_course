from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address
    
address_dict = {
    'city': 'Bengaluru',
    'state': 'Karnataka',
    'zip_code': '560001'
}

# Create an instance of Address using the dictionary
address1 = Address(**address_dict)

patient_dict = {
    'name': 'Shreyas',
    'age': 43,
    'gender': 'male',
    'address': address1
}

# Create an instance of Patient using the dictionary
patient1 = Patient(**patient_dict) # '**' is used to unpack the dictionary into keyword arguments

print(patient1)
# easy to access the nested model
print(patient1.name)
print(patient1.address.city)  # Output: Bengaluru
print(patient1.address.state)  # Output: Karnataka
print(patient1.address.zip_code)  # Output: 560001
