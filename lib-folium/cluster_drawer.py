import folium
from typing import List

class GeoPoint:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.name = None
        self.color = 'blue'

    def setColor(self, color: str):
        self.color = color

    def getColor(self):
        return self.color

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

    def getDistance(self, point) -> float:
        return ((self.getLat() - point.getLat())**2 + (self.getLng() - point.getLng())**2)**0.5
    
    def getCenter(self, point):
        return GeoPoint((self.getLat() + point.getLat())/2, (self.getLng() + point.getLng())/2)


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
    

def drawClusters(clusters: List[Cluster], map_obj: folium.Map, name = None):
    for cluster in clusters:
        for point in cluster.getPoints():
            folium.Marker(location=point.toTuple() , icon=folium.Icon(color=point.getColor())).add_to(map_obj)
        
        polyLine = []
        for point in cluster.getPoints():
            polyLine.append(point.toTuple())
            polyLine.append(cluster.getCenter().toTuple())

        folium.PolyLine(locations=polyLine, color="blue", weight=2.5, opacity=1).add_to(map_obj)

    if name is None:
        name = "map"

    map_obj.save(name + ".html")
    

