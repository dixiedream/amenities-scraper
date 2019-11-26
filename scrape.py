import anyconfig
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

try:
    whatToScrape = anyconfig.load("./config/whatToScrape.yml")
except FileNotFoundError as e:
    whatToScrape = anyconfig.load("./config/whatToScrape.example.yml")

api = overpass.API()
for data in whatToScrape:
    area = data['area']
    amenities = data['amenities']
    filename = data['filename']
    query = f'area[name="{area}"]->.searchArea; '
    for amenity in amenities:
        query = query + f'(node["amenity"="{amenity}"](area.searchArea);); '

    response = api.Get(query, responseformat="json")
    with open(f'./data/{filename}.json', 'w') as f:
        f.write(json.dumps(response['elements'], indent=2))

    with open(f"./data/named{filename.title()}.json", 'w') as f:
        f.write(json.dumps(createJSON(response['elements']), indent=2))