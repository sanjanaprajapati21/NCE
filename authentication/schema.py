from ninja import ModelSchema
from authentication.models import Freelancer
from authentication.models import Experience
from authentication.models import Skills
from authentication.models import Company


class FreelancerSchema(ModelSchema):
    class Config:
        model = Freelancer
        model_exclude = ("id","profile_picture", "description","certificates","skills", )

class SkillsSchema(ModelSchema):
    class Config:
        model= Skills
        model_fields = ("__all__")

class ExperienceSchema(ModelSchema):
    class Config:
        model = Experience
        model_fields = ("__all__")

class CompanySchema(ModelSchema):
    class Config:
        model = Company
        model_exclude = ("id","profile_picture", "description", "contact_number")
        
        