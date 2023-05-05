import folium
import random
from folium.plugins import MarkerCluster

# Define the bounding box for Tehran (min_lat, max_lat, min_lng, max_lng)
tehran_bbox = (35.65, 35.75, 51.24, 51.55)

def generate_random_coordinate(bbox):
    lat = random.uniform(bbox[0], bbox[1])
    lng = random.uniform(bbox[2], bbox[3])
    return (lat, lng)

# Generate random coordinates for 50 clusters with 2 nodes each
num_clusters = 10
num_nodes_per_cluster = 2

clusters = []
for _ in range(num_clusters):
    cluster = []
    for _ in range(num_nodes_per_cluster):
        node = generate_random_coordinate(tehran_bbox)
        cluster.append(node)
    clusters.append(cluster)

# Create a folium Map object centered on the middle of Tehran bounding box
map_center = ((tehran_bbox[0] + tehran_bbox[1]) / 2, (tehran_bbox[2] + tehran_bbox[3]) / 2)
map_obj = folium.Map(location=map_center, zoom_start=12)

# Add markers and lines for each cluster
for cluster in clusters:
    marker_cluster = MarkerCluster().add_to(map_obj)

    for node in cluster:
        folium.Marker(location=node).add_to(marker_cluster)

    folium.PolyLine(locations=cluster, color="blue", weight=2.5, opacity=1).add_to(map_obj)

# Save the map as an HTML file
map_obj.save("map.html")

