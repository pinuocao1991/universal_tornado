# conding:utf-8
from typing import List

import tornado.web
from tornado.log import access_log


# 请求日志
def log_func(handler):
    if handler.get_status() < 400:
        log_method = access_log.info
    elif handler.get_status() < 500:
        log_method = access_log.warning
    else:
        log_method = access_log.error
    request_time = 1000.0 * handler.request.request_time()
    log_method('''%d %s %s (%s) %s %s %.2fms''',
               handler.get_status(), handler.request.method,
               handler.request.uri, handler.request.remote_ip,
               handler.request.headers["User-Agent"],
               handler.request.arguments,
               request_time)

settings = {
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "log_function": log_func,
}




class Application(tornado.web.Application):
    """
    Tornado 应用实例
    """

    def load_handler_module(self, handler_module, perfix=".*$"):
        """
        从模块加载 RequestHandler
            `handler_module` : 模块
            `perfix` : url 前缀
        """
        # 判断是否是有效的 RequestHandler (是类且是 RequestHandler 的子类)
        is_handler = lambda cls: isinstance(cls, type) and issubclass(cls, RequestHandler)

        # 判断是否拥有 url 规则
        has_pattern = lambda cls: hasattr(cls, 'url_pattern') and cls.url_pattern
        handlers = []

        # 迭代模块成员

        for i in dir(handler_module):
            cls = getattr(handler_module, i)
            if is_handler(cls) and has_pattern(cls):
                if isinstance(cls.url_pattern, List):
                    for pattern in cls.url_pattern:
                        handlers.append((pattern, cls))
                else:
                    handlers.append((cls.url_pattern, cls))
        self.add_handlers(perfix, handlers)

    def _get_host_handlers(self, request):
        """
        覆盖父类方法, 一次获取所有可匹配的结果. 父类中该方法一次匹配成功就返回, 忽略后续
        匹配结果. 现通过使用生成器, 如果一次匹配的结果不能使用可以继续匹配.
        """
        host = request.host.lower().split(':')[0]
        # 使用生成器表达式而非列表推导式, 减少性能折扣
        handlers = (i for p, h in self.handlers for i in h if p.match(host))

        # Look for default host if not behind load balancer (for debugging)
        if not handlers and "X-Real-Ip" not in request.headers:
            handlers = [i for p, h in self.handlers for i in h if p.match(self.default_host)]
        return handlers


class RequestHandler(tornado.web.RequestHandler):
    url_pattern = None


def route(url_pattern):
    """
    路由装饰器, 只能装饰 RequestHandler 子类
    """
    def handler_wapper(cls):
        assert (issubclass(cls, RequestHandler))
        cls.url_pattern = url_pattern
        return cls
    return handler_wapper

