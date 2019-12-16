from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.forms import DocumentForm
from uploads.core.tests import *
from uploads.core.models import *

import csv
import os

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            print 'FILE STARTED TO UPLOADING....'
            try:
                myfile = request.FILES['myfile']
            except Exception as e:
                return render(request, 'core/simple_upload.html')

            file_data = myfile.read().decode("utf-8")     

            lines = file_data.split("\n")
            print lines
            try:
                for i in range(1,len(lines)):
                    l = lines[i].split(',')
                    deliver_boy = DeliveryBoy()
                    deliver_boy.name = l[0]
                    deliver_boy.age = l[1]
                    deliver_boy.address = l[2]
                    deliver_boy.phone_no = l[3]
                    deliver_boy.email_id = l[4]
                    deliver_boy.lanaguage_know = l[5]
                    deliver_boy.education_qualification = l[6]
                    deliver_boy.gender = l[7]
                    deliver_boy.married_status = l[8]
                    deliver_boy.save()
            except Exception as e:
                print e

            deliveryboyList = DeliveryBoy.objects.all()
            return render(request, 'core/list.html', {"data": deliveryboyList})
    except:
        print 'please upload file'


    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def listing_of_delivery_boy(request):
    deliveryboyList = DeliveryBoy.objects.all()
    print deliveryboyList
    return render(request, 'core/list.html', {"data": deliveryboyList})

def add_delivery_boy(request):
    return render(request, 'core/add_delivery_boy.html')

