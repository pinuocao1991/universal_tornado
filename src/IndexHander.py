from tornado.web import HTTPError

from config.base import route
from config.middleHandler import MiddleHandler


@route(['/(.*)','/'])
class Main(MiddleHandler):

    def get(self,view):
        print('get',view)
        print(self.keys)
        raise HTTPError(500, "Query argument cannot be empty string")

    def post(self,view):
        print('post:',view)


@route('/person')
class Person(MiddleHandler):
    def get(self, name):
        self.write(name)