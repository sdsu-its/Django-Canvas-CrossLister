## "https://sdsu.beta.instructure.com/"

import json
from datetime import date, datetime
from canvasapi import Canvas
import requests as req

currentYear = date.today().year
springStartDate = datetime.strptime(str(currentYear) + "-01-01", '%Y-%m-%d').date()
fallStartDate = datetime.strptime(str(currentYear) + "-08-01", '%Y-%m-%d').date()

apiURL = "https://sdsu.beta.instructure.com/"

apiKey = "10082~v9Bn1tTNSBncX4DX3JYb45yO8yfJejghWDnXGSBuGUb1t8NUKXQGQjOVChRaxpAf"
canvas = Canvas(apiURL, apiKey)




account = canvas.get_account(1)
courses = account.get_courses()

# Empty lists to store the course IDs and their SIS IDs for all courses
courseIDs = []
sisID = []

tempSISIDs = []
tempCourseIDs = []

# Empty list to store only the course IDs of based on the input
searchedIDList = []
searchedIDFullForm = []

# List of course codes that the user likes to crosslist
courseIDsToCrossList = []

# Open the JSON file an d parse all the SIS IDs and the Course IDs into the designated empty list

with open('data.json', 'r') as f:
    courseDict = json.load(f)
    for i in courseDict:
        sis = i['SIS ID']
        courseID = i['ID']
        sisID.append(sis)
        courseIDs.append(courseID)

SISIDInput = input("Enter a SIS ID for your new shell: ").upper()





def getTerm(sis_id):
    temp = sis_id.split('-')
    term = temp[-1]
    term = term.split('2')
    term = term[0]
    return term





def stripSISID(s):
    s = s.split('-')
    return s[0]


crs = stripSISID(SISIDInput)




# Sections to cross-list


'''



def parseSections(sis_id):
    temp = sis_id.split('-', 1)
    temp = str(temp[1]).lower()
    temp = temp.split(Term)

    section = str(tempList2[0])



for targetID in searchedIDList:

    if targetID
'''
try:
    print("List of Sections: ")
    temp1 = []
    temp2 = []
    for c, i in zip(sisID, courseIDs):
        if c.startswith(crs):
            if c.endswith('Spring' + str(currentYear)):
                temp1.append(c)
                temp2.append(i)

    if len(temp1) == 0:
        print("No Sections Available.")
    else:
        for c, i in zip(temp1, temp2):
            print('SIS ID: ', c, '', 'Course ID: ', i)
            newDict = {'SIS ID': c, 'Course ID':str(i)}
            sis = c
            id = i
            searchedIDFullForm.append(newDict)
            tempSISIDs.append(sis)
            tempCourseIDs.append(id)
            searchedIDList.append(i)

except:
    print("Error. Please try again later.")


# Example naming convention - chem100-01-03_06-spring2022


def parseIDSToCrossList(sis_id):


    if "cx" not in sis_id:
        # Storing counters for first iterations only
        l1 = []

        idsFromFirstIteration = []
        idsFromSecondIteration = []

        temp = sis_id.split('-', 1)
        temp = str(temp[1]).lower()

        temp = temp.split('-spring')
        temp = temp[0]
        temp = temp.split('_')

        listOne = temp[0]
        listOne = listOne.split('-')
        listOne = [int(item) for item in listOne]

        i = listOne[0]
        while i <= listOne[1]:
            l1.append(i)
            i = i + 1

        for sis, id in zip(tempSISIDs, tempCourseIDs):
            for i in l1:
                if str(i).zfill(2) in sis:
                    idsFromFirstIteration.append(id)

        listTwo = temp[1:]
        listTwo = [int(item) for item in listTwo]

        for sis, id in zip(tempSISIDs, tempCourseIDs):
            for i in listTwo:
                if str(i).zfill(2) in sis:
                    idsFromSecondIteration.append(id)

        mainList = idsFromFirstIteration + idsFromSecondIteration

        print(idsFromFirstIteration)
        print(idsFromSecondIteration)

        return mainList
    
    else:
        mainList = []
        mainList = searchedIDList + mainList
        return mainList


def createShell(sis_id):
    # Function to create an empty shell
    shell = account.create_course()


    term = str(getTerm(sis_id)).lower()

    tempList = sis_id.split('-',1)
    course_code = tempList[0]
    tempStr = str(tempList[1]).lower()
    tempList2 = tempStr.split(term)

    section = str(tempList2[0])
    name = course_code + '-' + section +  term.title() + str(currentYear)
    shell.update(
        course={'course_code': course_code, 'name': name, 'term_id': 160,
                'id': shell.id})
    return shell





# Create a function for cross-listing.
def crossList(sectionID, newCourseID):
    ## data = {'id':sectionID,'new_course_id':newCourseID}
    header = {'Authorization': "Bearer 10082~v9Bn1tTNSBncX4DX3JYb45yO8yfJejghWDnXGSBuGUb1t8NUKXQGQjOVChRaxpAf"}

    url = "https://sdsu.beta.instructure.com:443/api/v1/sections/{}/crosslist/{}".format(sectionID, newCourseID)
    resp = req.post(url, headers=header)
    return resp.status_code


# Create new Shell


try:
    print("Creating new shell.")
    newShell = createShell(SISIDInput)
    print("Shell Created:", newShell.name)
    print()
except:
    print("Error. Cannot create a shell.")
    print()


# Function to create a new section

def createSection(courseID):
    try:
        theCourse = canvas.get_course(courseID)
        sections = theCourse.create_course_section()
        print(sections)
        return None


    except:
        return "Error. Cannot create a new section for the shell."


# Extract section IDs from the courses. If section ID is not available, then ignore that course.





courseIDsToCrossList = parseIDSToCrossList(SISIDInput)

for x in courseIDsToCrossList:
    for y in canvas.get_course(x).get_sections():
        if y.id is not None:
            newCrossListedSection = crossList(y.id, newShell.id)
            print(newCrossListedSection)
            print("Course ID: ", canvas.get_course(x))
            print("Section ID: ", y.id)
        else:
            print("No section ID found for: ", x)



print(newShell.id)



