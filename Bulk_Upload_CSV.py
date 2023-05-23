#FQDN Bulk CSV Import Aaron Ratcliffe
import requests
import csv

# Prisma Access SASE API endpoint "Shred Location"
api_url = 'https://api.sase.paloaltonetworks.com/sse/config/v1/addresses?folder=Shared'

# API key or access token for authentication
api_key = ''
# Path to the CSV file containing the object list
csv_file = 'testupload.csv'

# Read the address objects from the CSV file
address_objects = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        address_object = {
            'name': row['Name'],
            'description': row['Desc'],
            #change to ip-mask etc depending on value
            'fqdn': row['Value']
        }
        address_objects.append(address_object)

# Send the POST request to add the address objects
success_count = 0
failure_count = 0
for obj in address_objects:
    response = requests.post(api_url, headers={'Authorization': f'Bearer {api_key}'}, json=obj)
    if response.status_code == 201:
        success_count += 1
    else:
        failure_count += 1
        print(f'Failed to add address object: {obj["name"]}, Error: {response.text}')

print(f'Successfully added {success_count} address objects.')
print(f'Failed to add {failure_count} address objects.')
