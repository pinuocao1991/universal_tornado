from config.base import route
from config.middleHandler import MiddleHandler


@route([r'/students/(.*)',r'/students'])
class students(MiddleHandler):

    def get(self,view=None):
        print(view)
        id = self.get_arguments("id")
        self.write("students class")

    def post(self):
        self.write("student post now")

