import pandas as pd
import tkinter as tk
import xlsxwriter
import os
import myFunctions
from pandas import read_csv
from tkinter import filedialog

filterList = []
badNumbers = []
Original = "CS_Survey_Number"
New = "Missing_Survey_Numbers"
i = 0

# *******************************************************************
# ***ENTER FILE NAME⋁⋁⋁⋁⋁⋁⋁⋁ MAKE SURE TO INCLUDE EXTENSION*******
# *******************************************************************
df = pd.read_csv('FinalTest.csv', index_col=None)
initialCol = df['CS Survey Number'].to_list()
inputFilenames = df['File Name'].to_list()

# Sort
initialCol.sort()

# Grab the survey #
numberList = initialCol
numberList = myFunctions.findFileNumber(numberList)
numberList.sort()

# Convert the strings to int
for x in range(0, len(numberList)):
    numberList[x] = int(numberList[x])

# Create list of bad Numbers
for x in range(numberList[0], numberList[-1] + 1):
    if x not in numberList:
        badNumbers.append(x)

# Convert the list to string
for x in range(0, len(badNumbers)):
    badNumbers[x] = str(badNumbers[x])

# Make them all same length
n = 0
for element in badNumbers:
    if len(element) == 2:
        badNumbers[n] = "00" + element
    n += 1

n = 0
for element in badNumbers:
    if len(element) == 3:
        badNumbers[n] = "0" + element
    n += 1

# find max length
maxLength = myFunctions.findLarger(len(numberList), len(badNumbers))

# Check if the user wants to continue
# If not save and quit
ans = input("Would you like to compare missing to files in a folder? (y/n)")
if ans == ('n' or 'N' or "No" or "no" or "NO"):
    myFunctions.writeFiles(numberList, badNumbers)
    exit()

# Create list of all files in files folder
# *******************************************************************
# ENTER Folder NAME⋁⋁⋁⋁⋁⋁⋁⋁ **************************************
# *******************************************************************
ExcelFolder = "/FilesExcel"
pdfFolder = "/filesPDF"
unreviewedFolder = "/unreviewedFiles"
maxFolder = "/Air Samples for Alex"

# Get the file names from the correct folder
excelListofFiles = myFunctions.getFileNames(ExcelFolder)
pdfListofFiles = myFunctions.getFileNames(pdfFolder)
unreviewedFiles = myFunctions.getFileNames(unreviewedFolder)
maxsFiles = myFunctions.getFileNames(maxFolder)

# Find the Survey#'s from the file names
excelFileNumbers = myFunctions.findFileNumber(excelListofFiles)
pdfFileNumbers = myFunctions.findFileNumber(pdfListofFiles)
unreviewedNumbers = myFunctions.findFileNumber(unreviewedFiles)
maxsFileNumbers = myFunctions.findFileNumber(maxsFiles)

# Sort the lists
excelFileNumbers.sort()
pdfFileNumbers.sort()
unreviewedNumbers.sort()
maxsFileNumbers.sort()
inputFilenames.sort()


# Start with the pdf files
toUploadPDF = myFunctions.findCommonElements(badNumbers, pdfFileNumbers)
stillNeed = myFunctions.leftExclusive(badNumbers, pdfFileNumbers)

# Second is excel
toUploadExcel = myFunctions.findCommonElements(stillNeed, excelFileNumbers)
stillNeed = myFunctions.leftExclusive(stillNeed, excelFileNumbers)

# Third is the unreviewed
toUploadUnreviewed = myFunctions.findCommonElements(stillNeed, unreviewedNumbers)
stillNeed = myFunctions.leftExclusive(stillNeed, unreviewedNumbers)

# Fourth is Maxs files
toUploadMax = myFunctions.findCommonElements(stillNeed, maxsFileNumbers)
stillNeed = myFunctions.leftExclusive(stillNeed, maxsFileNumbers)

# Then print
myFunctions.writeFiles(toUploadPDF, toUploadExcel, toUploadUnreviewed, toUploadMax, stillNeed)
