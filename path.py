#!/usr/bin/python
# Created by Adam Baldwin (evilpacket@gmail.com)
# EvilPacket

import urllib
import urllib2
import re
import sys
import json
import string
import time
import base64
from bplist import *

username = "nope@chucktesta"
password = "password"

# ====================================================

if len(sys.argv) < 2:
    print "Usage: python path.py searchterm"
    sys.exit()

user_agent = "Path/2.0.1 CFNetwork/548.0.4 Darwin/11.0.0"
credentials = base64.encodestring('%s:%s' % (username, password))[:-1]

# Common Headers
headers = {'User-Agent':user_agent,
      'X-PATH-TIMEZONE':'America/Los_Angeles',
      'X-PATH-LOCALE': 'en_US',
      'Authorization': 'Basic %s' % (credentials),
      'Accept':'*/*',
}

# Search
url = 'https://api.path.com/3/user/search?query=%s' % (sys.argv[1]) 


req = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(req)
result = response.read()
bp = BPlistReader(result).parse()

for i in bp['people']:
        a = bp['people'][i]
	print json.dumps(a)

	print "============================"

