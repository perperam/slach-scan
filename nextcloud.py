import requests
import urllib
from pathlib import Path

def nextcloud_drop(url, filename):
    """drop a file to an shered nextcloud folder with upload rights
    
    Arguments:
    url -- the url from the nextcloud shere menu
    filename -- name or path of the file to drop
    
    Return:
    response status False or True
    
    
    from example url:
    https://cloud.domain.eu/index.php/s/49Ah8teLFkukemMk
    made with the curl command:
    curl -T myfile.png -u "49Ah8teLFkukemMk:" -H 'X-Requested-With: XMLHttpRequest' https://cloud.domain.eu/public.php/webdav/myfile.png
    and:
    https://curlconverter.com/python/
    """
    
    # split url
    o = urllib.parse.urlparse(url)

    # authentication
    auth = Path(o.path).name

    # request url
    rurl = o._replace(path='', params='', query='', fragment='').geturl()
    path  = Path("public.php/webdav") / filename
    rurl = urllib.parse.urljoin(rurl, path.as_posix())
    
    # request prep
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
    }

    with open(filename, 'rb') as f:
        data = f.read()

    # upload file
    response = requests.put(
        rurl,
        headers=headers,
        data=data,
        auth=(auth, ''),
    )
    return response.ok
