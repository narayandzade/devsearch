from django.db import models
import uuid
# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.png")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link= models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True)
    vote_total = models.IntegerField(null=True, blank=True, default=0)
    vote_ratio = models.IntegerField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)

    #Added by Rishav
    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(max_length=200, null=True, blank=True)
    value = models.CharField(max_length=200,null=True, blank=True, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class PersonalDetails(models.Model):

    gender_options=(
        ("M", "Male"),("F", "Female"),
    )
    
    fullName= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    mobile= models.CharField(max_length=20)
    gender = models.CharField(max_length=100, choices=gender_options)


    def __str__(self):

        return self.fullName

