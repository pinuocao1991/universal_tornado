from tornado.web import HTTPError

from config.base import route
from config.middleHandler import MiddleHandler


@route('/')
class Main(MiddleHandler):
    def get(self, **kwargs):
        ss = self.get_argument("id")
        raise HTTPError(500, "Query argument cannot be empty string")

@route('/person')
class Person(MiddleHandler):
    def get(self, name):
        self.write(name)