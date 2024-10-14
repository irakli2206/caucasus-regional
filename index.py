import geopandas as gpd
import matplotlib.pyplot as plt

# Read the shapefile
world = gpd.read_file('gaul1_asap.shp')
world_regions = world['name1']

print('qwe', world_regions)

# Example genetic distance data
data = [
    # Georgia
    ['Kakheti', 10.2], 
    ['Imereti', 10.7], 
    ['Kvemo Kartli', 11.1], 
    ['Samergelo and Zemo (upper) Svaneti', 8.9], 
    ['Samtskhe-Javakheti', 11], 
    ['Tbilisi', 11], 
    ['Abkhazia Aut. Rep.', 5], 
    ['Mtskheta-Mtianeti', 9.1], 
    ['Shida Kartli', 10.1], 
    ['Guria', 8.6], 
    ['Racha-Lechkhumi and Kvemo (lower) Svaneti', 8.5], 
    ['Adjara Aut. Rep.', 13.9], 
    # Russia
    ['Dagestan Rep.', 13.4], 
    ['Chechnya Rep.', 19.7], 
    ['Severnaya Osetiya-alaniya Rep.', 10.6], 
    ['Ingushetiya Rep.', 15],
    ['Kabardino-balkariya Rep.', 11], 
    ['Karatchayevo-cherkesiya Rep.', 9.4], 
    ['Adygeya Rep.', 9.5], 
    ['Stavropolskiy Kray', 9.1], 
    ['Krasnodarskiy Kray', 9.5],
    # Azerbaijan
    ['Ganja-Gazakh', 12],
    ['Absheron', 7],
    ['Guba-Khachmaz', 14.1],  
    ['Aran', 13.7],
    ['Nakhchivan', 9.8],
    ['Lankaran', 14.2],  
    ['Daghlig Shirvan', 13.8],  
    ['Yukhari Garabakh', 14.1],  
    ['Shaki-Zaqatala', 12.2],  
    ['Kalbajar-Lachin', 14.5],
]

# Filter for a specific country (e.g., Georgia)
country = 'Azerbaijan'
regions = world[world['name0'] == country]

# Get region names and their geometries
region_names = regions['name1'].unique().tolist()
print(f'All entries of names for {country}:\n', region_names)

# Create and configure the figure
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=0.5, color='k')

# Define the boundaries for the plot (xlim and ylim)
xlim = (37, 50)  # Longitude limits
ylim = (38, 46)  # Latitude limits
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# Find centroids of the regions and annotate them
for region, value in data:
    # Find the corresponding region geometry
    matched_region = world.loc[world['name1'] == region]
    
    if not matched_region.empty:
        # Get the centroid of the region in the projected CRS
        centroid = matched_region.geometry.centroid.iloc[0]
        
        # Annotate the region with the value from the data
        ax.text(centroid.x, centroid.y, str(value), ha='center', va='center', fontsize=12, color='blue')



plt.title("Fertility rate in the Caucasus")

# Use tight_layout for better fit
plt.tight_layout()

# Save the figure with improved quality
plt.savefig('genetic_distance_map.png', dpi=300, bbox_inches='tight')

plt.show()
