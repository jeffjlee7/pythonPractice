import os

# Download the "Romeo and Juliet" file
'''
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
txt = open('RomeoAndJuliet.txt')
print(txt)
'''

# Open the text file
myFiles = 'RomeoAndJuliet.txt'
osPath = 'C:\\Users\\Jeff\\'
file = "%s%s" % (osPath, myFiles)
RJ = open(file)
txt = RJ.read()
# print(txt)

# count() will ask for a string. count() will locate the string's first instance
# in the file and count the number of times the string appears.

def count():
    txtLen = len(txt)
    print('Text length: ', txtLen)
    selection = (txt)
    # you can change the selection to look for your string in specific
    # areas of the file
    print('Selection length: ', len(selection))
    # print(selection)

    string = input("What text would you like to ask for? ")

    print('Looking for <string>, <string length>:', string, len(string))

    count = 0

    for i in range(len(selection)):

        if selection[i:i + len(string)].lower() == string.lower():
            print('"',string,'"', 'is located at ', i, '/', len(selection))
            count += 1


    print('"', string,'"', "appears this many times:", count)
count()