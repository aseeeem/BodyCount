import csv
import json

with open('txt.csv', 'r') as csvf:
    csv_read = csv.reader(csvf)
    csv_data = list(csv_read)
final_data = []
for row in csv_data:
    final_data.append({'count':row[0],'time':row[1]})

with open('data.txt', 'w') as jsonOut:
    json.dump(final_data, jsonOut, indent=2)
