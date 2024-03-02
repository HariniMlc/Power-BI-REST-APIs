# Import the requests library
import requests

# Replace with your access token, workspace ID, and dataset ID
access_token = "..."
groupId = "..."
datasetId = "..."

# Set the API endpoint
url = f"https://api.powerbi.com/v1.0/myorg/groups/{groupId}/datasets/{datasetId}/refreshes"

# Set the headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Set the body
body = {
    # Optionally, you can specify the notify option
    # Possible values are: NoNotification, MailOnCompletion, MailOnFailure
    # "notifyOption": "MailOnFailure"
}

# Send the POST request
response = requests.post(url, headers=headers, json=body)

# Check the status code
if response.status_code == 202:
    print("Refresh request accepted.")
elif response.status_code == 400:
    print("Refresh request invalid.")
elif response.status_code == 401:
    print("Access token invalid or expired.")
elif response.status_code == 403:
    print("Permission denied.")
elif response.status_code == 404:
    print("Dataset or workspace not found.")
elif response.status_code == 429:
    print("Refresh request throttled.")
elif response.status_code == 500:
    print("Internal server error.")
else:
    print("Unknown error.")
