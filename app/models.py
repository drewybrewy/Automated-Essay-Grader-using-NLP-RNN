from django.db import models

# Create your models here.
class Students(models.Model):

    roll_no =  models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)

    class Meta:

        db_table = "Students"

class Teachers(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)

    class Meta:

        db_table = "Teachers"

class Essays(models.Model):

    title = models.CharField(max_length = 500)
    essay = models.CharField(max_length = 5000)
    grade = models.IntegerField()
    students = models.ForeignKey(Students,default = 1, on_delete = models.CASCADE)

    class Meta:

        db_table = "Essays"
