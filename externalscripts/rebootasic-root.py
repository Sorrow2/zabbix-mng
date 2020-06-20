#!/usr/bin/env python3

import httplib2
import sys

URL = "http://"+sys.argv[1]+"/cgi-bin/reboot.cgi"
USER = "root"
PASS = "root"

h = httplib2.Http(cache=None, timeout=0.1)
h.add_credentials(USER, PASS)
try:
	resp = h.request(URL, "GET", headers={'cache-control':'no-cache'})
	resp
	print ("OK")
except:
	print ("Asic not avalible")
