from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com', 'icici.com']
        # extract domain from email
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f"Email domain '{domain}' is not allowed. Allowed domains are: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        # Transform name to uppercase
        return value.upper()
    
    @field_validator('age', mode='after') # mode='before' allows validation before any other processing
    @classmethod
    def validate_age(cls, value):
        if 0 < value <= 100:
            return value
        else:
            raise ValueError("Age must be between 1 and 100")
        

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')


patient_info = {
    'name': 'Shreyas',
    'email': 'abc@hdfc.com',
    'age': '43',
    'weight': 70.5,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '1234567890'
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)