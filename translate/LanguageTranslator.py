# Language Translator
'''
This scrict provides two functionalities.
1. Language translation: User need to insert source string, source language and destination language
code as input. User will get translated string as output.

2. Language Detection: User need to insert source string as input. User will get detect language
code and confidence as output.

'''
# Import Package
from googletrans import Translator

# Create Translator object
# translator = Translator()
#
# while True:
#     print('\n-------------------------------------')
#     print('Choose Option (Press 0 to exit)')
#     print('Press 1 to proceed')
#
#     option = int(input('Option:'))
#
#     if option==1:
#         srcString = input('Enter source string:')
#
#         # Translate source string in request destination laguage
#         detected = translator.detect(srcString)
#         print('Detected Language:', detected.lang, ' with confidence: ', detected.confidence)
#         srcLang = detected.lang
#         dstLang = input('Enter destination language:')
#
#         # Translate source string in request destination laguage
#         translated = translator.translate(srcString, src= srcLang, dest=dstLang)
#
#         # Print source string
#         #print('Source string:'+ translated.origin)
#
#         # Print source language
#         #print('Source Language:'+ translated.src)
#
#         # Print translated string
#         print('Translated string:'+ translated.text)
#
#         # Print destination laguage
#         print('Destination Language:'+ translated.dest)
#
#         # Print translated string pronunciation
#         print('Destination pronunciation:', translated.pronunciation)
#
#     elif option==0:
#         break
#     else:
#         print('Invalid option')
#         #option=0
#         #break


def Translate(text, language):
    translator = Translator()
    detected = translator.detect(text)
    srcLang = detected.lang
    translated = translator.translate(text, src=srcLang, dest=language)
    return translated
