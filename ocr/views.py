from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from Functions.OcrScanner import *
from Functions.LanguageTranslator import *
from Functions.Summarizer import *
from Functions.TextToSpeech import *
import os

def upload(request):
    if 'myfile' in request.FILES:
    	print('if')
    	myfile = request.FILES['myfile']
    	fs = FileSystemStorage()
    	filename = fs.save(myfile.name, myfile)
    	uploaded_file_path = fs.path(filename)
    	f=open(uploaded_file_path)
    	im=ImageScan(uploaded_file_path)
    	summ = summa(im)
    	return render(request, 'base.html', {
            'uploaded_file_url': uploaded_file_path,
            'im': im,
            'summ': summ
        })
    elif 'tyfile' in request.POST:
        uploaded_file_path = request.POST['tyfile']
        mylanguage = request.POST['language']
        f=open(uploaded_file_path)
        im=ImageScan(uploaded_file_path)
        summ = summa(im)
        trans = Translate(im,mylanguage)
        return render(request, 'base.html', {
            'uploaded_file_url': uploaded_file_path,
            'im': im,
            'summ': summ,
            'trans': trans
        })
    return render(request, 'base.html')

def translate(request):
    if request.method == 'POST':
        text = request.POST['text']
        mylanguage = request.POST['language']
        trans = Translate(text,mylanguage)
        return render(request, 'translate.html', {
            'im': text,
            'trans': trans
        })
    return render(request, 'translate.html')

def summ(request):
    if request.method == 'POST':
    	text = request.POST['text']
    	summ = summa(text)
    	return render(request, 'summarize.html', {
        	'im': text,
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