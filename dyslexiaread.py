#reading for Dyslexia 

def getFile():
    try:
        fileName = input("Input the file that you want to read:")
    except:
        print("Sorry we count not read your file")

    return fileName

def createSentence():
    read = open(fileName)
        while True: 
            line = read.readline()
            print(line)
        if not line:
            break 
    read.close()