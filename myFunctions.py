import os
import xlsxwriter
import tkinter as tk
from tkinter import filedialog


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for file in listOfFile:
        fullPath = os.path.join(dirName, file)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def writeFiles(list1, list2):
    print("Where would you like to save the results?")
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')

    workbook = xlsxwriter.Workbook(export_file_path)
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(list1):
        worksheet.write(row_num, 0, data)

    for row_num, data in enumerate(list2):
        worksheet.write(row_num, 1, data)

    workbook.close()


def writeFiles(list1, list2, list3, list4, list5):
    print("Column1: Survey#'s needed from the PDF folder \n"
          "Column2: Survey#'s needed from the Excel reviewed folder\n"
          "Column3: Survey#'s needed from the Excel unreviewed folder\n"
          "Column4: Survey#'s needed from Max's folder\n"
          "Column5: Survey#'s still missing")
    print("Where would you like to save the results?")
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')

    workbook = xlsxwriter.Workbook(export_file_path)
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(list1):
        worksheet.write(row_num, 0, data)

    for row_num, data in enumerate(list2):
        worksheet.write(row_num, 1, data)

    for row_num, data in enumerate(list3):
        worksheet.write(row_num, 2, data)

    for row_num, data in enumerate(list4):
        worksheet.write(row_num, 3, data)

    for row_num, data in enumerate(list5):
        worksheet.write(row_num, 4, data)

    workbook.close()


def findLarger(first, second):
    if first > second:
        return first
    else:
        return second


def findFileNumber(s):
    stack = []
    i = 0
    for word in s:
        pos = 0
        length = len(word)
        while pos < length - 3:
            if (ord(word[pos]) > 47) and (ord(word[pos]) < 58):
                if (ord(word[pos+1]) > 47) and (ord(word[pos+1]) < 58):
                    if (ord(word[pos+2]) > 47) and (ord(word[pos+2]) < 58):
                        if (ord(word[pos+3]) > 47) and (ord(word[pos+3]) < 58):
                            if (pos+4 == length):
                                stack.append(word[pos] + word[pos + 1] + word[pos + 2] + word[pos + 3])
                                pos = len(word) - 3
                            elif (ord(word[pos+4]) > 47) and (ord(word[pos+4])) < 58:
                                pos += 5
                            else:
                                stack.append(word[pos] + word[pos + 1] + word[pos + 2] + word[pos + 3])
                                pos = len(word) - 3

                        else:
                            pos += 4

                    else:
                        pos += 3

                else:
                    pos += 2

            else:
                pos += 1

        i += 1

    return stack


def findCommonElements(list1, list2):
    return [value for value in list1 if value in list2]


def leftExclusive(list1, list2):
    return [item for item in list1 if not item in list2]


def getFileNames(folder):
    dirName = os.getcwd() + folder
    listOfFiles = getListOfFiles(dirName)

    # Remove everything before the last \
    i = 0
    for file in listOfFiles:
        temp = file.rfind("\\")
        listOfFiles[i] = file[temp + 1:]
        i += 1

    return listOfFiles