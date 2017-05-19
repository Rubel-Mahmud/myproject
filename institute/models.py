from django.db import models

# Create your models here.

class Institute(models.Model):
# This model will show all of institute list, listed by student_name
	student_id = models.IntegerField(primary_key=True)
	student_name = models.CharField(max_length=30)
	institute = models.CharField(max_length=10)
	
	def __str__(self):
		return self.student_name

