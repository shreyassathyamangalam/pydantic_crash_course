from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
    


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
    'age': '65',
    'weight': 70.5,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '1234567890',
        'emergency': '9876543210'
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)