import requests
import json

url = 'https://console-00488.qradar.ibmcloud.com/api/reference_data/sets/'
headers = {"Accept": "application/json", "SEC": "582be4fe-9282-46a9-b12b-e95de0025a7a"}

with open("inputs.txt", "r") as file_1:
    for line in file_1:
        stripped_line = line.strip('\n')
        u = url + stripped_line
        response = requests.delete(u, headers=headers, verify=False)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=4))
