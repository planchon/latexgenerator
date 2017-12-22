from genClass import *

def interpretProcessedData(processedData):
    index = 0
    latex = latexObj()
    for lines in processedData:
        if lines[0] == "CHAPTER":
            chapter = chapterObj(lines[1])
            endOfChapter = findEndChapter(processedData, index)
            print (processedData[index + 1 : endOfChapter - 1])
            chapter.addRawData(processedData[index + 1 : endOfChapter])
            latex.addChapter(chapter)
        index += 1
    return latex

def findEndChapter(data, index):
    for i in range(index, len(data)):
        if i+1 < len(data):
            if ((data[i][0] == "END") and (data[i+1][0] == "CHAPTER")):
                return i+1
        else :
            if(data[i][0] == "END"):
                return i+1

    print('Chapter END not found. Error in your file')
    return -1000
