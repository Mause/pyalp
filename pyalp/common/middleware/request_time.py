from time import time


IDENT = b'<!-- request_time -->'


class TimerMiddleware(object):
    def process_request(self, request):
        request._tm_start_time = time()

    def process_response(self, request, response):
        if not hasattr(request, "_tm_start_time"):
            return response

        total = time() - request._tm_start_time

        if IDENT in response.content:
            response.content = response.content.decode().replace(
                IDENT.decode(),
                '{:.4f}s'.format(total)
            ).encode()

        return response
