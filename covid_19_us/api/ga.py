from django.conf import settings
from pyga.requests import Tracker
from pyga.requests import Page
from pyga.requests import Session
from pyga.requests import Visitor


def gq_middleware(get_response):
    ga_id = settings.GA_ID

    def middleware(request):
        if ga_id is not False:
            tracker = Tracker(ga_id, request.headers['Host'])
            visitor = Visitor()
            visitor.ip_address = request.META.get('REMOTE_ADDR')
            if request.headers['User-Agent']:
                visitor.user_agent = request.headers['User-Agent']
            session = Session()
            path = request.path
            if request.META.get('QUERY_STRING'):
                path = f"{request.path}?{request.META.get('QUERY_STRING')}"
            page = Page(path)
            page.title = request.path
            tracker.track_pageview(page, session, visitor)

        response = get_response(request)
        return response

    return middleware
