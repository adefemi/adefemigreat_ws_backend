import requests
import jwt
from datetime import datetime, timedelta
from random import SystemRandom
from rest_framework.pagination import PageNumberPagination
from .settings import SECRET_KEY
import string
from rest_framework.exceptions import APIException


class Helper:

    @staticmethod
    def normalizer_request(data):
        try:
            data._mutable = True
            result = data.dict()
        except:
            result = data

        return result

    @staticmethod
    def generate_random_number(length):
        return ''.join(str(SystemRandom().randrange(0, 10)) for i in range(length))

    @staticmethod
    def jwt_encode(data, expiry):
        expiry_date = datetime.utcnow() + timedelta(days=expiry)
        data.update({
            "expiry": str(expiry_date)
        })
        return jwt.encode(data, SECRET_KEY, algorithm='HS256').decode("utf-8")

    @staticmethod
    def jwt_decode(token):
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    @staticmethod
    def generate_random_string(length):
        return ''.join(SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))

    @staticmethod
    def reference_generator(random_string):
        return "rr_" + datetime.now().strftime("%m%d%y%H%M%S") + random_string

    @staticmethod
    def http_request(data, url, authorization=None, method="post"):
        headers = {}

        if method == "post":
            headers.update({
                'Content-Type': 'application/json',
            })

        if authorization:
            headers.update({
                'Authorization': 'Bearer {}'.format(authorization)
            })

        try:
            if method == "get":
                res = requests.get(url, headers=headers)
            elif method == "put":
                res = requests.put(url, data, headers=headers)
            else:
                res = requests.post(url, data, headers=headers)

        except requests.ConnectionError as e:
            raise APIException("failed operation", e)

        if res.status_code == 200:
            return res.json().get('data')
        else:
            raise APIException(res.json().get('message'))


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
