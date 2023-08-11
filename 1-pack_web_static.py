#!/usr/bin/python3
""" scriptto  generates .tgz archive from contents of the web_static folder  """
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''Function do_pack to return the archive path
    '''
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    site = f'versions/web_static_{now}.tgz'
    print(f'Packing web_static to {site}')
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    fab_stat = local(f'tar -cvzf {site} web_static')
    if fab_stat.succeeded:
        site_size = os.path.getsize(site)
        print(f'web_static packed: {site} -> {site_size}Bytes')
        return site
    else:
        return None
