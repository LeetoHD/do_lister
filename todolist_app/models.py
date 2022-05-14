from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class DoList(models.Model):
    
    owner  = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    task = models.CharField(max_length=500)
    do = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " -- " + str(self.do)
