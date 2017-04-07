#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import commands
import json


@click.command()
@click.argument('project')
def export_hosts(project):
    ret = commands.getoutput('/usr/bin/gcloud compute --project "%s" instances list --format json' % project)
    export = {}
    for host in json.loads(ret.strip()):
        export[host['name']] = {
            "tags": ",".join(["gcp", project] + host['tags']['items']),
            "osFamily": "Linux",
            "username": "root",
            "osVersion": "7",
            "osArch": "x86_64",
            "description": "GCE Node",
            "hostname": host['networkInterfaces'][0]['accessConfigs'][0]['natIP'],
            "nodename": host['name'],
            "osName": "CentOS 7",
            "cpuPlatform": host['cpuPlatform']
        }
    click.echo(json.dumps(export))


export_hosts()
