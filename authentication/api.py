from ninja import NinjaAPI

from authentication.schema import FreelancerSchema
from authentication.schema import SkillsSchema
from authentication.schema import ExperienceSchema
from authentication.schema import CompanySchema

from authentication.models import Freelancer
from authentication.models import Skills
from authentication.models import Experience
from authentication.models import Company

import bcrypt

api = NinjaAPI()

@api.post("/register")
def register(request,data :FreelancerSchema):
    data = data.dict()
    password = data["password"]
    salt=bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=password.encode(), salt=salt)
    data["password"] = hashed_password
    Freelancer.objects.create(**data)

def register(request,data :CompanySchema):
    Company.objects.create(data.dict())




    

