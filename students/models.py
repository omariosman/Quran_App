from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Shaikh(models.Model):
    code= models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sex = models.IntegerField()
    age = models.IntegerField()
    phone_number = models.IntegerField()
    country = models.CharField(max_length=50)
    Ijazah_flag = models.BooleanField()
    classes_days = models.CharField(max_length=100)
    classes_dates = models.DateField()
    current_job = models.CharField(max_length=50)
    marital_status = models.IntegerField()
    donation_flag = models.BooleanField()
    
    def __str__(self):
        return str(self.name)  
    
class Student(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.IntegerField()
    age = models.IntegerField()
    Job = models.CharField(max_length=100)
    Previous_Hefz = models.CharField(max_length=50)
    Weekly_Hefz = models.CharField(max_length=50)
    Tagweed_level = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    donation_flag = models.BooleanField()
    marital_status = models.IntegerField()
    shaikh_code = models.ForeignKey(Shaikh, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)

    
class Mentor(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.IntegerField()
    age = models.IntegerField()
    phone_number = models.IntegerField()
    
    def __str__(self):
        return str(self.name)      
 
    
    
class Surah_Quran(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.name)
    
class Student_Class(models.Model):
    student_code = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    werd = models.CharField(max_length=50)
    werd_grade = models.IntegerField()
    revision = models.CharField(max_length=50)
    revision_grade = models.IntegerField()
    attendance = models.BooleanField()

    
    
    
    
    


