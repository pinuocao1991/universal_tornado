import importlib

from config.base import RequestHandler


class Middleware(object):
    '''
    中间件基类
    '''
    # 继承该类对象被调用的时候触发，返回对象的结果 - 在 MiddleHandler 类内进行处理（当前未处理）
    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request)
        return response

class TestMiddleware(Middleware):
    def process_request(self, request):
        print('TestMiddleware - request')
        print(request) # <__main__.ProfileHandler object at 0x000001EBF1277A58>

    def process_response(self, request):
        print('TestMiddleware - response')

class TestMiddleware2(Middleware):
    def process_request(self, request):
        print('TestMiddleware2 - request')
    def process_response(self, request):
        print('TestMiddleware2 - response')

class MiddleHandler(RequestHandler):
    '''
    中间件处理基类
    基于多中间件的 request和response 处理顺序
     - process_request-1、process_request-2
     - process_response-1、process_response-2
    '''

    def initialize(self):
        # 若子类内没有自定义，则使用settings内的默认配置
        try:
            self.middleware_list
        except AttributeError:
            self.middleware_list = [
                'middleware.TestMiddleware',
                'middleware.TestMiddleware2',
            ]

    def prepare(self):
        for middleware in self.middleware_list:
            mpath, mclass = middleware.rsplit('.', maxsplit=1)
            # mod = importlib.import_module(mpath)
            mod = '.'
            mclass = TestMiddleware
            getattr(mod, mclass).process_request(self, self)

    def on_finish(self):
        for middleware in self.middleware_list:
            mpath, mclass = middleware.rsplit('.', maxsplit=1)
            mod = '.'
            mclass = TestMiddleware2
            # mod = importlib.import_module(mpath)
            getattr(mod, mclass).process_response(self, self)

    def finish(self, chunk=None):
        super().finish(chunk)

    def write_error(self, status_code, **kwargs):
        # 若捕获错误，则发送错误信息给client
        exc_cls, exc_instance, trace = kwargs.get("exc_info")
        if status_code != 200:
            self.set_status(status_code)
            self.write({"msg": str(exc_instance)})
