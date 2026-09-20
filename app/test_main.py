from main import app

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Desigapperumal" in response.data
    print("Professional Unit Test Passed Successfully!")
