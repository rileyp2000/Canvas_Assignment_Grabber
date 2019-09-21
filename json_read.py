import json
import requests

user_id = '45110000000126834'
acc_token = '4511~V35YjSpgz6zU1lSniHKUYjFvHNaE7h3koE8g9t6XUsXVTGv2ZGNoxn3FoRPxZTYC'

#Gets a list of all classes
#response = requests.get('https://canvas.instructure.com/api/v1/courses', params=access_token)
class_list = requests.get(f'https://canvas.instructure.com/api/v1/courses?access_token={acc_token}').json()

#Generic Command to get assignments from a class
#assignments_by_class = response = requests.get('https://canvas.instructure.com/api/v1/users/:user_id/courses/:course_id/assignments')

classes = {}

for distro in class_list:
    print(distro['name'])
    print(distro['id'])
    
    #Adds classes to list based on user input
    ch = input('Would you like to keep this class? (Y/N): ')

    if ch == 'Y' or ch == 'y':
        classes.update({distro['name']: distro['id']})

#For each class, get a list of assignments 
for course in classes:
    #Course is the key in the dict
    class_id = classes[course]
    assigns = requests.get(f'https://canvas.instructure.com/api/v1/users/{user_id}/courses/{class_id}/assignments?access_token={acc_token}').json()
    assignments = {}
    for a in assigns:
        print(a['name'])
        assign_id = a['id']
        assignment_details = requests.get(f'https://canvas.instructure.com/api/v1/users/{user_id}/courses/{class_id}/assignments/{assign_id}/submission_summary')
        