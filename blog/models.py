from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length=100, default='')
	text = models.TextField()
	pub_date = models.DateTimeField()
	author = models.ForeignKey(User)
	id = models.AutoField(primary_key=True)

	def __str__ (self):
		return self.title