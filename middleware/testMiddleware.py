from middleware.baseMiddleware import Middleware


class TestMiddleware(Middleware):
    def process_request(self, request):
        pass

    def process_response(self, response):
        pass
