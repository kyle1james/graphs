import time
start_time = time.time()

def cheapest_path(matrix,start,goal):
    shortest_path = {}
    parent = {}
    unseenNodes = []
    path = []
    spelled = []

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            shortest_path[(x,y)] = float('Inf')
            unseenNodes.append((x, y))
    shortest_path[start] = 0

    while unseenNodes:
        minNode = None
        for x in unseenNodes:
            if minNode == None:
                minNode = x
            elif shortest_path[minNode] > shortest_path[x]:
                minNode = x

        if minNode == goal:
            path[(goal)] = (cx,cy)

        unseenNodes.remove(minNode)
        current_weight = shortest_path[minNode]
        x,y = minNode

        neighbors = [ (x+1, y), (x, y+1), (x-1,y), (x,y-1) ]
        real_neighbors = [(x,y) for (x,y) in neighbors if (x,y) in unseenNodes]
        for cx,cy in real_neighbors:
            weight = current_weight + matrix[cx][cy]
            if weight < shortest_path[(cx,cy)]:
                shortest_path[(cx,cy)] = min(weight, shortest_path[(cx,cy)])
                parent[(cx,cy)] = minNode



    currentNode = goal
    while currentNode != start:
        path.insert(0,currentNode)
        currentNode = parent[currentNode]


    px, py = start
    for x,y in path:
        if x > px:
            spelled.append('up')
        elif x < px:
            spelled.append('down')
        elif y < py:
            spelled.append('right')
        else:
            spelled.append('left')
        px,py = x,y

    return spelled








g= [
    [1,4,1,1],
    [1,9,1,0],
    [1,1,1,0]
    ]

h = [
    [1, 20, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 90, 90, 90, 90, 90, 90, 90, 90, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

m = [[1, 2, 4, 10, 1, 4, 8, 1, 9, 3, 6, 5, 7, 5, 10, 6, 5, 1, 8, 5, 10, 2, 5, 7, 5], [8, 1, 5, 9, 5, 4, 7, 0, 10, 2, 9, 6, 3, 7, 1, 1, 5, 5, 0, 5, 10, 9, 5, 1, 9], [10, 10, 6, 10, 3, 2, 5, 6, 6, 1, 3, 9, 4, 7, 4, 3, 7, 10, 0, 4, 1, 4, 5, 9, 10], [2, 8, 4, 10, 1, 8, 5, 6, 6, 10, 7, 5, 3, 9, 5, 2, 4, 1, 1, 0, 6, 3, 2, 4, 0], [7, 9, 6, 8, 2, 9, 6, 5, 7, 10, 0, 5, 1, 9, 8, 1, 6, 10, 4, 7, 10, 8, 9, 10, 7], [8, 3, 6, 10, 9, 10, 2, 0, 5, 1, 3, 2, 8, 3, 4, 10, 9, 0, 7, 2, 7, 3, 2, 9, 2], [2, 2, 7, 2, 9, 10, 4, 1, 4, 1, 3, 1, 0, 0, 1, 10, 3, 7, 8, 4, 10, 6, 5, 1, 0], [3, 10, 9, 5, 1, 0, 6, 0, 3, 9, 7, 5, 7, 8, 10, 2, 10, 10, 8, 9, 8, 1, 6, 5, 3], [7, 5, 5, 3, 0, 5, 4, 9, 10, 1, 3, 1, 4, 9, 6, 8, 6, 8, 10, 7, 1, 6, 1, 10, 7], [9, 6, 0, 6, 5, 6, 10, 3, 6, 4, 6, 9, 5, 10, 2, 5, 0, 7, 2, 3, 7, 9, 10, 5, 1], [7, 9, 5, 5, 8, 5, 4, 5, 0, 2, 10, 1, 9, 2, 0, 7, 10, 4, 8, 7, 9, 2, 0, 5, 9], [3, 0, 10, 4, 1, 9, 9, 3, 2, 0, 5, 6, 4, 6, 3, 6, 10, 10, 2, 10, 2, 8, 10, 8, 0], [4, 9, 6, 6, 6, 4, 8, 8, 6, 5, 2, 5, 7, 1, 8, 3, 5, 6, 2, 1, 8, 5, 6, 10, 3], [7, 1, 1, 9, 6, 10, 2, 6, 2, 2, 6, 6, 9, 3, 8, 9, 1, 8, 10, 8, 9, 3, 3, 5, 8], [6, 5, 4, 8, 2, 10, 10, 5, 8, 7, 4, 6, 5, 7, 2, 5, 3, 9, 1, 8, 2, 9, 9, 8, 9], [4, 7, 3, 8, 10, 1, 9, 6, 9, 1, 10, 7, 6, 9, 1, 4, 3, 1, 2, 1, 4, 5, 4, 6, 4], [5, 6, 8, 5, 5, 1, 10, 10, 4, 6, 9, 5, 0, 9, 4, 4, 8, 4, 2, 6, 5, 0, 8, 7, 0], [5, 10, 0, 7, 0, 5, 10, 5, 4, 8, 8, 1, 0, 0, 3, 7, 5, 9, 6, 9, 4, 5, 4, 4, 5], [6, 7, 0, 3, 8, 7, 9, 4, 8, 2, 7, 1, 7, 9, 5, 4, 1, 8, 7, 3, 0, 6, 8, 6, 3], [0, 4, 6, 3, 0, 3, 5, 1, 9, 7, 2, 3, 0, 7, 2, 9, 6, 8, 6, 9, 8, 9, 8, 6, 1]]

print(cheapest_path(m,(0,0), (19,23)))
print("--- %s seconds ---" % (time.time() - start_time))
