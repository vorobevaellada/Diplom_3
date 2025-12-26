import string
import random
from random import randint
import pytest
import requests
from data import *
from selenium import webdriver

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    if request.param == "chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--window-size=1920,1080")     # фиксированный размер окна
        browser = webdriver.Chrome(options=opts)
    elif request.param == "firefox":
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--window-size=1920,1080")
        browser = webdriver.Firefox(options=opts)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        txt = ''.join(random.choice(letters) for i in range(length))
        return txt

    email = str(randint(10000, 99999)) + "@gmail.com"
    password = str(randint(1000000, 9999999))
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload

@pytest.fixture(scope='session')
def registration(payload):
    response = requests.post(Urls.CREATE_USER, data=payload)
    assert response.status_code == 200
    return {
        'email': payload['email'],
        'password': payload['password'],
        'name': payload['name'],
        'accessToken': response.json().get('accessToken')
    }

@pytest.fixture(scope='session')
def get_token(registration):
    return registration['accessToken']

@pytest.fixture(scope='session', autouse=True)
def delete_user(get_token):
    headers = {'Authorization': f'{get_token}'}
    yield
    response = requests.delete(Urls.AUTH_USER, headers=headers)
    assert response.status_code == 202