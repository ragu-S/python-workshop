#!/usr/bin/python
# def firstFunction(parm1):
#     print 'first function called with parm1: ', parm1
#     print 'will return false'
#     return 0

import urllib2

gh_url = 'http://www.tutorialspoint.com/python/python_command_line_arguments.htm'

req = urllib2.Request(gh_url)

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'pass')

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(req)

print handler.getcode()

print handler.info()

print req.get_data()
