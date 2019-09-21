import json
import requests

user_id = '45110000000126834'
acc_token = '4511~V35YjSpgz6zU1lSniHKUYjFvHNaE7h3koE8g9t6XUsXVTGv2ZGNoxn3FoRPxZTYC'

def pull_classes():
        #Gets a list of all classes
        #response = requests.get('https://canvas.instructure.com/api/v1/courses', params=access_token)
        class_list = requests.get(f'https://canvas.instructure.com/api/v1/courses?access_token={acc_token}').json()
        
        with open('classes.json', 'w+') as f:
                json.dump(class_list, f)

def get_classes():
        with open('classes.json', 'r') as f:
                classes_all = json.load(f)

        classes = {}

        for distro in classes_all:
                print(distro['name'])
                print(distro['id'])
        
                #Adds classes to list based on user input
                ch = input('Would you like to keep this class? (Y/N): ')

                if ch == 'Y' or ch == 'y':
                        classes.update({distro['name']: distro['id']})
        return classes

def pull_assignments(name, class_id):
    assigns = requests.get(f'https://canvas.instructure.com/api/v1/users/{user_id}/courses/{class_id}/assignments?access_token={acc_token}').json()
    assignments = {}
    for a in assigns:
        assign_name = a['name']
        due_date = a['due_at']
        assign_id = a['id']
        assign_pts_pos = a['points_possible']
        assignment_details = (assign_name, due_date, assign_id, assign_pts_pos)
        #TODO: Instead of tuple convert to pandas dataframe and then export to a csv with the class name
        print(assignment_details)


#pull_classes()
classes = get_classes()
for c in classes:
        pull_assignments(c, classes[c])    