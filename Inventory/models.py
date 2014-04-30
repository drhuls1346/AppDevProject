from django.db import models

# Create your models here.

class GPS(models.Model):
    name = models.CharField(max_length=30)
    unittype = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)

    def __unicode__(self):
        return "{} - {} - Out: {} - {} - {}".format(self.name,
                                          self.unittype,
                                          self.status,
                                          self.email,
                                          self.phone)