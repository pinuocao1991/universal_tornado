from tornado.web import HTTPError

from config.base import route, catch_exception
from config.middleHandler import MiddleHandler


@route(['/'])
class Main(MiddleHandler):

    @catch_exception
    def get(self):
        # ss = 1/0
        print(self.keys)
        raise HTTPError(500, "Query argument cannot be empty string")

    def post(self,view):
        print('post:',view)


@route('/person')
class Person(MiddleHandler):
    def get(self):
        self.write(str([1,2,'1243']))