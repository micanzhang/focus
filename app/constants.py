import json

__author__ = 'micanzhang'

DB_HOST = 'localhost'
DB_NAME = 'focus'
DB_USERNAME = 'focus'
DB_PASSWORD = 'focus'

class Roles:
    GUEST = 0
    AUTHROIZED = 1
    ADMIN = 100


class ResponseStatus:
    STATUS_OK = 0
    STATUS_INCORRECT_PARAMS = 1
    STATUS_NOT_FOUND = 2
    STATUS_AUTH_FAILED = 3
    STATUS_REPEAT_REQUEST = 4
    STATUS_SERV_INTERVAL_ERR = 5
    STATUS_BAD_REQUEST = 6

class Response:
    def __init__(self, error=ResponseStatus.STATUS_OK, msg='ok', data={}):
        self.error = error
        self.msg = msg
        self.data =data

    def json(self):
        response_d = {'error':self.error, 'msg':self.msg, 'data':self.data}
        return json.dumps(response_d)
