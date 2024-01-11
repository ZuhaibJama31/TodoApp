from django.db import models

# Create your models here.

class MakeList(models.Model):

    STATUS_CHOICES =[
        ('Incomplete' ,'Incomplete'),
        ('Complete' ,'Complete'),
    ]
    Title = models.CharField(max_length = 100)
    Description = models.TextField(max_length = 100)
    Status = models.CharField(max_length = 100, choices = STATUS_CHOICES ) 
    Date = models.DateTimeField(auto_now= False)

    def __str__(self):
        return f"Title: {self.Title}, Description: {self.Description}, Status: {self.Status}, Date: {self.Date}"