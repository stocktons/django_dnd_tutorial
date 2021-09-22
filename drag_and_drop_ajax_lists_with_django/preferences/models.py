from django.db import models

class StudentUser(models.Model):
    username = models.CharField(max_length=20)

class PartnerPreferences(models.Model):
    username = models.CharField(max_length=20)
    partner = models.ManyToManyField(StudentUser, through='StudentPartnerPreferences')

class StudentPartnerPreferences(models.Model):
    partnerpreferences = models.ForeignKey(PartnerPreferences, on_delete=models.PROTECT)
    studentuser = models.ForeignKey(StudentUser, on_delete=models.PROTECT)
    active = models.BooleanField()
    order = models.IntegerField()
    
    class Meta():
        ordering = ['order',]

