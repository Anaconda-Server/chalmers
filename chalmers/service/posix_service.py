"""
Linux services
"""
from __future__ import unicode_literals, print_function

import logging

from . import cron_service, sysv_service, upstart_service, systemd_service


log = logging.getLogger('chalmers.service')

if systemd_service.check():
    PosixService = systemd_service.SystemdService
elif upstart_service.check():
    PosixService = upstart_service.UpstartService
elif sysv_service.check():
    PosixService = sysv_service.SysVService
else:
    PosixService = cron_service.CronService

