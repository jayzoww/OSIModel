class FindPath:
    def __init__(self):
        pass 
    def dijkstra(self, graph, src, dest, visited = [], distances = {}, previous = {}):
              
        if src == dest:
            #show shortest path
            path=[]
            prev=dest
            while prev != None:
                path[:0] = prev
                prev=previous.get(prev,None)
            print 'shortest path: ',path
            print 'cost:', distances[dest]
        else :     
            #first run, intialize cost to -
            if not visited: 
                distances[src]=0
            # visit the neighbors
            for neighbor in graph[src] :
                if neighbor not in visited:
                    new_distance = distances[src] + graph[src][neighbor]
                    if new_distance < distances.get(neighbor,float('inf')):
                        distances[neighbor] = new_distance
                        previous[neighbor] = src
            #mark as visited
            visited.append(src)
            #redo dijkstras with closest non visited as source
            unvisited = {}
            for i in graph:
                if i not in visited:
                    unvisited[i] = distances.get(i,float('inf'))        
            x = min(unvisited, key = unvisited.get)
            self.dijkstra(graph,x,dest,visited,distances,previous)
        


if __name__ == "__main__":

    graph = {
        'a': {'e': 2, 'b': 1},
        'b': {'a': 1, 'e': 2, 'd': 2},
        'c': {'e': 2, 'd': 7, 'f': 4},
        'd': {'b': 1, 'c': 11, 'f': 5},
        'e': {'a': 3, 'b': 4, 'c':8},
        'f': {'c': 4, 'd': 5}
        }

    fp = FindPath()
    fp.dijkstra(graph,'a','f')