from app import create_app


def make_client():
    return create_app({"TESTING": True}).test_client()


def test_home_page():
    response = make_client().get("/")

    assert response.status_code == 200


def test_home_page_content():
    response = make_client().get("/")

    assert b"Southern City Explorer" in response.data