import json
from clustering import cluster

# Lines 5 and 6 is where I open my open my cities.Json file and I store it in the variable 'cities'.
with open('data\cities.json') as file:
    cities = json.load(file)

# Lines 9 and 10 is where I open my open my libraries.Json file and I store it in the variable 'cities'.
with open('data\libraries.json') as file:
    libraries = json.load(file)

# Line 13 creates a list with all my city names in it.
list_cities = [x['name'] for x in cities]

# Line 18 asserts the variable 'dictionary' with a nested dictionary that contains the values for the populations
# and books for a given city.
   
dictionary = {x: {'population':0, 'books':0} for x in list_cities}

# I use the series of for loops to take the information I need from the files and store it in the dictionary.
for city in list_cities:
    for i in cities:
        if i['name'] == city:
            dictionary[city]['population'] = i['population']
    for j in libraries:
        if j['city'] == city:
            dictionary[city]['books'] += j['books']


with open('data/combined.json', 'w') as file:
    json.dump(dictionary, file)

# run the cluster function
datapoints = [(x['population'], x['books']) for x in dictionary.values()]