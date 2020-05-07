import importlib

from tornado.web import HTTPError

from config.base import RequestHandler

#引入中间件，可以自定义过滤器。
middleware_list = [
    'middleware.testMiddleware.TestMiddleware'
]

class MiddleHandler(RequestHandler):

    def initialize(self):
        self.keys = self.request.arguments.keys()
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

        # 获取send_error中的reason
        reason = kwargs.get('reason', 'unknown')

        # 获取HTTPError中的log_message作为reason
        if 'exc_info' in kwargs:
            exception = kwargs['exc_info'][1]
            if isinstance(exception, HTTPError) and exception.log_message:
                reason = exception.log_message
        self.write({'status_code': status_code, 'reason': reason})
