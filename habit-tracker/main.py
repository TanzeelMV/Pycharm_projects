import requests
import datetime as dt

USERNAME = "whatsnext"
TOKEN = "widw85645cwc456cwaf47"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Sample graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# today = dt.datetime.now()
yesterday = dt.datetime(year=2024, month=6, day=9)
date = yesterday.strftime("%Y%m%d")

post_pixel_endpoint = f"{graph_endpoint}/{graph_config["id"]}"

pixel_params = {
    "date": date,
    "quantity": "20.85",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{post_pixel_endpoint}/{date}"
update_pixel_params = {
    "quantity": "4",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_endpoint = f"{post_pixel_endpoint}/{dt.datetime.now().strftime("%Y%m%d")}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

