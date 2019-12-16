from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from uploads.core.models import *

# Register your models here.


class DeliveryBoyAdmin(ModelAdmin):
    search_fields = ['name','id']
    list_display = ('id', 'name','age','address','phone_no','email_id','lanaguage_know','education_qualification','gender','married_status','created_on')
    list_display_links = ('name',)


class FileUploadAdmin(ModelAdmin):
    list_display = ('uploader_link',)
    list_display_links = ('uploader_link',)

admin.site.register(DeliveryBoy,DeliveryBoyAdmin)
admin.site.register(FileUpload,FileUploadAdmin)