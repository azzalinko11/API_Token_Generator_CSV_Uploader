#FQDN Bulk CSV Import azzalinko11
import requests
import csv
import credentials_file

#get the token First

# Set the endpoint URL for token retrieval
token_url = "https://auth.apps.paloaltonetworks.com/oauth2/access_token"

client_id = credentials_file.client_id
client_secret = credentials_file.client_secret

# Set the scope and grant type
scope = credentials_file.scope
grant_type = "client_credentials"

# Set the request payload
payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope,
    "grant_type": grant_type
}

# Set the headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Send the token retrieval request
response = requests.post(token_url, data=payload, headers=headers)

# Process the API response
if response.status_code == 200:
    # Extract the API token from the response
    api_token = response.json()["access_token"]
    print("API token obtained successfully:", api_token)
else:
    print("Failed to obtain API token. Status code:", response.status_code)
    print("Error message:", response.text)


# Prisma Access SASE API endpoint "Shred Location"
api_url = 'https://api.sase.paloaltonetworks.com/sse/config/v1/addresses?folder=Shared'

# API key or access token for authentication
api_key = api_token

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
            row['Type']: row['Value']
        }
        address_objects.append(address_object)

print(" "+ str(address_objects))

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
