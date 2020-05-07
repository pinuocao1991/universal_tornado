from tornado.web import HTTPError

from config.base import route
from config.middleHandler import MiddleHandler


@route(['/view/','/'])
class Main(MiddleHandler):

    def get(self):
        # ss = 1/0
        print(self.keys)
        raise HTTPError(500, "Query argument cannot be empty string")

    def post(self,view):
        print('post:',view)


@route('/person')
class Person(MiddleHandler):
    def get(self):
        return "{'asd':1223}"