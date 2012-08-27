import math

class Stop(object):
    """Class representing a bus stop."""

    def __init__(self, stop_id, stop_name, stop_lat, stop_lon):
        self.stop_id = stop_id
        self.name = stop_name
        self.lat = stop_lat
        self.lon = stop_lon
        self.neighbors = []

    def add_neighbor(self, stop):
        """Add a stop_id as this stop's neighbor."""
        self.neighbors.append(stop)

    def get_neighbors(self):
        """Return the list of this stop's neighbors."""
        return self.neighbors

    def get_distance(self, stop):
        """Return the euclidean distance between two nodes."""
        return math.sqrt((float(self.lat) - float(stop.lat)) ** 2
                        + (float(self.lon) - float(stop.lon)) ** 2)

    def get_walking_time(self, stop):
        """Return the aproximate time (in seconds) necessary to walk
        from a stop to another.
        """
        avg_speed = 1.4 # m/s
        time_walking = self.get_distance(stop) / avg_speed
        return time_walking

    def get_weight(self, stop):
        """Return the weight of the path between this stop and another."""
        return self.get_walking_time(stop)

class Graph(object):
    """Class containing a list of bus stops and the relations between them."""

    def __init__(self):
        self.stops = {}
        self.trips = {}

    def add_stop(self, stop):
        """Add a stop to the graph."""
        if stop.stop_id in self.stops:
            return # Stop already added
        self.stops[stop.stop_id] = stop

    def get_stop(self, stop_id):
        """Return the stop object for a given stop_id."""
        return self.stops[stop_id]

    def get_stops(self):
        """Return the list of stop_ids in the graph."""
        return self.stops.keys()

    def add_trip(self, trip):
        pass
