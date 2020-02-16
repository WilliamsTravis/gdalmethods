#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:58:40 2020

@author: twillia2
"""
from setuptools import setup
import subprocess as sp
from urllib.request import urlopen
import json


# Matching gdal versions
def match_gdal():
    # Get system gdal version
    gdalinfo = sp.check_output(["gdalinfo", "--version"]).decode()
    gdalv = gdalinfo[gdalinfo.index(" ") + 1: gdalinfo.index(",")]
    print(gdalv)

    # Get all pygdal releases
    pygdaljson = "https://pypi.python.org/pypi/pygdal/json"
    r = urlopen(pygdaljson)
    pygdalvs = json.loads(r.read())["releases"].keys()
    print(pygdalvs)

    # This should work if major and 1st minor releases match
    gdalv = ".".join(gdalv.split("."))
    useablevs = [v for v in pygdalvs if gdalv == ".".join(v.split(".")[:3])]

    # Let's try the latest
    pygdal_version = useablevs[-1]

    return pygdal_version


pygdal_version = match_gdal()
print(pygdal_version)