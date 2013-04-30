#!/usr/bin/env python

import json
import os

with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)

try:
    os.unlink('requirements.txt')
except OSError:
    print "No requirements.txt found, using production config."

print 'Using PRODUCTION mode requirements'
os.symlink('requirements/_base.txt', 'requirements.txt')