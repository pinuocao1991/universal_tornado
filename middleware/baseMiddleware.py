# coding:utf-8
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

