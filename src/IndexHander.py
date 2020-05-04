from config.base import route, RequestHandler

@route('/')
class Main(RequestHandler):
    def get(self):
        self.write("Hello World")

@route('/person')
class Person(RequestHandler):
    def get(self, name):
        self.write(name)