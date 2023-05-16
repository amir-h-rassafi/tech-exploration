from cluster_drawer import GeoPoint
import random


class Ride:
    def __init__ (self, sourcePoint: GeoPoint, destinationPoint: GeoPoint):
        self.source = sourcePoint
        self.source.setColor('green')
        self.dest= destinationPoint
        self.dest.setColor('blue')

    def getSource(self) -> GeoPoint:
        return self.source

    def getDest(self) -> GeoPoint:
        return self.dest


def generate_random_ride(box) -> Ride:
    lat = random.uniform(box[0], box[1])
    lng = random.uniform(box[2], box[3])
    source = GeoPoint(lat, lng)
    lat = random.uniform(box[0], box[1])
    lng = random.uniform(box[2], box[3])
    dest = GeoPoint(lat, lng)
    return Ride(source, dest)