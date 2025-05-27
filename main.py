from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(..., min_length=3, max_length=50, title="Name of the patient", description="Name must be between 3 and 50 characters", examples=["John Doe", "Jane Smith"])] 
    email: EmailStr
    linkedIn: Optional[AnyUrl] = None
    age: int
    weight: Annotated[float, Field(..., gt=0, le=300, strict=True)]
    married: Annotated[bool, Field(default=False, title="Marital Status", description="True if married, False otherwise")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
    
    
def insert_patent_data(patient: Patient):
    
    print(patient.name)
    print(patient.email)
    print(patient.linkedIn)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('inserted')
    
def update_patent_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('updated')
    

patient_info = {
    'name': 'Shreyas',
    'email': 'shr@shr.com',
    'linkedIn': 'https://www.linkedin.com/in/shreyas',
    'age': 43,
    'weight': 70.5,
    'married': False,
    'allergies': ['pollen', 'dust'],
    'contact_details': {
        'phone': '1234567890'
    }
}

patient1 = Patient(**patient_info)

insert_patent_data(patient1)