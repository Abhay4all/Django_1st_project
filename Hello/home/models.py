from django.db import models



# Create your models here.

# makemigration - create change and store in a file
# migrate : apply the  pending changes created by make migration

class Contact(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=120)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

