from django.db import models
    
class students(models.Model):
    name = models.CharField(max_length=45)
    address = models.TextField()
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
