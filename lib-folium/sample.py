import random
import folium
from cluster_drawer import GeoPoint, Cluster, drawClusters

# Define the bounding box for Tehran (min_lat, max_lat, min_lng, max_lng)
tehran_bbox = (35.65, 35.75, 51.24, 51.55)

point_count = 80

dc_count = 5

def generate_random_coordinate(bbox):
    lat = random.uniform(bbox[0], bbox[1])
    lng = random.uniform(bbox[2], bbox[3])
    return GeoPoint(lat, lng)


points = [generate_random_coordinate(tehran_bbox) for i in range(point_count)]
dcs = [generate_random_coordinate(tehran_bbox) for i in range(dc_count)]


###p2p clusters

p2p_clusters = []
for i in range(int(point_count/2)):
    cluster = Cluster("cluster" + str(i))
    cluster.setCenter(points[i])
    cluster.addPoint(points[i])
    cluster.addPoint(points[i + int(point_count/2)])
    p2p_clusters.append(cluster)

grouped_clusters = []
for dc in dcs:
    dc_cluster = Cluster("dc_cluster")
    dc_cluster.setCenter(dc)
    grouped_clusters.append(dc_cluster)

for p in points:
    candidateCluster = grouped_clusters[0]
    for c in grouped_clusters:
        if p.getDistance(c.getCenter()) < candidateCluster.getCenter().getDistance(p):
            candidateCluster = c
    
    candidateCluster.addPoint(p)
    

map_center = GeoPoint((tehran_bbox[0] + tehran_bbox[1]) / 2, (tehran_bbox[2] + tehran_bbox[3]) / 2)        
map_obj = folium.Map(location=map_center.toTuple(), zoom_start=12)

for dc in dcs:
    folium.Marker(location=dc.toTuple(), icon=folium.Icon(color="red")).add_to(map_obj)

drawClusters(p2p_clusters, map_obj, name="p2p")

map_obj = folium.Map(location=map_center.toTuple(), zoom_start=12)

for dc in dcs:
    folium.Marker(location=dc.toTuple(), icon=folium.Icon(color="red")).add_to(map_obj)

drawClusters(grouped_clusters, map_obj, name="cluster")

