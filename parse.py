import json
import csv

with open('session.json', 'r') as f:
    data = json.load(f)
sum = 0
speakers = 0 
products = []
with open('out.csv', 'w') as file:
    csv_file = csv.writer(file)
    for p in data['data']:
        fields = ['title', 'description']
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        products = [w.replace('\t', ' ') for w in p['products']]
        igniteURL = 'https://myignite.techcommunity.microsoft.com/sessions/' + p['sessionId']
        writer.writerow([p['title'], p['downloadVideoLink'], ', '.join(products), igniteURL, p['format'], p['slideDeck']])
        # print(p['durationInMinutes'])
        # print(len(p['speakerIds']))
        speakers = speakers + len(p['speakerIds'])
        sum = sum + p['durationInMinutes'] 

print(sum)
print(speakers)
