import requests
import random
import json,string,uuid

base_url="https://gorest.co.in"
auth_token="Bearer {enter your token}"
##Random email generator
def genarate_random_email():
    domain="testing.com"
    email_length=10
    random_string=''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email=random_string+'@'+domain
    return random_string,email
def random_data():
    name,email=genarate_random_email()
    return{"name":name,
        "email":email ,
        "gender": "female",
        "status": "active"
    }
def test_get_request():
    url=base_url+"/public/v2/users"
    headers={"Authorization":auth_token}
    response= requests.get(url,headers=headers)
    assert response.status_code==200
    json_data=response.json()
    data=json.dumps(json_data,indent=4)
    print(" json response body",data)
   
def test_post_request():
    url=base_url+"/public/v2/users"
    headers={"Authorization":auth_token}
    data=random_data()
    response=requests.post(url, json=data, headers=headers)
    assert response.status_code==201
    json_data=response.json()
    data=json.dumps(json_data,indent=4)
    print(" json post response body",data)
    user_id=json_data["id"]
    #assert "name" in json_data
    #assert json_data["name"]== "Gopi testing"
    return user_id

def test_put_request():
    user_id=test_post_request()
    url=base_url+f"/public/v2/users/{user_id}"
    headers={"Authorization":auth_token}
    data=random_data()
    response=requests.put(url,json=data,headers=headers)
    assert response.status_code==200
    json_data=response.json()
    data=json.dumps(json_data,indent=4)
    print(" json put response body",data)
    print("updated user id {}".format(user_id))
    return user_id

def test_delete_request():
    user_id=test_put_request()
    url=base_url+f"/public/v2/users/{user_id}"
    headers={"Authorization":auth_token}
    response=requests.delete(url,headers=headers)
    assert response.status_code==204
    print(" .....delete user is done........{}".format(user_id))

#test_get_request()
#user_id=test_post_request()
#test_put_request(user_id)
#test_delete_request(user_id)
