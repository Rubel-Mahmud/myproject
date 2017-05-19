from django.db import models

# Create your models here.

class District(models.Model):
# This model will show all district list 	
	dis_choices = (
	('Ga','Gaibandha'),
	('Na','Nator'),
	('Bo','Bogra'),
	('Di','Dinajpur')
	)
	
	student_id = models.IntegerField(primary_key=True)
	student_name = models.CharField(max_length=30)
	district = models.CharField(max_length=2, choices=dis_choices, default='Gaibandha')
	
	def __str__(self):
		return self.student_name
	
