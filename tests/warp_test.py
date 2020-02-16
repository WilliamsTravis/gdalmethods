#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:20:41 2020

@author: twillia2
"""
import os
from urllib.request import urlretrieve
from osgeo import gdal, osr
from pygds.gdalmethods import warp, gdal_options


# Checking for this proj4 string
ALBERS = ("+proj=aea +lat_1=20 +lat_2=60 +lat_0=40 +lon_0=-96 +x_0=0 +y_0=0 "
          "+datum=NAD83 +units=m +no_defs ")

# We have gridded climate data sets all the way back to 1895!
SRC = "data/spei2_1895_10_PRISM.tif"
DST = "data/test.tif"
DSTSRS = "epsg:102008"

# Get the sample raster
if not os.path.exists(SRC):
    URL = "https://wrcc.dri.edu/wwdt/data/PRISM/spei2/spei2_1895_10_PRISM.tif"
    urlretrieve(URL, SRC)

# Check the options function
def test_options():
    """Test that gdal_options doesn't break for 'warp'."""
    gdal_options("warp")

# And warp
def test_warp():
    """Test that warp runs and writes the expected file."""
    warp(SRC, DST, dstSRS=DSTSRS, srcNodata=-9999., dstNodata=-9999.,
         overwrite=True)
    assert os.path.exists(DST)

# And check results
def test_projection():
    """Test that the projection system of our output file is correct."""
    refs = osr.SpatialReference()
    test = gdal.Open(DST)
    wkt = test.GetProjection()
    refs.ImportFromWkt(wkt)
    proj4 = refs.ExportToProj4()
    assert proj4 == ALBERS

def test_shape():
    """Test that the shape of the output files' data array is correct."""
    test = gdal.Open(DST).ReadAsArray()
    assert test.shape == (908, 1571)
