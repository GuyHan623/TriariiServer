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
    
class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    divisionid = models.ForeignKey(Division, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
    

class Dispatch(models.Model):
    id = models.AutoField(primary_key=True)
    messageid = models.ForeignKey(Message, on_delete=models.CASCADE)
    agentid = models.ForeignKey(Agent, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.id