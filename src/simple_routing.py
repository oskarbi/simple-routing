"""
Simple Routing.

Loads the GTFS files into a data structure called Graph, which contains the
collection of bus stops and the available travels between them.
"""
import algorithm
import csv_parser
import models

class Router(object):

    def __init__(self):
        self.graph = None

    def load_graph(self):
        self.graph = models.Graph()
        stop_list = csv_parser.parse_stops()
        for stop in stop_list:
            self.graph.add_stop(stop)

        trip_list = csv_parser.parse_stop_times()
        for trip in trip_list:
            self.graph.add_trip(trip, trip_list[trip])
            for stop_id, next_stop_id in zip(trip_list[trip], trip_list[trip][1:]):
                if next_stop_id not in self.graph.get_stop(stop_id).neighbors:
                    self.graph.get_stop(stop_id).add_neighbor(next_stop_id)
                    self.graph.get_stop(stop_id).add_trip(trip)

    def run(self, origin, destination):
        return algorithm.dijkstra(self.graph, origin, destination)

def main():
    """Run an example."""
    router = Router()
    router.load_graph()
    path, dist = router.run("2327", "2317")
    print path
    print dist

if __name__ == "__main__":
    main()
