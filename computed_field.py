from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('inserted')

    

patient_info = {
    'name': 'Shreyas',
    'email': 'abc@hdfc.com',
    'age': '65',
    'weight': 70.5, # in kg
    'height': 1.76, # in mtr
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '1234567890',
        'emergency': '9876543210'
    }
}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)