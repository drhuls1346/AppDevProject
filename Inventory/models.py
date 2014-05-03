from django.db import models

# This is my sqlite3 table. It has the fields name, unittype, status, email, and phone. all fields
# are character fields except for the status field which is a boolean field and it's default value
# is False.

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