import itertools

class DeliveryGraph:
    def __init__(self):
        self.locations = []
        self.distances = {}
        self.graph = {}

    def add_location(self, location):
        self.locations.append(location)
        self.graph[location] = {}

    def add_distance(self, from_location, to_location, distance):
        self.graph[from_location][to_location] = distance
        self.graph[to_location][from_location] = distance  

def calculate_route_distance(route, graph):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph.graph[route[i]][route[i+1]]
    return total_distance

def find_best_route(graph, start_location):
    
    locations = graph.locations
    locations.remove(start_location)
    
    best_route = None
    min_distance = float('inf')
    
    for perm in itertools.permutations(locations):
        route = [start_location] + list(perm)
        distance = calculate_route_distance(route, graph)
        
        if distance < min_distance:
            min_distance = distance
            best_route = route
    
    return best_route, min_distance

def take_input():
    graph = DeliveryGraph()

    num_locations = int(input("Enter the number of delivery locations: "))
    print(f"Enter {num_locations} delivery locations:")
    
    for i in range(num_locations):
        location = input(f"Enter delivery location {i + 1}: ")
        graph.add_location(location)

    print("Enter the distance matrix (distance between each pair of locations):")
    for i in range(num_locations):
        for j in range(i+1, num_locations):
            distance = int(input(f"Enter the distance between {graph.locations[i]} and {graph.locations[j]}: "))
            graph.add_distance(graph.locations[i], graph.locations[j], distance)

    start_location = input("Enter the starting location for the delivery path calculation: ")
    
    return graph, start_location


graph, start_location = take_input()

best_route, min_distance = find_best_route(graph, start_location)

print(f"The best route starting from {start_location} is: {' -> '.join(best_route)}")
print(f"Total distance: {min_distance}")
