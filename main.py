#!/usr/bin/python

import platform


os = platform.system()

if os == 'Linux':
    print 'There is no viruses!'
elif os == 'Windows':
    print 'High risk! Your system infected!'
else:
    print "What the hell I'm running on?"

