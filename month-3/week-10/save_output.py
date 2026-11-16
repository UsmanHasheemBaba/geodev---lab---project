import geopandas as gpd

wards = wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
wards.to_file("data/processed/wards.gpkg", layer="wards_copy")
wards.drop(columns="geometry").to_csv("data/processed/wards_table.csv", index=False)

print(gpd.list_layers("data/processed/wards.gpkg"))