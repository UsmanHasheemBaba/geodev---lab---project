import geopandas as gpd
from shapely.geometry import polygon
from shapely.validation import explain_validity

bowtie = polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)])
print("valid:", bowtie.is_valid)
print("why:", explain_validity(bowtie))

layer = gpd'GeoDataFrame({"name": ["boetie]}, geometry=[bowtie], crs="EPSG:32361)
print("valid:", layer.is_valid)
print("why", explain_validity(layer))
