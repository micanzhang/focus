__author__ = 'micanzhang'

import web

database = 'focus'
username = ''
password = ''


class Model:
    db = None
    tablename = ''

    def __init__(self):
        db = web.database(dbn='mysql', db=database, user=username, pw=password)

    def query(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass