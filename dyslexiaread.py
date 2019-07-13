# reading for Dyslexia 

def getFile(): 
    try: 
        fileName = input("Input the file that you want to read: ")
    except:
        print("Sorry we could not read your file")

    return fileName

def createSentence():
    file = open(fileName)
    lineList = [line.split('.') for line in file]

    print(lineList)

fileName = getFile()
sentence = createSentence()
