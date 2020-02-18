#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:20:41 2020

@author: twillia2
"""
import os
from urllib.request import urlretrieve
from osgeo import gdal
from gdalmethods import warp, gdal_options


# Constants
ALBERS = ("+proj=aea +lat_1=20 +lat_2=60 +lat_0=40 +lon_0=-96 +x_0=0 "
          "+y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ")
DST = "data/test.tif"
SRC = "data/spei2_1895_10_PRISM.tif"

# Get the sample raster (A drought index for Oct, 1895!)
if not os.path.exists(SRC):
    URL = "https://wrcc.dri.edu/wwdt/data/PRISM/spei2/spei2_1895_10_PRISM.tif"
    urlretrieve(URL, SRC)

# Create a data folder if not present
os.makedirs("data", exist_ok=True)

# Tests
def test_options():
    """Test that gdal_options doesn't break for 'warp'."""
    gdal_options("warp")

def test_warp():
    """Test that warp runs and writes the expected file."""
    warp(SRC, DST, dstSRS=ALBERS, srcNodata=-9999., dstNodata=-9999.,
         overwrite=True)
    assert os.path.exists(DST)

def test_shape():
    """Test that the shape of the output files' data array is correct."""
    test = gdal.Open(DST).ReadAsArray()
    assert test.shape == (908, 1571)

def test_all():
    """Test three conditions for gdalmethod.warp."""
    test_options()
    test_warp()
    test_shape()

# Run all of these, we need the files
if __name__ == "__main__":
    test_all()
