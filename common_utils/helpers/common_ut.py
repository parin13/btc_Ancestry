#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.0.1"


import os, sys
from os.path import dirname, join, abspath
import uuid 


sys.path.insert(0, abspath(join(dirname(__file__), '..')))


def get_error_traceback(sys, e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return "%s || %s || %s || %s" %(exc_type, fname, exc_tb.tb_lineno,e)


def generate_uuid4():
    return str(uuid.uuid4()) 
