# umap_geojson
Read gpx file which was generate by the OSMTrakcer for Android app
and convert GeoJSON file that can be imported to uMap system.

# how to use

## download files
- umapgeojson.py 
- gpx2geojson.py
- requirements.txt

## install dependent modules
- pip install requirements.txt

## how to use
- get a gpx file from android smartphone
- run gpx2geojson.py : python gpx2geojson.py (gpx_filename)
- as a result of execution, the file name is saved by changing the extension .gpx to .geojson
- import geojson file to uMap system

# environment in which operation has been confirmed
- os : windows 10
- python 3.6.8
- geojson==2.5.0
- gpxpy==1.3.5
