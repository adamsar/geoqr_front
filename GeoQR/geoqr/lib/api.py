"""
Module for interacting with the GeoQR API
"""

import urllib
import httplib2
import json

class API(object):

    BASE_URL = "localhost:9000"

    def _get(self, url, params={}):
        """
        Quick access for http2 get
        """
        if params:
            url += "?%s" % urllib.urlencode(params)

        print url
        h = httplib2.Http()
        return h.request(url)        

        
    def get(self, resource, _id):
        """
        Gets a single resource
        """
        response, content = self._get("http://%s/%s/%s" % (self.BASE_URL,
                                                          resource,
                                                          _id))
        if int(response['status']) is 200:
            return json.loads(content)
        return None
        
    
    def index(self, resource, params={}):
        """
        Index for a particular resource
        """

        response, content = self._get("http://%s/%s" % (self.BASE_URL,
                                                        resource), params)
        if int(response["status"]) is 200:
            return json.loads(content)
        return


    def _post(self, url, data):
        h = httplib2.Http()
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        encoded_data = urllib.urlencode(data)
        print "url:"
        print url
        resp, content = h.request(url, "POST", headers=headers, body=encoded_data)
        print resp
        print content
        return resp, content
        
            
    def create(self, resource, data={}):
        """
        Creates a new entry in the resource
        """
        
        full_url = "http://%s/%s" % (self.BASE_URL, resource)
        response, content = self._post(full_url, data)

        if int(response['status']) == 201:
            return True
        return False
        

    def post(self, resource, _id, action, data={}):
        """
        Post an action to a specific resource
        """

        full_url = "http://%s/%s/%s/%s" % (self.BASE_URL, resource,
                                           str(_id), action)
        response = self._post(full_url, data)

        if response and response.code == 201:
            return True
        return False 

