from config.base import route
from config.middleware import MiddleHandler


@route('/')
class Main(MiddleHandler):
    def get(self):
        self.write("Hello World")

@route('/person')
class Person(MiddleHandler):
    def get(self, name):
        self.write(name)