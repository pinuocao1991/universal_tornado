import importlib
from config.base import RequestHandler

#引入中间件，可以自定义过滤器。
middleware_list = [
    'middleware.testMiddleware.TestMiddleware'
]

class MiddleHandler(RequestHandler):

    def initialize(self):
        # 若子类内没有自定义，则使用settings内的默认配置
        try:
            self.middleware_list
        except AttributeError:
            self.middleware_list = middleware_list

    def prepare(self):
        for middleware in self.middleware_list:
            mpath, mclass = middleware.rsplit('.', maxsplit=1)
            mod = importlib.import_module(mpath)
            getattr(mod, mclass).process_request(self, self)

    def on_finish(self):
        for middleware in self.middleware_list:
            mpath, mclass = middleware.rsplit('.', maxsplit=1)
            mod = importlib.import_module(mpath)
            getattr(mod, mclass).process_response(self, self)

    def finish(self, chunk=None):
        super().finish(chunk)

    def write_error(self, status_code, **kwargs):
        # 若捕获错误，则发送错误信息给client
        exc_cls, exc_instance, trace = kwargs.get("exc_info")
        if status_code != 200:
            self.set_status(status_code)
            self.write({"msg": str(exc_instance)})
