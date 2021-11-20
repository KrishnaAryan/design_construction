from django.contrib import admin
from .models import *
admin.site.site_header=''
admin.site.index_title='Welcome to our site'
# Register your models here.
@admin.register(SignUpModel)
class SignUpAdmin(admin.ModelAdmin):
    list_display=['id','job_id','mobile','email']
    search_fields=['phone_number','job_id']

@admin.register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display=['id','full_name','project_id','mobile','email','address','location','package_offered','package_details']
    search_fields=['phone_number','full_name']

@admin.register(TeamAssignedModel)
class TeamAssignedAdmin(admin.ModelAdmin):
    list_display=['id','team_member_details']
    search_fields=['id']


@admin.register(ProjectDocumentsModel)
class Project_DocumentsAdmin(admin.ModelAdmin):
    list_display=['id','documents']
    search_fields=['id']