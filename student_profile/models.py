from django.db import models

# Create your models here.


class Student(models.Model):
# This model will show all of the students profile details, listed by student_name
	sex_choices = (
	('Male','Male'),
	('Female','Female')
	)
	
	id_no = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	sex = models.CharField(max_length=6, choices=sex_choices)
	birth_day = models.DateField('Date of birth')
	gmail = models.CharField(max_length=40)
	address = models.TextField()
	institute = models.CharField(max_length=10)
	
	def __str__(self):
		return self.name
		
