from django.db import models

class Signup(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
