from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    id: int
    name: Optional[str]
    major: Optional[str]

class Professor(BaseModel):
    id: int
    name: Optional[str]
    position: Optional[str]
    office: Optional[str]
    students: Optional[List[Student]]

class Department(BaseModel):
    id: int
    name: Optional[str]
    chairperson: Optional[str]

class Faculty(BaseModel):
    id: int
    name: Optional[str]
    location: Optional[str]
    depts: List[Department]