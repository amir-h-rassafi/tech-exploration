import random
import folium
from cluster_drawer import GeoPoint, Cluster, drawCluster

# Define the bounding box for Tehran (min_lat, max_lat, min_lng, max_lng)
tehran_bbox = (35.65, 35.75, 51.24, 51.55)

def generate_random_coordinate(bbox):
    lat = random.uniform(bbox[0], bbox[1])
    lng = random.uniform(bbox[2], bbox[3])
    return GeoPoint(lat, lng)

# Generate random coordinates for 50 clusters with 2 nodes each
num_clusters = 10
num_nodes_per_cluster = 2

cluster = Cluster("Test")
cluster.setCenter(generate_random_coordinate(tehran_bbox))
cluster.addPoint(generate_random_coordinate(tehran_bbox))
cluster.addPoint(generate_random_coordinate(tehran_bbox))
cluster.addPoint(generate_random_coordinate(tehran_bbox))
cluster.addPoint(generate_random_coordinate(tehran_bbox))



map_center = GeoPoint((tehran_bbox[0] + tehran_bbox[1]) / 2, (tehran_bbox[2] + tehran_bbox[3]) / 2)        
map_obj = folium.Map(location=map_center.toTuple(), zoom_start=12)


drawCluster(cluster, map_obj, name="test")

