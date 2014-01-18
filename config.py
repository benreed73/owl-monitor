import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('owlmon.cfg')

use_pushover = config.getboolean('General','use_pushover')
use_email = confg.getboolean('General','use_email')
from_email = config.get('SMTP','from_email')
to_email = config.get('SMTP','to_email')
smtp_server = config.get('SMTP','server')
smtp_port = config.get('SMTP','port')
api_key = config.get('Pushover','api_key')
user_key = config.get('Pushover','user_key')
device = config.get('Pushover','device')
