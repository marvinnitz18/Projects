#!/usr/bin/python3

from pythonping import ping


def get_latency(host):
   ping(host, verbose=True) 


get_latency("1.1.1.1")