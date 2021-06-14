from django.db import models
    
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['Network']) < 3:
            errors["Network"] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["dec"] = "description should be at least 10 characters"
        
        return errors
        
class Show(models.Model):
    title = models.CharField(max_length=255)
    Network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
