#!/usr/bin/python

import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/messageboard")

from messageboard import app as application

