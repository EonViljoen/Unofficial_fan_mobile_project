from flask import jsonify, request
import json


# Read JSON
with open('species.json', 'r') as myfile:
    information_file=myfile.read()

# Load JSON
species = json.loads(information_file) 

# Return item if id exists
def return_item_with_id(id):
    for item in species['list']:
        if item['id'] == id:
            return (item)


# print(species['list'][0]['name'])

# Return list of ids
def get_species_id_list():
    id_results = []

    for thing in species['list']:
        id_results.append(thing['id'])
        return (id_results)

def return_full_list():
    return species['list']

