from django.db import models

class Leavelist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surename = models.CharField(max_length=100)
    position = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    type_leave = models.CharField(max_length=100)
    cause = models.CharField(max_length=255)
    date_first = models.DateField()
    date_end = models.DateField()
    date_save = models.DateTimeField()
    status = models.CharField(max_length=100)
    del_flg = models.BooleanField()

    def __str__(self):
        return self.name
