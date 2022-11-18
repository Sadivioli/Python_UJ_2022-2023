
import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
	data = json.load(read_file)

trams = {}
stops = {}

for linia in data['linia']:
    trams[linia['name']] = []
    if 'przystanek' in linia:
        for przystanek in linia['przystanek']:
            #[-3] ucina 3 ostatnie znaki z nazwy przystanku czyli numer i spacje
            trams[linia['name']].append(przystanek['name'][:-3])

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(trams, file, ensure_ascii=False)