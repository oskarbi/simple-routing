import csv
from models import Stop, Graph

def parse_stops():
    stop_list = []
    with open("../gtfs/stops.txt") as stops_file:
        stops_csv = csv.reader(stops_file)
        stops_csv.next() # Skip CSV's header
        for stop_line in stops_csv:
            stop_id = stop_line[0]
            stop_name = stop_line[2]
            stop_lat = stop_line[4]
            stop_lon = stop_line[5]
            stop = Stop(stop_id, stop_name, stop_lat, stop_lon)
            stop_list.append(stop)
    return stop_list

def parse_stop_times():
    trip_list = {}
    with open("../gtfs/stop_times.txt") as stoptimes_file:
        stoptimes_csv = csv.reader(stoptimes_file)
        stoptimes_csv.next() # Skip CSV's header
        for stoptime_line in stoptimes_csv:
            trip_id = stoptime_line[0]
            stop_id = stoptime_line[3]
            stop_sequence = stoptime_line[4]
            if trip_id not in trip_list:
                # TODO: Tener en cuenta que el fichero puede estar desordenado
                # Habra que usar la secuencia para ordenar paradas
                trip_list[trip_id] = [stop_id]
            else:
                trip_list[trip_id].append(stop_id)
    return trip_list
