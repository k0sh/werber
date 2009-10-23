#!/usr/bin/env python
# -*- mode: python; coding: utf-8; -*-

import sys

db = {}

def ip_update(ip, size):
    if db.has_key(ip):
        db[ip] += size
    else:
        db[ip] = size

for line in sys.stdin:
    raw_list = line.split()
    ip_update(raw_list[2], int(raw_list[4]))

print db

