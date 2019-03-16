from datetime import datetime
from django.conf import settings
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class RequestTimeMiddleware(MiddlewareMixin):
    """ Display request time on a page """

    def process_request(self, request):
        if not settings.DEBUG:
            return
        request.start_time = datetime.now()

    def process_response(self, request, response):
        if not settings.DEBUG:
            return response
        # if our procees_request was canceled somewhere within
        # middleware stack, we cannot calculate request time
        if not hasattr(request, 'start_time'):
            return response

        # calculate request execution time
        request.end_time = datetime.now()
        if 'text/html' in response.get('Content-Type', ''):
            response.write('<br>Request took: %s' % str(request.end_time - request.start_time))
            return response

    def process_view(self, request, view, args, kwargs):
        return None

    def process_template_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        return HttpResponse('Exception found: %s' % exception)
