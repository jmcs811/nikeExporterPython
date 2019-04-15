
import requests
import json
from requests.exceptions import HTTPError

def main():
    print("Starting")
    token = "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc2YWI1NThkLWMwZTMtNGVhYi05MTljLTJkYjA3YjFjN2NhMHNpZyJ9.eyJ0cnVzdCI6MTAwLCJpYXQiOjE1NTUyODQyNDIsImV4cCI6MTU1NTI4Nzg0MiwiaXNzIjoib2F1dGgyYWNjIiwianRpIjoiMzMzNjc1NzItMzAzMS00Nzk5LWFkZjMtNTZkZTAyYTQ4OGI2IiwibGF0IjoxNTUxNTM4NzYzLCJhdWQiOiJjb20ubmlrZS5kaWdpdGFsIiwic3ViIjoiY29tLm5pa2UuY29tbWVyY2UubmlrZWRvdGNvbS53ZWIiLCJzYnQiOiJuaWtlOmFwcCIsInNjcCI6WyJuaWtlLmRpZ2l0YWwiXSwicHJuIjoiMTQ3NTg0NjY3MzEiLCJwcnQiOiJuaWtlOnBsdXMifQ.FuH1jGF67CEazztugnKHV1Olg1WUGZmwXa0kRUeH3QliKn2Igd5yMutHCjDW3GGu8VAJm6A9jpvxnjTcQeHnn7jHjU8BR2hjD_oZNDtDRFRMZhVnwgCn453rht4hdwZ4dYVm2CGXp8XW5TD4cGu0u6JZ24JmF6tmO7wu33e3BNajps8pDeQo-SUti0XQJ5b3oPk-M9qFvVSrHh_aWh6lybedfywDb0Pz4iCaXTvFyhdCQ-lRdNnzH-DVPFjYMNhlARtJqnBaKnScwW4bQ1MXzoUTklnJPosHQuLGBORXY6heoww2MgLKtSbQ_D4g46O7MgB8-JsgHL-jH0A4wUcT-A"
    jsonContent = getJson(token)
    parseJson(jsonContent)

def getToken():
    try:
        response = requests.get("https://www.nike.com/us/en_us/e/nike-plus-membership")
        response.raise_for_status
    except HTTPError as htpe:
        print(f'HTTP Error: {htpe}')
    except Exception as e:
        print(f'Other Exception: {e}')
    else:
        responseCode = response.status_code
    
    if (responseCode == 200):
        responseHeaders = response.headers
    
    print(responseHeaders)

def getJson(token):
    header = {
        'authorization': "Bearer " + token,
        'content-type': "application/json"
    }

    try:
        response = requests.get("https://api.nike.com/sport/v3/me/activities/after_time/0", headers=header)
        response.raise_for_status
    except HTTPError as htpe:
        print(f'HTTP Error: {htpe}')
    except Exception as e:
        print(f'Other Exception: {e}')
    
    jsonContent = response.json()
    return jsonContent

def parseJson(jsonContent):
    # convert dict to string for json.loads
    jasonData = json.loads(json.dumps(jsonContent))

    # if paging info is in json then more data 
    # can be pulled
    if "paging" in jasonData:
        print("more pages to go")


main()