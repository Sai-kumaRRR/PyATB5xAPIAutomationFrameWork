# Pre-built methods for thr GET , POST , PATCH , PUT , DELETE , REQUESTS


import json
import requests



def get_request(url, auth , in_json):
    get_response = requests.get(url=url, auth=auth)
    if in_json:
        return get_response.json()
    return get_response

def post_request(url,auth, headers , payload, in_json):
    post_response = requests.post(url=url,headers=headers, auth=auth,data=json.dumps(payload))
    if in_json:
        return post_response.json()
    return post_response


def patch_request(url,headers, auth,payload , in_json):
    patch_response_data = requests.patch(url=url, headers=headers, auth=auth,data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def put_request(url,headers, auth, payload , in_json):
    put_response_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data


def delete_requests(url, headers , auth, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth  )
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data


