from django.db import models

# Create your models here.

class carouselModel(models.Model):
    Titile=models.CharField(max_length=75)
    Description=models.TextField()
    ButtonText=models.CharField(max_length=30)
    Image=models.ImageField(upload_to="carousel")
    Display=models.BooleanField(default=True)
    Date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Titile}-{self.Display }"
    
class AssosiationMembersModel(models.Model):
    Name=models.CharField(max_length=30)
    Desigination=models.CharField(max_length=30)
    Year=models.CharField(max_length=10)
    ProfilePic=models.ImageField(upload_to="Assosiation Members")

    def __str__(self):
        return f"{self.Name}-{self.Desigination}"
    
class PlacementModel(models.Model):
    Name=models.CharField(max_length=30)
    Batch=models.CharField(max_length=10)
    Placed=models.BooleanField(default=True)
    Desigination=models.CharField(max_length=30)
    LPA=models.PositiveIntegerField(null=False)
    StartUp=models.BooleanField(default=False)
    Company=models.CharField(max_length=30)
    ProfilePic=models.ImageField(upload_to="Placement profile",null=True,blank=True)
    Placedon=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.Name}-{self.Batch}"
    