import json
import numpy as np
import requests
import sys

python_version = sys.version_info[0]
if python_version == 2:
    import urllib2 as lib2
    import urllib as lib
if python_version == 3:
    import urllib.request as lib2
    import urllib.parse as lib

def load_data(file=None):
    data = None
    # Gets the Raw GitHub file using the simple 'urllib' module
    url = "https://raw.github.com/landtechnologies/technical-challenge/master/" + file
    try:
        req = lib2.Request(url)
    except Exception:
        req = None
    if req:
        res = lib2.urlopen(req)
        # Reads the file line-by-line
        data = res.readlines()
    return data

def get_color(p=None,r=None):
    v = None
    if p and r:
        for color,val in r.items():
            if p > val:
                v = color
            else:
                break
    return v

def get_relative_percentage(arr=[]):
    vals = {}
    if arr:
        a = np.array(arr)
        bounds = {0:'p',5:'b',25:'g',75:'y',95:'r'}
        for perc,color in bounds.items():
            p = np.percentile(a, perc)
            vals[color] = p
    return vals
