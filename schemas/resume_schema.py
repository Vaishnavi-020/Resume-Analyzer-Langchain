from pydantic import BaseModel,Field
from typing import List,Optional

class Project(BaseModel):
    title:str=Field(description="Name of the project")
    description:Optional[str]=None
    tech_stack:List[str]=[]

class ResumeSchema(BaseModel):
    name:str
    skills:List[str]
    education:List[str]
    experience:List[str]
    certifications:List[str]
    projects:List[Project]
    