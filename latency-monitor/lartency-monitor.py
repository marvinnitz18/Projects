#!/usr/bin/python3

import os
import subprocess as sp



def get_latency(host):
    param = '-qc1'
    command = ['ping', param, host]
    print(sp.call(command))


get_latency("1.1.1.1")