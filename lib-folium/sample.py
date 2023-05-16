import random
import folium
from cluster_drawer import GeoPoint, Cluster, drawClusters
from ride import Ride, generate_random_ride

# Define the bounding box for Tehran (min_lat, max_lat, min_lng, max_lng)
tehran_bbox = (35.65, 35.75, 51.24, 51.55)

ride_count = 40

dc_count = 6

def generate_random_coordinate(bbox):
    lat = random.uniform(bbox[0], bbox[1])
    lng = random.uniform(bbox[2], bbox[3])
    return GeoPoint(lat, lng)

def getMapWithDcs(dcs, box):
    map_center = GeoPoint((box[0] + box[1]) / 2, (box[2] + box[3]) / 2)        
    map_obj = folium.Map(location=map_center.toTuple(), zoom_start=12)
    for dc in dcs:
        folium.Marker(location=dc.toTuple(), icon=folium.Icon(color="red")).add_to(map_obj)
    return map_obj

rides = [generate_random_ride(tehran_bbox) for i in range(ride_count)]
sourcePoints = [ride.getSource() for ride in rides]
destinationPoints = [ride.getDest() for ride in rides]
dcs = [generate_random_coordinate(tehran_bbox) for i in range(dc_count)]


###p2p clusters

p2p_clusters = []
for i, ride in enumerate(rides):
    cluster = Cluster("cluster" + str(i))
    cluster.setCenter(ride.getSource())
    cluster.addPoint(ride.getSource())
    cluster.addPoint(ride.getDest())
    p2p_clusters.append(cluster)

source_clusters = []
dest_clusters = []
for dc in dcs:
    dc_cluster = Cluster("dc_cluster")
    dc_cluster.setCenter(dc)
    source_clusters.append(dc_cluster)
    dest_clusters.append(dc_cluster)

for p in sourcePoints:
    candidateCluster = source_clusters[0]
    for c in source_clusters:
        if p.getDistance(c.getCenter()) < candidateCluster.getCenter().getDistance(p):
            candidateCluster = c
    candidateCluster.addPoint(p)


for p in destinationPoints:
    candidateCluster = dest_clusters[0]
    for c in dest_clusters:
        if p.getDistance(c.getCenter()) < candidateCluster.getCenter().getDistance(p):
            candidateCluster = c
    candidateCluster.addPoint(p)    

map_obj = getMapWithDcs(dcs, tehran_bbox)
drawClusters(p2p_clusters, map_obj, name="p2p")

map_obj = getMapWithDcs(dcs, tehran_bbox)
drawClusters(source_clusters + dest_clusters, map_obj, name="cluster")

map_obj = getMapWithDcs(dcs, tehran_bbox)
drawClusters(source_clusters, map_obj, name="source_cluster")

map_obj = getMapWithDcs(dcs, tehran_bbox)
drawClusters(dest_clusters, map_obj, name="dest_cluster")