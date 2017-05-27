from __future__ import unicode_literals
from django.db import models

class Forum(models.Model):
	user = models.CharField(max_length=25, default="anonymous")
	title = models.CharField(max_length=30)
	content = models.CharField(max_length=250)
	image = models.ImageField(upload_to = './storage/', null=True)
	date = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	def __str__(self):
   		return "{} ".format(self.id) + self.title

class Comment(models.Model):
	forum = models.ForeignKey(Forum, null=False, on_delete=models.CASCADE)
	comment = models.CharField(max_length=140)
	date = models.DateTimeField(auto_now_add=True)
	# user

	def __str__(self):
   		return "{} ".format(self.id) + self.comment

# class User(models.Model):
# 	ip = models.IntegerField()	
		

