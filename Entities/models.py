from django.db import models

# Create your models here.
class Division(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.id
    
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1024)
    divisionid = models.ForeignKey(Division, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.id