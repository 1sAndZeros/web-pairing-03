def test_get_users(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "john, jane, alice"


def test_get_user_no_user_found(web_client):
    response = web_client.get("/users/4")
    assert response.status_code == 404
    assert response.data.decode("utf-8") == "Error: User not found"


def test_get_user_valid_id(web_client):
    response = web_client.get("/users/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "john"


def test_create_user(web_client):
    response = web_client.post("/users", data={"username": "test name"})
    assert response.status_code == 201
    assert response.data.decode("utf-8") == "User test name created with id 4"

    get_response = web_client.get("/users")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "john, jane, alice, test name"


def test_create_user_no_username_given(web_client):
    response = web_client.post("/users")
    assert response.status_code == 400
    assert response.data.decode("utf-8") == "Error: Username is required"


def test_updates_user_correctly(web_client):
    pass
