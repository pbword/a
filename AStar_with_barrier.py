class AStarGraph(object):
    def __init__(self):
        self.barriers = []
        t = int(input("Enter the number of barriers: "))
        for i in range(t):
            x = int(input("Enter row number for barrier point: "))
            y = int(input("Enter column number for barrier point: "))
            self.barriers.append((x, y))

    def heuristic(self, start, goal):
        D = 1
        D2 = 1
        dx = abs(start[0] - goal[0])
        dy = abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def get_vertex_neighbours(self, pos):
        n = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if 0 <= x2 <= 5 and 0 <= y2 <= 5:
                n.append((x2, y2))
        return n

    def move_cost(self, a, b):
        if b in self.barriers:
            return 100
        return 1


def print_grid(graph, path, start, end):
    print("\nGrid:")
    for row in range(6):
        for col in range(6):
            if (row, col) == start:
                print("S", end=" ")
            elif (row, col) == end:
                print("E", end=" ")
            elif (row, col) in graph.barriers:
                print("X", end=" ")
            elif (row, col) in path:
                print(".", end=" ")
            else:
                print(".", end=" ")
        print()


def AStarSearch(start, end, graph):
    G = {}
    F = {}  # Estimated movement cost of start to end

    G[start] = 0
    F[start] = graph.heuristic(start, end)

    closedVertices = set()
    openVertices = set([start])
    cameFrom = {}

    step = 1  # Step counter for debugging

    while len(openVertices) > 0:
        # Step 1: Get the vertex in the open list with the lowest F score
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        # Step 2: Check if we have reached the goal
        if current == end:
            # Retrace our route backward
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            print_grid(graph, path, start, end)
            return path, F[end]  # Done!

        openVertices.remove(current)
        closedVertices.add(current)

        # Debug output for each step
        print(f"Step {step}:")
        print(f"  Current node: {current}")
        print(f"  Open list: {openVertices}")
        print(f"  Closed list: {closedVertices}")

        # Print the grid with current state
        print_grid(graph, closedVertices, start, end)

        # Step 3: Explore neighbors
        for neighbour in graph.get_vertex_neighbours(current):
            if neighbour in closedVertices:
                continue

            candidateG = G[current] + graph.move_cost(current, neighbour)

            if neighbour not in openVertices:
                openVertices.add(neighbour)
            elif candidateG >= G.get(neighbour, float('inf')):
                continue

            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

            print(f"  Checking neighbor: {neighbour}")
            print(f"    G score: {G[neighbour]}")
            print(f"    H score: {H}")
            print(f"    F score: {F[neighbour]}")

        step += 1

    raise RuntimeError("A* failed to find a solution")


if __name__ == '__main__':
    graph = AStarGraph()
    s1 = int(input("Enter the row number for start point: "))
    s2 = int(input("Enter the column number for start point: "))
    g1 = int(input("Enter the row number for goal point: "))
    g2 = int(input("Enter the column number for goal point: "))
    result, cost = AStarSearch((s1, s2), (g1, g2), graph)
    print("Route:", result)
    print("Cost:", cost)

OUTPUT:Checking neighbor: (2, 3)
    G score: 1
    H score: 2
    F score: 3
  Checking neighbor: (0, 1)
    G score: 1
    H score: 3
    F score: 4
  Checking neighbor: (2, 1)
    G score: 1
    H score: 1
    F score: 2
  Checking neighbor: (0, 3)
    G score: 1
    H score: 3
    F score: 4
Step 2:
  Current node: (2, 1)
  Open list: {(0, 1), (1, 1), (0, 3), (2, 3), (0, 2), (2, 2), (1, 3)}
  Closed list: {(1, 2), (2, 1)}

Grid:
. . . . . . 
. . S . . . 
. . . . . . 
. E . . . . 
. . X . . . 
. . . . . . 
  Checking neighbor: (3, 1)
    G score: 2
    H score: 0
    F score: 2
  Checking neighbor: (2, 0)
    G score: 2
    H score: 1
    F score: 3
  Checking neighbor: (3, 2)
    G score: 2
    H score: 1
    F score: 3
  Checking neighbor: (1, 0)
    G score: 2
    H score: 2
    F score: 4
  Checking neighbor: (3, 0)
    G score: 2
    H score: 1
    F score: 3

Grid:
. . . . . . 
. . S . . . 
. . . . . . 
. E . . . . 
. . X . . . 
. . . . . . 
Route: [(1, 2), (2, 1), (3, 1)]
Cost: 2
