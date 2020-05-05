from middleware.baseMiddleware import Middleware


class TestMiddleware(Middleware):
    def process_request(self, request):
        request.get
        print('TestMiddleware - request')
        print(request)

    def process_response(self, response):
        print('TestMiddleware - response')
        print(response)
