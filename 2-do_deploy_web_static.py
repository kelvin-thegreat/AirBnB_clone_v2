#!/usr/bin/python3
""" module to extract and deploy  web static files
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['100.25.138.54', '100.26.161.218']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
        """
        do_deploy class : deploys archived path
        Deploy web files to server
        returns : False, true
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                """ upload archive"""
                put(archive_path, '/tmp/')

                """create target dir"""
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                """ uncompress archive and delete .tgz"""
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                """ remove archive"""
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                """move contents into host web_static"""
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                """ remove extraneous web_static dir"""
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                """delete sym link"""
                run('sudo rm -rf /data/web_static/current')

                """symbolic linka"""
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False
        """Successfully Deployed"""
        return True
