import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pi/messageboard/')

from my_flask_app import app as application

application.secret_key = 'UzQyVTlPNU43MHJKOGNnU3FLV3I0NW93a1NTekhHM0ZEN1U3NFdtZkVkZmlPcWNZTFNBRVdqWlJL'
