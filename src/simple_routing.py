"""
Simple Routing.

Loads the GTFS files into a data structure called Graph, which contains the
collection of bus stops and the available travels between them.
"""
import algorithm
import csv_parser
import models

def main():
    """
    Ejecuta un ejemplo
    """
    graph = models.Graph()
    stop_list = csv_parser.parse_stops()
    for stop in stop_list:
        graph.add_stop(stop)

    trip_list = csv_parser.parse_stop_times()
    for trip in trip_list:
        for stop, next_stop in zip(trip_list[trip], trip_list[trip][1:]):
            if next_stop not in stop.neighbors:
                graph.get_stop(stop).add_neighbor(next_stop)

    # This is an example:
    path, dist = algorithm.dijkstra(graph, "2317", "2327")
    print path
    print dist

if __name__ == "__main__":
    main()
