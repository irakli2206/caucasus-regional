import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from data import data

# List of shapefiles to read
shapefile = 'map_data/ne_10m_admin_1_states_provinces.shp'

# Read the shapefile into a GeoDataFrame
world = gpd.read_file(shapefile)

# Define a list of North Caucasian republics
north_caucasus_republics = [
    'Chechnya', 'Dagestan', 'Ingush', 'North Ossetia', 
    'Kabardin-Balkar', 'Karachay-Cherkess', 'Stavropol', 'Adygey', 
]

# Filter regions to include Georgia, Armenia, Azerbaijan, and North Caucasian republics
caucasus_countries = world[world['admin'].isin(['Georgia', 'Armenia', 'Azerbaijan']) | world['name'].isin(north_caucasus_republics)]

# Create a DataFrame for regions and values
values_df = pd.DataFrame(data, columns=['Region', 'Value']).set_index('Region')

# Create a plot
fig, ax = plt.subplots(figsize=(15, 10))

# Plot only the Caucasus regions
caucasus_countries.plot(ax=ax, edgecolor='black', facecolor='none', linewidth=0.3)

# Set limits to focus on the Caucasus region (adjust these values as necessary)
ax.set_xlim(38.0, 52.0)  # Longitude limits
ax.set_ylim(38.5, 46)  # Latitude limits

# Annotate the regions
for region, value in data:
    matched_region = caucasus_countries.loc[caucasus_countries['name'] == region]
    if not matched_region.empty:
        centroid = matched_region.geometry.centroid.iloc[0]
        ax.text(centroid.x, centroid.y, str(value), ha='center', va='center', fontsize=12, color='blue')

plt.title('Births per 1000 people in the Caucasus')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.savefig('fertility_rate_caucasus.png', dpi=300, bbox_inches='tight')
plt.show()
