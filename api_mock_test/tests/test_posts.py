from utils.api_client import APICLIENT

client = APICLIENT() #object

def test_get_posts_status_code(): # function to get all posts
    response = client.get("/posts")
    assert response.status_code == 200


def test_get_single_post(): # funcion to get only one post based on id
    response = client.get("/posts/1")
    assert response.status_code == 200
    json = response.json()
    assert json["id"] == 1
    assert "title" in json

def test_create_post(): # function to create a new post
    payload = {
        "title": "foo",
        "body" : "bar",
        "useId" : "1"
    }

    response = client.post("/posts", data=payload)
    assert response.status_code == 201
    json = response.json()
    assert json["title"] == payload["title"]