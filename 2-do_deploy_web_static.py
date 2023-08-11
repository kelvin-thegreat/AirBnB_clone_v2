#!/usr/bin/python3
"""
mdule to deploy zipped web static  files  to web servers
"""

from fabric.api import env, put, run
from os.path import exists, isfile
import os
import argparse

env.hosts = ['100.25.138.54', '100.26.161.218']


def do_deploy(archive_path):
    """
    do_deploy class:
    distributes an archive to your web servers
    return : false, true, do_deploy 
    """

    if not exists(archive_path) and not isfile(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        no_ext = os.path.splitext(archive_filename)[0]

        """ upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, '/tmp/')

        """ Extract the archive to the folde"""
        release_folder = '/data/web_static/releases/' + no_ext + '/'
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        """delete the archive from the web server and
        move files to proper locations"""
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {}web_static/* {}'.format(release_folder, release_folder))

        run('rm -f /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print('New version deployed!')
        return True

    except Exception:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('archive_path', type=str, help='path to the archive file')
    parser.add_argument('-u', '--username', type=str, help='SSH username')
    parser.add_argument('-i', '--private-key', type=str, help='Path to SSH private key')
    arg = parser.parse_args()

    if arg.username:
        env.user = args.username

    if arg.private_key:
        env.key_filename = arg.private_key

    do_deploy(arg.archive_path)
