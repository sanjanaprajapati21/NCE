from django.contrib import admin
from authentication.models import Freelancer
from authentication.models import Skills
from authentication.models import Experience
from authentication.models import Company
# Register your models here.


admin.site.register(Freelancer)
admin.site.register(Company)
admin.site.register(Experience)
admin.site.register(Skills)


