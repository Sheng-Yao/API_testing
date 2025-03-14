# # GET information (Status, Timestamp)
# import requests
# import json

# url = 'https://wildtechalert-39e415aada0a.herokuapp.com/'
# url_type = 'health'
# final_url = url + url_type

# headers = {
#     'X-API-Key': '7f89940a-bdc5-47bc-9743-f4b2ba20f64e'
# }

# response = requests.get(final_url, headers=headers)

# print(response.text)
# print(json.loads(response.text)["status"])

# # POST information (Confidence Score, Device ID)
# import requests

# url = 'https://wildtechalert-39e415aada0a.herokuapp.com/'
# url_type = 'detect'
# final_url = url + url_type

# headers = {
#     'X-API-Key': '7f89940a-bdc5-47bc-9743-f4b2ba20f64e'
# }

# information = {
#     'confidence_score': 0.85,
#     'device_id': 753
# }

# response = requests.post(final_url, headers=headers, json=information)

# print(response.text)