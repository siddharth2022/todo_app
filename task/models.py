from django.db import models

# Create your models here.
class task(models.Model):
    
    task_name= models.CharField(max_length=100)
    mark_complete = models.IntegerField(default=0)
    closed_date = models.DateTimeField(default=None, null=True)
    description = models.CharField(max_length=500, default=None)

    def __str__(self):
        return self.task
