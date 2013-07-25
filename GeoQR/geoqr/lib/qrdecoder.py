"""
Decodes QRCodes using zxcoder
"""
import httplib
import mimetypes
import urlparse
from lxml import etree

RAW_CODE = "<td>Raw bytes</td><td><pre.*>(.+)</pre>"

ZX_URL = "http://zxing.org/w/decode"

def multipart_post(host, selector, fields, files):
    """
    Performs a HTTP multpart POST request
    """
    content_type, body = encode_multipart_data(fields, files)
    h = httplib.HTTP(host)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    return h.file.read()
    
def encode_multipart_data(fields, files):
    """
    Encodes multipart data
    """
    LIMIT = "--------lImIt_of_THE_fIle_eW_$"
    CRLF = "\r\n"
    L = []
    for (key, val) in fields:
        L.append('--' + LIMIT)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(val)
    for (key, filename, val) in files:
        L.append('--' + LIMIT)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename,))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(val)
    L.append('--' + LIMIT + '--')
    L.append('')
    L = [str(seg) for seg in L]
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % LIMIT
    return content_type, body

def get_content_type(filename):
    """
    Guesses the content type of a file
    """
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    
def post_file(url, files):
    """
    Posts a file
    """
    urlparts = urlparse.urlsplit(url)
    return multipart_post(urlparts[1], urlparts[2], {}, files)


def decode(name, f):
    """
    Does the actual decoding
    """
    data = post_file(ZX_URL, [
        ('f', name, f.read(),)
    ])
    try:
        tree = etree.fromstring(data)
        return tree.xpath("/html/body/div/table/tr[5]/td[2]/pre")[0].text
    except:
        return None
