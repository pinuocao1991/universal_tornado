from tornado.web import HTTPError
from config.base import route, params
from config.middleHandler import MiddleHandler


@route(['/'])
class IndexHander(MiddleHandler):

    @params(
        strs=["view",'id'],
        ints=['ss'],
        required_params=["id"]
    )
    def get(self,view,**kwargs):
        print(kwargs)
        print(view)
        raise HTTPError(500, reason="你好")

    def post(self,view):
        print('post:',view)


@route('/person')
class Person(MiddleHandler):
    def get(self):
        self.write(str([1,2,'1243']))