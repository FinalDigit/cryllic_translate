#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

russian = False
text = sys.argv[1]
print(text)

if len(sys.argv) == 3:
	if sys.argv[2].lower() == 'russian':
		russian = True
else:
	pass

def translation(text):
	'''Convert text from English to Russian(cryllic). '''

	symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

	# For Python 3
	#tr = {ord(a):ord(b) for a, b in zip(*symbols)}

	# For Python 2.*:
	# Russian(cryllic) to English
	tr_RtoE = dict( [ (ord(a), ord(b)) for (a, b) in zip(*symbols) ] )
	# English to Russian(cryllic)
	tr_EtoR = dict( [ (ord(a), ord(b)) for (b, a) in zip(*symbols) ] )

	# Sample Texts
	#text = u'Лорем ипсум долор сит амет'
	#text = u'Lorem ipsum dolor sit amet'
	if russian == True:
		text_tr = text.translate(tr_EtoR)
	else: # Cryllic to English as Default
		text_tr = text.translate(tr_RtoE)
	print(text_tr) 
	return text_tr

translation(text.decode('utf-8'))
