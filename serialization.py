from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str = 'Male'  # Default (for exclude_unset example)
    address: Address
    
address_dict = {
    'city': 'Bengaluru',
    'state': 'Karnataka',
    'zip_code': '560001'
}

# Create an instance of Address using the dictionary
address1 = Address(**address_dict)

# removed 'male' from the dictionary to demonstrate exclude_unset
patient_dict = {
    'name': 'Shreyas',
    'age': 43,
    'address': address1
}

# Create an instance of Patient using the dictionary
patient1 = Patient(**patient_dict) # '**' is used to unpack the dictionary into keyword arguments


# Serialize the Patient instance to a dictionary
temp = patient1.model_dump()  # This will return a dictionary representation of the Patient instance

print(temp)
print(type(temp))

temp2 = patient1.model_dump_json()  # This will return a JSON string representation of the Patient instance
print(temp2)
print(type(temp2))

# the include and exclude parameters can be used to control which fields are included in the output
temp3 = patient1.model_dump(include={'name', 'age'})  # Only include 'name' and 'age'
print(temp3)

temp4 = patient1.model_dump(exclude={'address':['state']})  # Exclude 'state' from the address
print(temp4)

# exclude_unset can be used to exclude fields that were not set during initialization
temp5 = patient1.model_dump(exclude_unset=True)  # Exclude fields that were not set
print(temp5)
