from __future__ import unicode_literals

from django.db import models
from uploads.core.tests import *



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class FileUpload(models.Model):
	uploader_link = models.CharField(max_length=255, blank=False, default="http://127.0.0.1:8000/uploads/simple/")

	class Meta:
		managed = False
		db_table = 'uploader'




class DeliveryBoy(models.Model):
	name = models.CharField(max_length=255, blank=False)
	age = models.IntegerField(blank=False)
	address = models.TextField(max_length=255, blank=False)
	phone_no = models.CharField(max_length=255, blank=False)
	email_id = models.CharField(max_length=255, blank=False)
	lanaguage_know = models.CharField(max_length=255, blank=False)
	education_qualification = models.CharField(max_length=255, blank=False)
	gender = models.CharField(max_length=255, blank=False)
	married_status = models.CharField(max_length=255, blank=False)
	created_on = UnixTimestampField(auto_now_add=True)


	class Meta:
		managed = False
		db_table = 'delivery_boy'

	def __unicode__(self):
		return unicode(self.name) 

	def save(self, *args, **kwargs):
		if not self.created_on:
			self.created_on = datetime.now()
		super(DeliveryBoy, self).save(*args, **kwargs)


