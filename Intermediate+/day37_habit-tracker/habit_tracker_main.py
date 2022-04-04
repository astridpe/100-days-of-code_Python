import requests
import datetime as dt

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"
TODAY = dt.datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_update_endpoint = f"{pixel_creation_endpoint}/{TODAY}"
pixel_delete_endpoint = f"{pixel_creation_endpoint}/{TODAY}"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 1. Create a user account on Pixela:
# response = requests.post(pixela_endpoint, json=user_parameters)
# print(response.text)


# 2. Create a graph definition:
graph_config = {
    "id": GRAPH_ID,
    "name": "Sleeping Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)

# 3. Posting a pixel:
pixel_config = {
    "date": TODAY,
    "quantity": input("How many hours of sleep did you get tonight? ")
}

response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_config)
print(response.text)

# 4. update a pixel:
pixel_update = {
    "quantity": "6.51"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
# print(response.text)

# 5. deleting a pixel:
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
