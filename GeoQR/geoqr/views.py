from pyramid.view import view_config

import pyramid.httpexceptions as exc

from geoqr.lib.qrdecoder import decode

from geoqr.lib import googlemaps
from geoqr.lib import qrencoder

import datetime

def date_parse(date):
    """parses a string to a proper datetime object
    yyyy-MM-dd'T'HH:mm'Z'"""
    return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%MZ")

def pluck(lst, checkfn):
    """Plucks an element from the list"""
    for element in lst:
        if checkfn(element):
            return element

def collect(iterable, check, transform=lambda x: x):
    """
    Collects and transforms
    """
    return [transform(x) for x in iterable if check(x)]

def handle_errors(req):
    """Pulls errors out of the request context and
    adds them to the session"""
    check_param = lambda x: x[0] == u"error"
    return collect(req.params.iteritems(), check_param, lambda x: x[1])
            
            
@view_config(route_name='home', renderer='login.mako')
def index(request):
    """
    Basic index for the page. If there's a user, go to the action
    screen, if not display the login screen
    """
    if "user" in request.session:
        raise exc.HTTPFound(request.route_url("actions"))
    return {
        "errors": handle_errors(request)
        }    

@view_config(route_name="doLogin")
def doLogin(request):
    """
    Logins a user, then goes to index
    """
    p = request.params
    login_info = {
        "email": p["email"],
        "password": p["password"]        
        }
    account = request.api.index("accounts/login", params=login_info)
    if account:
        request.session["user"] = account
    raise exc.HTTPFound(request.route_url("home") + "?error=INVALID_LOGIN")
    

@view_config(route_name="actions", renderer="actions.mako")
def actions(request):
    """List of available actions for the user"""
    return {}

    
@view_config(route_name="scan", renderer="scan.mako")
def scan(request):
    """Page to scan in a new photo"""
    for x in request.params.iteritems():
        print x
    errors = handle_errors(request)
    print errors
    return {
        "errors": errors
        }
    

@view_config(route_name="doScan", renderer="json")
def doScan(request):
    """Processes a photo, gets the geoqr info from it and """
    p = request.params
    lat, lon = p.get("lat"), p.get("lon")
    f = request.POST['code'].file
    f.seek(0)
    code = decode(request.POST['code'].filename, f)
    if not code:
        raise exc.HTTPFound(request.route_url("scan") + "?error=CODE_NOT_READABLE")
    created = request.api.create("accounts/%s/checkins" % request.session['user']['id'],
                                 data={
                                     "code": code,
                                     "lat": lat,
                                     "lon": lon
                                 })
    if created:
        raise exc.HTTPFound(request.route_url("list"))
    else:
        raise exc.HTTPFound(request.route_url("scan") + "?error=BAD_LOCATION")
    
    
@view_config(route_name="list", renderer="list.mako")
def list(request):
    """View all listings"""
    checkins = request.api.index("accounts/%s/checkins" %
                                 request.session["user"]["id"])
    
    for c in checkins:
        c['location'] = request.api.get("locations", c['location'])
        c['expired'] = date_parse(c['expiresOn']) > datetime.datetime.now()
    sorted(checkins, key = lambda checkin: checkin['createdOn'], reverse=True)
    return {
        "checkins": checkins
    }

    
@view_config(route_name="view", renderer="view.mako")
def view(request):
    """View a specific listing"""
    checkins = request.api.index("accounts/%s/checkins" %
                                 request.session["user"]["id"])
    checkin = pluck(checkins, lambda x: x.get('location') == request.params.get("id"))
    location = request.api.get("locations", request.params.get("id"))
    location.update(checkin)
    location['canValidate'] = (not location['validated'] and
                               date_parse(location['expiresOn']) > datetime.datetime.now())
    return location

    
@view_config(route_name="add_listing", renderer="add.mako")
def add(request):
    """Add a new location"""

    return {}

    
@view_config(route_name="do_add", renderer="showCode.mako")
def doAdd(request):
    """
    Makes an entry and QRcode for the poster
    """
    
    p = request.params
    lat, lon = googlemaps.decode_to_latlon(p['address'])
    if not lat or not lon:
        raise exc.HTTPFound(request.route_url("add_listing") + "?error=ADDRESS_NOT_FOUND")

    new_loc = {
        "code": p['code'],
        "lat": str(lat),
        "lon": str(lon),
        "info": p['info'],
        "timeToExpires": 24
        }
    
    if request.api.create("locations", data=new_loc):
        img = qrencoder.generate_from_code(new_loc['code'])
        raise exc.HTTPFound(img)
    raise exc.HTTPFound(request.route_url("add_listing") + "?error=UNABLE_TO_CREATE")
    
@view_config(route_name="redeem", renderer="string")
def redeem(request):
    """Redeems a QRcode"""    
    request.api.create("accounts/%s/checkins/%s/redeem" % (request.session['user']['id'],
                                                          request.params['location']),
                       data={})
    raise exc.HTTPFound(request.route_url("list"))
    
