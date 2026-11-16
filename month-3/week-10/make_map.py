import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards")
facilities = gpd.read_file("data/processed/facilities.gpkg", layer="facilities")

fig,ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color="#E6F2FE", edgecolor="#037E8D")
facilities.plot(ax=ax, color="#0FEA13", markersize=15)
ax.set_title("Ibadan North Health Facilities")
ax.set_axis_off()

fig.savefig("month-3/week-10/ibadan_healthfacilities.pdf", dpi=200, bbox_inches="tight")
print("Map saved")