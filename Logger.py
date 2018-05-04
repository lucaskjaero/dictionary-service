import os

import logging
from logdna import LogDNAHandler

key = os.environ['LOGDNA_KEY']
options = {

}
handler = LogDNAHandler(key, options)

log = logging.getLogger('logdna')
log.setLevel(logging.INFO)
log.addHandler(handler)


def get_logger():
    return log
