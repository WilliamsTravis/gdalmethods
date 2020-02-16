from setuptools import setup
import subprocess as sp
from urllib.request import urlopen
import json


# Matching gdal versions
def match_gdal():
    # Get system gdal version
    gdalinfo = sp.check_output(["gdalinfo", "--version"]).decode()
    gdalv = gdalinfo[gdalinfo.index(" ") + 1: gdalinfo.index(",")]

    # Get all pygdal releases
    pygdaljson = "https://pypi.python.org/pypi/pygdal/json"
    r = urlopen(pygdaljson)
    pygdalvs = json.loads(r.read())["releases"].keys()

    # This should work if major and 1st minor releases match
    gdalv = ".".join(gdalv.split("."))
    useablevs = [v for v in pygdalvs if gdalv == ".".join(v.split(".")[:3])]

    # Let's try the latest
    pygdal_version = useablevs[-1]

    return pygdal_version


pygdal_version = match_gdal()


setup(
    name='gdalmethods',
    version='0.0.1',
    author='Travis Williams',
    packages=['gdalmethods'],
    url="https://github.com/WilliamsTravis/gdalmethods.git",
    description=("A collection of methods a objects meant "
                 "to make using GDAL Python bindings easier."),
    include_package_data=True,
    install_requires=['numpy',
                      'pygdal==' + pygdal_version,
                      'geopandas',
                      'shapely',
                      'rasterio',
                      'tqdm']
)
