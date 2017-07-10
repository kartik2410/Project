from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Gift(models.Model):
    GiftId = models.CharField(primary_key=True,max_length=50)
    GiftName = models.CharField(max_length=200, null=False, blank=False)
    Description = models.TextField(max_length=500, null=False)
    Image = models.ImageField(upload_to="media/img")
    class Meta:
        db_table = u'Gifts'

