from config.base import route
from config.middleware import MiddleHandler


@route('/students')
class students(MiddleHandler):
    def get(self):
        self.write("students class")

    def post(self):
        self.write("student post now")
