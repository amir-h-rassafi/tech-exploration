import folium
from typing import List

class GeoPoint:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.name = None

    def setName(self, name: str):
        self.name = name

    def getName(self) -> str:
        return self.name

    def getLat(self) -> float:
        return self.lat
    
    def getLng(self) -> float:
        return self.lng

    def toTuple(self) -> tuple:
        return (self.lat, self.lng)

class Cluster:
    def __init__(self, name: str):
        self.name = name
        self.points = []

    def setCenter(self, center: GeoPoint):
        self.center = center
        self.addPoint(center)

    def getCenter(self) -> GeoPoint:
        return self.center

    def addPoint(self, point: GeoPoint):
        self.points.append(point)

    def getPoints(self) -> list:
        return self.points


def drawCluster(cluster: Cluster, map_obj: folium.Map, name = None):

    for point in cluster.getPoints():
        folium.Marker(location=point.toTuple()).add_to(map_obj)
    
    polyLine = []
    for point in cluster.getPoints():
        polyLine.append(point.toTuple())
        polyLine.append(cluster.getCenter().toTuple())

    folium.PolyLine(locations=polyLine, color="blue", weight=2.5, opacity=1).add_to(map_obj)

    if name is None:
        name = "map"

    map_obj.save(name + ".html")
    

