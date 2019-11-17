import requests
import jwt
from datetime import datetime, timedelta
from random import SystemRandom
import math
from .settings import GOOGLE_GEOCODING_API, GOOGLE_API_KEY, SECRET_KEY
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
    def distance_between_lat_lon_in_km(lat1, lon1, lat2, lon2):
        p = 0.017453292519943295  # math.pi / 180

        c = math.cos  # shorten definition for math.cos

        a = 0.5 - c((lat2 - lat1) * p) / 2 + c(lat1 * p) * c(lat2 * p) * (1 - c((lon2 - lon1) * p)) / 2

        result = 12742 * math.asin(math.sqrt(a))  # 12742 = 2 * 6371km, earth radius

        return result

    @staticmethod
    def reference_generator(random_string):
        return "rr_" + datetime.now().strftime("%m%d%y%H%M%S") + random_string

    @staticmethod
    def resolve_address(full_address):
        url = GOOGLE_GEOCODING_API + '?address={}&key={}'.format(
            str(full_address).replace(" ", "").lower(), GOOGLE_API_KEY)
        r = requests.get(url)
        data = r.json()

        if r.status_code == 200:
            try:
                return {
                    "resolved_address": data['results'][0]["formatted_address"],
                    "latitude": data['results'][0]['geometry']['location']['lat'],
                    "longitude": data['results'][0]['geometry']['location']['lng'],
                }
            except Exception:
                raise APIException("Location / address cannot be resolved")
        else:
            raise APIException("Location / address cannot be resolved")

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
