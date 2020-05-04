from config.base import route, RequestHandler

@route('/students')
class students(RequestHandler):
    def get(self):
        self.write("students class")

    def post(self):
        self.write("student post now")
