import overpass
import json

def createJSON(elements):
    toReturn = []
    for element in elements:
        if 'name' in element['tags']:
            toReturn.append({
                'name': element['tags']['name'],
                'lat': element['lat'],
                'lon': element['lon']
            })
    return toReturn

api = overpass.API()
query = 'area(3600042602)->.searchArea; (node["amenity"="school"](area.searchArea););'
response = api.Get(query, responseformat="json")

with open('./data/schools.json', 'w') as f:
    f.write(json.dumps(response['elements'], indent=2))

with open('./data/namedSchools.json', 'w') as f:
    f.write(json.dumps(createJSON(response['elements']), indent=2))