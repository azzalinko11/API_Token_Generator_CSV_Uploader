#Aratcliffe @ PANW
import requests
import credentials_file

# Set the endpoint URL for token retrieval
token_url = "https://auth.apps.paloaltonetworks.com/oauth2/access_token"

# Set the client ID and secret from credentials_file.py

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
