from django.db import models

# Create your models here.

class Participants(models.Model):
    name= models.CharField(max_length=100, null=True)
    email= models.CharField(max_length=100, null=True)
    phone= models.CharField(max_length=100, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Club(models.Model):
    CATEGORY=(
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name= models.CharField(max_length=100, null=True)
    event= models.CharField(max_length=100, null=True)
    category= models.CharField(max_length=100, null=True, choices=CATEGORY)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class participates(models.Model):
    name= models.ForeignKey(Participants, null=True, on_delete=models.SET_NULL)
    club= models.ForeignKey(Club, null=True, on_delete=models.SET_NULL)
    date_created= models.DateTimeField(auto_now_add=True, null=True)