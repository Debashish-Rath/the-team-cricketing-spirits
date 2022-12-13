from django.db import models

# Create your models here.
class Player_Registration_Form(models.Model):
    name = models.CharField(max_length=80)
    phone_no = models.BigIntegerField()
    whatsapp_no = models.BigIntegerField()
    role = models.CharField(max_length=50,default='LHB')
    reference_person = models.CharField(max_length=80)
    is_available = models.BooleanField()

    def __str__(self):
        return self.name