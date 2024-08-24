from django.contrib import admin
from app.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']

class UserAdmin1(admin.ModelAdmin):
    list_display = ['name',"start_content"]

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['name',"heading"]

class ImageAdmin(admin.ModelAdmin):
    list_display = ["image"]


admin.site.register(Home,UserAdmin)
admin.site.register(Profile,UserAdmin1)
admin.site.register(Images,ImageAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Subject_experience,ExperienceAdmin)
admin.site.register(Paper,UserAdmin1)
admin.site.register(FoundedProject,UserAdmin1)
admin.site.register(Seminars,UserAdmin1)
admin.site.register(Eventorganized,UserAdmin1)
admin.site.register(InvitedTalks,UserAdmin1)
admin.site.register(Roles,UserAdmin)
admin.site.register(Conferences,UserAdmin1)
