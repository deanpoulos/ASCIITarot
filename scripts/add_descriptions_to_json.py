from fuzzywuzzy import fuzz
import json

l = json.load(open('../assets/cards-original.json', 'r'))

def extract_text(name: str): 
    description = ""
    with open('../assets/major_arcana_descriptions.txt', 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            ratio = fuzz.ratio(name,line) 
            if ratio > 70:
                description = lines[i+2]
                break

    return description


for i, entry in enumerate(l):
    name = entry['name']
    if 'Reversed' in name:
        name.replace(' Reversed', '')

    description = extract_text(name)
    if description: l[i]['description'] = description

with open('../assets/cards.json', 'w+') as f:
    json.dump(l,f)
