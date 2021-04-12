import sys
import re
import time
import codecs
from argparse import ArgumentParser
from openpyxl import Workbook


desc = """ 
    Strip-logcat parses logcat debugging log of Android system.
"""

# Declare global variables
ofd = None
workbook = None
worksheet = None
outputFileName = None
pattern = '^\d{2}-\d{2}'
separater = "|"

def initArgument():
    parser = ArgumentParser(description=desc)
    parser.add_argument('logcat', type=str, metavar='logcat', help='Logcat file to parse')
    parser.add_argument('-o', dest='output', type=str, metavar='output', help='Output file name')
    parser.add_argument('-f', dest='format', type=str, default='excel', choices=['excel', 'text'], help='Ouput file format')
    return parser.parse_args();

def removeDoubleSpace(str):
    str = str.replace('  ',' ')
    str = str.replace('  ',' ')
    str = str.replace('  ',' ')
    str = str.replace('  ',' ')
    return str;
    
# Define interface for text file.
def openText(path, mode):
    global ofd, outputFileName
    if mode!='r' and mode!='w' :
        print("invalid mode selection")
        return;
    outputFileName = "%s.txt" % path
    ofd = codecs.open(outputFileName, mode, 'utf-8')
    return;
    
def readLineText():
    global ofd
    if ofd is None :
        return None;
    return ofd.readline();

def writeText(string):
    global ofd
    if ofd is not None :
        line = removeDoubleSpace(string)
        array = line.split(' ')
        if re.search(pattern, line) is not None :
            wholeLog = ' '.join(array[5:])
            logArray = wholeLog.split(':')
            log = ':'.join(logArray[1:])
            ofd.write("%s%s%s" %(logArray[0], separater, log))
        else :
            ofd.write("Exception: %s%s" %(separater, string))
    return;

def closeText():
    global ofd
    if ofd is not None :
        ofd.close();
    return;

# Define interface for excel format.
def openXl(path, mode) :
    # In this case, var mode isn't used.
    global workbook, worksheet, outputFileName
    workbook = Workbook()
    worksheet = workbook.active
    outputFileName = "%s.xlsx" % path
    return;
    
def readXl() :
    # Do nothing, this function is not needed.
    return;

def writeXl(string) :
    global worksheet
    line = removeDoubleSpace(string)
    array = line.split(' ')
    
    if re.search(pattern, line) is not None :
        wholeLog = ' '.join(array[5:])
        logArray = wholeLog.split(':')
        log = ':'.join(logArray[1:])
        worksheet.append([array[0], array[1], array[2], array[3], array[4], logArray[0], log])
    else :
        worksheet.append(['', '', '', '', '', '', line])
    return;

def closeXl() :
    global workbook, outputFileName
    workbook.save("./"+outputFileName)
    return;


# Define handler index 
open, read, write, close = range(4)

# Define file output handler tuples
hioText     = (openText,    readLineText,   writeText,      closeText)
hioExcel    = (openXl,      readXl,         writeXl,        closeXl)


if __name__ != '__main__' :
    sys.exit()

print("strip-logcat by ted")

args = initArgument()

# Set parameters 
input = args.logcat
if args.output is None :
    output = args.logcat+".out"
else :
    output = args.output

if args.format is 'excel' :
    hio = hioExcel
else :
    hio = hioText

# Input file format must be text.
ifd = codecs.open(input, 'r', 'utf-8')
hio[open](output, 'w')

while True:
    line = ifd.readline()
    if not line:
        break
    if len(line.strip())==0 :
        continue
    hio[write](line)

ifd.close()
hio[close]()

print("...finish")
