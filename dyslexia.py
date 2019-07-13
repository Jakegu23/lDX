# Dyslexia.py
# WIT Hackathon, TEAM lDX
# 13th July 2019

import speech_recognition as sr
import difflib
from collections import Counter


def getFile():
    try:
        fileName = input("What file do you want to read: ")
    except:
        print("Could not find file")

    return fileName


def Record(text_to_read):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Read text: {text_to_read}")
        audio = r.listen(source)
        
        try:
            textSaid = r.recognize_google(audio)
            #print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

    return textSaid

def Compare(textSaid, text_to_read):
    
    import difflib
    s1cnt = Counter(textSaid)
    s2cnt = Counter(text_to_read)
    
    print(f"Differenc: {s1cnt - s2cnt}")

    common_ratio = difflib.SequenceMatcher(None, textSaid, text_to_read).ratio()
    print ('%.1f%% of words common.' % (100*common_ratio))
    
    



fileName = getFile()

with open(fileName,'r') as file:
    data = file.read()
    data = data.lower()

textSaid = Record(data)
Compare(textSaid,data)
print(data)
print(textSaid)






