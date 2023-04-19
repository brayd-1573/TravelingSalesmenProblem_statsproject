import itertools
import time


def distance(city1, city2):
    # calculate the Euclidean distance between two cities
    return ((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2) ** 0.5



def tsp_recursive(cities):
    # generate all possible permutations of the cities
    permutations = itertools.permutations(cities)

    shortest_distance = float('inf')
    shortest_route = None

    def tsp_helper(route, visited_cities):
        nonlocal shortest_distance, shortest_route

        if len(visited_cities) == len(cities):
            # calculate the total distance of the current route
            total_distance = 0
            for i in range(len(route)-1):
                total_distance += distance(route[i], route[i+1])
            # add the distance from the last city to the first city
            total_distance += distance(route[-1], route[0])
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_route = route
        else:
            for city in cities:
                if city not in visited_cities:
                    tsp_helper(route + (city,), visited_cities + (city,))

    start_time = time.time()
    for route in permutations:
        tsp_helper((route[0],), (route[0],))
        
    end_time = time.time()

    print("Shortest route:", shortest_route)
    print("Shortest distance:", shortest_distance)
    print("Recursive ime taken:", end_time - start_time)



def tsp_iterative(cities):
    # generate all possible permutations of the cities
    permutations = itertools.permutations(cities)

    shortest_distance = float('inf')
    shortest_route = None

    start_time = time.time()
    for route in permutations:
        total_distance = 0
        for i in range(len(route)-1):
            total_distance += distance(route[i], route[i+1])
        # add the distance from the last city to the first city
        total_distance += distance(route[-1], route[0])
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_route = route
        
    end_time = time.time()

    print("Shortest route:", shortest_route)
    print("Shortest distance:", shortest_distance)
    print("Iterative Time taken:", end_time - start_time)


# example usage
cities = [(0,0), (1,2), (3,1), (2,4), (5,3), (4,6), (7,4), (6,8), (9,5), (8,10)]
tsp_recursive(cities)
tsp_iterative(cities)
