#!/usr/bin/python3

import cv2
import numpy as np 
import pytesseract
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import nltk

# Reading image
frame=cv2.imread('/root/Desktop/Playground/Opencv-python/news.png',cv2.IMREAD_COLOR)

#pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
# -l is for language, here it  is english
# --oem 1 for using LSTM OCR Engine
config = ('-l eng --oem 1 --psm 3')

# extracting text from image
text=pytesseract.image_to_string(frame,config=config)

# Tokenizing words
text=word_tokenize(text)

# removing Stopwords
new_words=[i for i in text if i.lower() not in stopwords.words('english')]

# Plotting graph 
nlp=nltk.FreqDist(new_words)
nlp.plot()

