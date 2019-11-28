from django.contrib import messages
from django.shortcuts import render, redirect
from translate.form import TranslateForm
from translate.LanguageTranslator import Translate


def translate_view(request):
    form = TranslateForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data.get('translate')
        language = form.cleaned_data.get('language')
        translated = Translate(text, language)
    else:
        form = TranslateForm(request.POST)
    context = {'form': form}
    return render(request, 'translate.html', context=context)
