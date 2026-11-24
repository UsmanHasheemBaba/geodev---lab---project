import geopandas as gpd

gpd.read_file("data/processed/wards.gpkg", layers="wards").to_crs(epsg=32631)
gpd.read_file("data/processed/roads.gpkg", layers="roads").to_crs(epsg=32631)

agodi = wards[wards["ward_name"] =="Agodi"]

agodi_roads = gpd.clip(roads, agodi)
print("Roads in Agodi:", len(agodi_roads))
print("Road length in Agodi:" round(agodi_roads.length.sum() / 1000,2),"km")

# Merging wards into lgas

lga = wards.dissolve(by="lga_name")
print(lga.reset_index()["lga_name"])
print("LGA area:", round(lga.area.iloc[0]) / 1000000, 1), "km2"