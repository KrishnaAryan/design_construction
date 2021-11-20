from django.db import models
import uuid
from django.db.models.deletion import CASCADE

from django.db.models.fields import CharField, IntegerField
# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True
def generate_id():
    try:
        obj=SignUpModel.objects.all().last()
        if obj is not None:
            return (obj.id)+1
        else:
            return 1000
    except Exception as e:
        print(e)

class SignUpModel(BaseModel):
    id=models.IntegerField(default=generate_id,primary_key=True,editable=False)
    job_id=models.IntegerField()
    mobile=models.CharField(max_length=13)
    email=models.EmailField()
    new_password=models.CharField(max_length=15)

# def generate_id():
#     try:
#         obj=DashbordModel.objects.all().last()
#         if obj is not None:
#             return(obj.id)+1
#         else:
#             return 1000
#     except Exception as e:
#         print(e)
# class DashbordModel(BaseModel):
#     id=models.IntegerField(default=generate_id,primary_key=True,editable=None)
#     welcome_client_name=models.CharField(max_length=25)
#     my_profile=models.CharField(max_length=100)
#     project_details=models.CharField(max_length=500)
#     payment=models.CharField(max_length=100)
#     e_tracker=models.CharField(max_length=100)
#     project_document=models.CharField(max_length=500)
#     team_assigned=models.CharField(max_length=100)


def generet_id():
    try:
        obj=UserProfileModel.objects.all().last()
        if obj is not None:
            return(obj.id)+1
        else:
            return 1001
    
    except Exception as e:
        print(e)

class Package(BaseModel):
    add_package=models.CharField(max_length=100)
class UserProfileModel(BaseModel):
    id=models.IntegerField(default=generate_id,primary_key=True,editable=None)
    full_name=models.CharField(max_length=25)
    project_id=models.IntegerField()
    mobile=models.CharField(max_length=13)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    package_offered=models.CharField(max_length=200)
    package_details=models.ForeignKey(Package,on_delete=models.CASCADE)

def generate_id():
    try:
        obj=TeamAssignedModel.objects.all().last()
        if id is not None:
            return(obj.id)+1
        else:
            return 1000
    except Exception as e:
        print(e)

class Team(BaseModel):
    team_name=models.CharField(max_length=100)
class TeamAssignedModel(BaseModel):
   # package_choices=(('Project_head','Project_head'),('Project_manager','Project_manager'),('Architect','Architect'),('Structural_engineer','Structural_engineer'),('Procurement_manager','Procurement_manager'),('Project_coordinator','Project_coordinator'),('Project_engineer','Project_Site Engineerengineer'),('Site_engineer','Site_engineer'),('Customer_success','Customer_success'))
    id=models.IntegerField(default=generate_id,primary_key=True,editable=None)
    team_member_details=models.ForeignKey(Team,on_delete=models.CASCADE)

def generate_id():
    try:
        obj=ProjectDocumentsModel.objects.all().last()
        if obj is not None:
            return(obj.id)+1
        else:
            return 1000
    except Exception as e:
        print(e)

class Agreements(BaseModel):
   agreements=models.CharField(max_length=100) 
class ProjectDocumentsModel(BaseModel):
   # package_services=(('Agreements','Agreements'),('Documents','Documents'),('Drawings','Drawings'))
    id=models.IntegerField(default=generate_id,primary_key=True,editable=None)
   # documents=models.CharField(max_length=100,choices=package_services)
    documents=models.ForeignKey(Agreements,on_delete=CASCADE)

