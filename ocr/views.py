from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Functions.OcrScanner import *
from Functions.LanguageTranslator import *
from Functions.Summarizer import *
from Functions.TextToSpeech import *
import os

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_path = fs.path(filename)
        f=open(uploaded_file_path)
        im=ImageScan(uploaded_file_path)
        return render(request, 'base.html', {
            'uploaded_file_url': uploaded_file_path,
            'im': im
        })
    return render(request, 'base.html')

def translate(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        mylanguage = request.POST['language']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_path = fs.path(filename)
        f=open(uploaded_file_path)
        im=ImageScan(uploaded_file_path)
        trans = Translate(im,mylanguage)
        return render(request, 'translate.html', {
            'uploaded_file_url': uploaded_file_path,
            'im': im,
            'trans': trans
        })
    return render(request, 'translate.html')

def summ(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_path = fs.path(filename)
        f=open(uploaded_file_path)
        im=ImageScan(uploaded_file_path)
        summ = summa(im)
        return render(request, 'summarize.html', {
            'uploaded_file_url': uploaded_file_path,
            'im': im,
            'summ': summ
        })
    return render(request, 'summarize.html')

def tts(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_path = fs.path(filename)
        f=open(uploaded_file_path)
        im=ImageScan(uploaded_file_path)
        Text2Speech(im)
        return render(request, 'tts.html', {
            'uploaded_file_url': uploaded_file_path,
            'im': im,
        })
    return render(request, 'tts.html')