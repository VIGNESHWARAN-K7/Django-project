from django.db import models

# Create your models here.
class Home(models.Model):
    name="Home"
    content=models.TextField(max_length=1000, blank=True)

class Profile(models.Model):
    name="Profile"
    start_content=models.TextField(max_length=500, blank=True)
    color_text=models.CharField(max_length=500,blank=True)
    end_content=models.TextField(max_length=500, blank=True)

class Images(models.Model):
    image=models.ImageField(upload_to="images/",blank=True)



class Experience(models.Model):
    name="Experience"
    heading=models.TextField(max_length=50,blank=True)
    list=models.TextField(max_length=500, blank=True)

class Subject_experience(models.Model):
    name="Subject_experience"
    heading=models.TextField(max_length=50,blank=True)
    content=models.TextField(max_length=1000, blank=True)
    
class Paper(models.Model):
    name="Paper_publication"
    start_content=models.TextField(max_length=500, blank=True)
    color_text=models.CharField(max_length=500,blank=True)
    end_content=models.TextField(max_length=500, blank=True)
class FoundedProject(models.Model):
    name="Founded_Project"
    start_content=models.CharField(max_length=500, blank=True)
    color_text=models.CharField(max_length=500,blank=True)
    end_content=models.CharField(max_length=500, blank=True)

class Seminars(models.Model):
    name="Seminars"
    start_content=models.CharField(max_length=500, blank=True)
    color_text=models.CharField(max_length=500,blank=True)
    end_content=models.CharField(max_length=500, blank=True)

class Eventorganized(models.Model):
    name="EventOrganized"
    start_content=models.CharField(max_length=500, blank=True)
    color_text=models.CharField(max_length=500,blank=True)
    end_content=models.CharField(max_length=500, blank=True)
class InvitedTalks(models.Model):
    name="Invited_Talks"
    start_content=models.CharField(max_length=500, blank=True)
    color_text=models.CharField(max_length=500,blank=True)
    end_content=models.CharField(max_length=500, blank=True)
class Roles(models.Model):
    name="Roles and responsibilities"
    content=models.CharField(max_length=500, blank=True)
class Conferences(models.Model):
    name="Conferences"
    start_content=models.CharField(max_length=500, blank=True)
    color_text=models.CharField(max_length=500,blank=True)
    end_content=models.CharField(max_length=500, blank=True)

    # class Meta:
    #     db_table = 'P0rtfolio_table'
        