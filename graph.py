from math import inf


class GraphModel():
    
    def __init__(self, edges: dict) -> None: 
        """
        Init graph as a dictionary
        edges = {
          "A": [("B", dist_AB),("C", dist_AC)],]
          "B": [("A", dist_AB)]
        }
        """
        self.graph = dict
        self.add_edges(edges)
        self.add_adjacent_nodes(edges)
    
    def add_edges(self, edges: dict) -> None:
        """
        Add edges to graph as dictionary of lists        
        """
        self.graph = edges
    
    def add_adjacent_nodes(self, edges: dict) -> None:
        """
        Create a dict with adjacent_nodes
        adjacent_nodes = {
          "A" = { "B": dist_AB, "C": dist_AC },
          "B" = { "C": dist_BC }
        }
        """
        self.adjacent_nodes = dict()
        
        for key in edges:
          self.adjacent_nodes[key] = dict()

          for x in edges[key]:
            self.adjacent_nodes[key][x[0]] = x[1]

    def get_edges(self) -> None:
        """
        Returns all graph's edges
        """
        edges = []
        for key in self.graph.keys():
            edges.append((key, self.graph[key]))
        return edges

    def get_nodes(self) -> list:
        """
        Returns all graph's nodes
        """
        return list(self.graph.keys())

    def get_neighbors(self) -> dict:
        """
        Returns all neighbors from graph
        """
        return self.graph

    def find_shortest_path(self, start: str, end: str) -> list:
        """
        Find shortest path using Dijkstra algorithm
        """
        path = [end] # path will be backwards in first moment
        total_dist = 0 # total distance traveled
        dijkstra_result = self.dijkstra(start=start)

        total_dist, node = dijkstra_result.get(end) # init path and set total distance by end point

        # path finder (end node to start node)
        while node != start:
          path.append(node)
          dist, node = dijkstra_result.get(node)
        
        path.append(start) # add start node at the end
        path.reverse() # correct path to be start point to end point

        return (path, total_dist)


    def dijkstra(self, start):
        """
        Dijkstra algorithm
        return = {
          node_A: (min_dist, min_neighbor),
          node_B: (min_dist, min_neighbor)
        }
        """
        nodes = self.get_nodes()
        distances = {}

        # init distances with infinite and 0 to start point
        for node_A in self.adjacent_nodes:
          for node_B in self.adjacent_nodes[node_A]:
            distances[node_A] = (inf, None)
            distances[node_B] = (inf, None)
        distances[start] = (0, start)

        # init not visited nodes list
        temporary_nodes = [n for n in nodes]

        # while temporary nodes is not empty
        while len(temporary_nodes) > 0:
            upper_bounds = {n: distances[n] for n in temporary_nodes}
            lower_bound = min(upper_bounds, key=lambda v: upper_bounds.get(v)[0])
            temporary_nodes.remove(lower_bound)
            for node, distance in self.adjacent_nodes[lower_bound].items():
                new_distance = (distances[lower_bound][0] + distance, lower_bound)
                distances[node] = min(distances[node], new_distance, key=lambda v:v[0])

        return distances


