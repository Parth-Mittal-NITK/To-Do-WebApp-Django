from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField( max_length=50)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True) #Added automatically each time an object is created

    
    def __str__(self):
        return self.title
    