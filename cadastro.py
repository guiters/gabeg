from locust import HttpLocust, TaskSet, task
from random import randrange, uniform, random
import string
import json
import sys

reload(sys)

sys.setdefaultencoding('utf8')


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


class UserBehavior(TaskSet):

    @task(200)
    def click_registrar(self):
        irand = str(randrange(10000000000000, 999999999999999999))
        post = {
            'form_name': 'register',
            'checkboxes[]': 'terms',
            'register[first_name]': 'Guilherme',
            'register[last_name]': 'The Hacker',
            'register[email]': "batata" + irand + "@assada.com",
            'register[country_code]': "+55",
            'register[area_code]': "11",
            'register[phone_number]': str(randrange(999111111, 999999999)),
            'register[country_abbreviation]': 'BR',
            'register[btc_knowledge]': '4',
            'register[terms]': 'Y',
            'register[default_currency]': '28',
            'register[ref]': '',
            'verify_fields[first_name]': "1",
            'verify_fields[last_name]': "1",
            'verify_fields[email]': "1",
            'verify_fields[btc_knowledge]': "1"

        }
        response = self.client.post("http://lbtest.atlastest.tk/register.php", post)
        print("Register - Response status code:", response.status_code)

    @task(300)
    def click_login(self):
        irand = str(randrange(10000000, 99999999))
        post = {
            'login[user]': irand,
            'login[pass]': "CadeasdCgasdas",
            'submitted': "1",
            'uniq': "e927253ff04b6ee79e306d053fd39f8e",
            'submit': "Login"
        }
        json_post = json.dumps(post)
        response = self.client.post("http://lbtest.atlastest.tk/login.php", json_post)
        print("Login - Response status code:", response.status_code)

    @task(100)
    def index(self):
        response = self.client.get("http://lbtest.atlastest.tk/")
        print("Home - Response status code:", response.status_code)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
