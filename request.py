import requests
import json, pprint
import pathlib
# variable region


BASE_URL = "http://saral.navgurukul.org/api/courses"
coursesJsonData={}
exerciseJsonData = {}
def printText(text):
    print ("\n\n\t"+"*"*20+text+"*"*20+"\t\n\n")

printText("WELCOME TO SARAL")    

# calling API by get in function.
def getResp(api):
    getData = requests.get(api)                                                     
    coursesJsonData = getData.json()
    return coursesJsonData


# Write json_data in courses.json file. 
def writeData(data,fileName):
    with open(fileName, "w") as writeIt: 
	    writeIt.write(json.dumps(data))
    writeIt.close()


# Read the json_data from courses.json file.
def readData(fileName):
    with open(fileName, "r") as readIt: 
        readJson = json.load(readIt)
    return readJson

# Chacking the file exists or not.
def getData(fileName,url):
    file = pathlib.Path(fileName)
    if file.exists ():
        readJsonData = readData(fileName)
        coursesJsonData=readJsonData

    else:
        coursesJsonData=getResp(url)
        writeData(coursesJsonData,fileName)

    return coursesJsonData
coursesJsonData = getData("courses.json",BASE_URL)

# Using while loop for print courses Names.
def getCourses(jsonData):
    index = 0
    while index<len(jsonData["availableCourses"]):
        print  (str(index+1)+"."+jsonData["availableCourses"][index]["name"])
        index = index+1
getCourses(coursesJsonData)

printText("*"*10)

# I created a function to take userInput from the user.
userInput = input("Enter your course number :- ")
courseId = (coursesJsonData["availableCourses"][int(userInput)]["id"])
courseName=(coursesJsonData["availableCourses"][int(userInput)]["name"])
print (courseId)


