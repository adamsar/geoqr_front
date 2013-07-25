from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    sf = UnencryptedCookieSessionFactoryConfig('geoqr')
    config = Configurator(settings=settings, session_factory=sf)
    map(lambda x: config.add_route(x[0], x[1]),
        {
            "home": "/",
            "doLogin": "/doLogin",
            "actions": "/actions",
            "scan": "/scan",
            "list": "/list",
            "view": "/view",
            "doScan": "/doScan",
            "add_listing": "/addListing",
            "do_add": "/doAdd",
            "redeem": "/redeem"
        }.iteritems())
    def add_api(event):
        from geoqr.lib.api import API
        event.request.api = API()
        
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_subscriber(add_api, NewRequest)
    config.scan()
    return config.make_wsgi_app()
