import requests
from http import HTTPStatus

base_url = "https://reqres.in"

endpoint_get_user_list = "/api/users?page=2"
endpoint_get_user = "/api/users/{}"
endpoint_post_create_user = "/api/users"
endpoint_put_update_user = "/api/users/{}"
endpoint_delete_user = "/api/users/{}"

post_payload = {
                    "name": "LILY",
                    "job": "ARTIST"
                }

put_payload = {
                    "name": "LILY",
                    "job": "CREATOR"
              }

user_id = None

def get_all_data():
    response = requests.get(url = base_url + endpoint_get_user_list)
    if response.status_code == HTTPStatus.OK:
        json_response = response.json()
        print("GET api call's output\n", json_response)

def post_data():
    global user_id
    response = requests.post(url = base_url + endpoint_post_create_user, data = post_payload)
    if response.status_code == HTTPStatus.CREATED:
        json_response = response.json()
        print("POST api call's output\n", json_response)
        user_id = json_response.get('id')
        get_data_by_id()

def put_data():
    if user_id is not None:
        response = requests.put(url = base_url + endpoint_put_update_user.format(user_id), data = put_payload)
        if response.status_code == HTTPStatus.OK:
            json_response = response.json()
            print("PUT api call's output\n", json_response)
            get_data_by_id()

def get_data_by_id():
    if user_id is not None:
        # print("ARE WE HERE")
        # print(user_id)
        response = requests.get(url = base_url + endpoint_get_user.format(user_id))
        # print(response.text)
        if response.status_code == HTTPStatus.OK:
            json_response = response.json()
            print("GET api call's output for specific user\n", json_response)

def delete_user():
    if user_id is not None:
        response = requests.delete(url = base_url + endpoint_delete_user.format(user_id))
        if response.status_code == HTTPStatus.NO_CONTENT:
            print("User with id {} is deleted".format(user_id))
            get_data_by_id()

get_all_data()
post_data()
put_data()
delete_user()
