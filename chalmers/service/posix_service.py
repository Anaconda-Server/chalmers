"""
Install a crontab rule to run at system boot 
"""
from __future__ import unicode_literals, print_function

import logging
import os

from chalmers import errors

from . import cron_service, redhat_service, upstart_service


log = logging.getLogger('chalmers.service')


def system_install(target_user):
    if os.getuid() != 0:
        raise errors.ChalmersError("You must run chalmers as root when using the --system argument")

    if redhat_service.have_chkconfig():
        redhat_service.install(target_user)
    elif upstart_service.have_initctl():
        upstart_service.install(target_user)
    else:
        raise NotImplementedError("TODO:")

    log.info("All chalmers programs will now run on boot")


def system_uninstall(target_user):
    if os.getuid() != 0:
        raise errors.ChalmersError("You must run chalmers as root when using the --system argument")

    if target_user is None:
        target_user = os.environ.get('SUDO_USER')

    if redhat_service.have_chkconfig():
        redhat_service.uninstall(target_user)
    elif upstart_service.have_initctl():
        upstart_service.uninstall(target_user)

    else:
        raise NotImplementedError("TODO:")


def system_status(target_user):

    if target_user is None:
        target_user = os.environ.get('SUDO_USER')

    if redhat_service.have_chkconfig():
        redhat_service.status(target_user)
    elif upstart_service.have_initctl():
        upstart_service.status(target_user)

    else:
        raise NotImplementedError("TODO:")


def install(args):

    if args.system is False:
        cron_service.install()
    else:
        system_install(args.system)

def uninstall(args):

    if args.system is False:
        cron_service.uninstall()
    else:
        system_uninstall(args.system)

def status(args):

    if args.system is False:
        cron_service.status()
    else:
        system_status(args.system)

