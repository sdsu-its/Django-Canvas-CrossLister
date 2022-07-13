## "https://sdsu.beta.instructure.com/"

import json
from datetime import date, datetime
from canvasapi import Canvas
import requests as req


def crossList(api,sisInput):


    currentYear = date.today().year
    springStartDate = datetime.strptime(str(currentYear) + "-01-01", '%Y-%m-%d').date()
    fallStartDate = datetime.strptime(str(currentYear) + "-08-01", '%Y-%m-%d').date()

    apiURL = "https://sdsu.beta.instructure.com/"

    apiKey = api

    canvas = Canvas(apiURL, apiKey)


    account = canvas.get_account(1)
    courses = account.get_courses()

    # Empty lists to store the course IDs and their SIS IDs for all courses
    courseIDs = []
    sisID = []

    sisIDsNoCourseCode = []
    tempCourseIDs = []

    # Empty list to store only the course IDs that are available of based on the input
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

    SISIDInput = sisInput.upper()


    def getTermFromSIS(sis_id):
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
                sis = c.split('-')
                sis = sis[1]
                id = i
                searchedIDFullForm.append(newDict)

                sisIDsNoCourseCode.append(sis)
                tempCourseIDs.append(id)
                searchedIDList.append(i)

    except:
        print("Error. Please try again later.")


    # Example naming convention - chem100-01-03_06-spring2022

    # Function to choose and parse specific courses.

    def parseIDSToCrossList(sis_id):
        l1 = []

        idsFromIteration = []


        temp = sis_id.split('-', 1)
        temp = str(temp[1]).lower()

        temp = temp.split('-cx-spring')
        temp = temp[0]
        temp = temp.split('_')

        for element in temp:

            if '-' in element:
                listOne = element
                listOne = listOne.split('-')
                listOne = [int(item) for item in listOne]

                i = listOne[0]
                while i <= listOne[1]:
                    l1.append(i)
                    i = i + 1

                for sis, id in zip(sisIDsNoCourseCode, tempCourseIDs):
                    for i in l1:
                        if str(i).zfill(2) in sis:
                            idsFromIteration.append(id)

            else:

                listTwo = element
                listTwo = [int(item) for item in listTwo]

                for sis, id in zip(sisIDsNoCourseCode, tempCourseIDs):
                    for i in listTwo:
                        if str(i).zfill(2) in sis:
                            idsFromIteration.append(id)




        return idsFromIteration





    def createShell(sis_id):
        # Function to create an empty shell
        shell = account.create_course()


        term = str(getTermFromSIS(sis_id)).lower()

        tempList = sis_id.split('-',1)
        course_code = tempList[0]
        tempStr = str(tempList[1]).lower()
        tempList2 = tempStr.split(term)

        section = str(tempList2[0])
        section = section.split('-cx-')
        section = section[0] + '-CX-'

        name = course_code + '-' + section +  term.title() + str(currentYear)
        shell.update(
            course={'course_code': course_code, 'name': name, 'term_id': 160,
                    'id': shell.id})
        return shell





    # Create a function for cross-listing.
    def crossList(sectionID, newCourseID):
        ## data = {'id':sectionID,'new_course_id':newCourseID}
        header = {'Authorization': f"Bearer {api}"}

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

    print(courseIDsToCrossList)

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
