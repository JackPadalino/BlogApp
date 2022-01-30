from django.db import models # this import standard with django
from django.utils import timezone
from django.contrib.auth.models import User # this import imports the User model that comes with Django
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #the 'auto_now_add=True' argument records the creation date of the post
    #date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    #this sets the reltionship between posts and authors, called a 'one to many' relationship
    #by saying 'on_delete = models.CASCADE' we are saying that 'on the deletion of a user, delete all their posts too'
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} | {self.content} | {self.date_posted} | {self.author}'
    
    def get_absolute_url(self):
        return reverse('post-details',kwargs={'pk':self.pk})