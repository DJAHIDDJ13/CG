import heapq
from collections import deque

# Parse input
w = int(input())
h = int(input())
m = [[] for _ in  range(h)]
sx, sy = -1, -1
ex, ey = -1, -1
start_conditions = [('>', 0, 'x'), ('<', w-1, 'x'), ('v', 0, 'y'), ('^', h-1, 'y')]
end_conditions = [('<', 0, 'x'), ('>', w-1, 'x'), ('^', 0, 'y'), ('v', h-1, 'y')]
for y in range(h):
    ext = input()
    for x, c in enumerate(ext):
        if any((cs , vs) == (c, x if rs == 'x' else y) for cs, vs, rs in start_conditions):
            sx, sy = x, y
        if any((cs , vs) == (c, x if rs == 'x' else y) for cs, vs, rs in end_conditions):
            ex, ey = x, y
        m[y].append(c)

# Check if coordinates are within the grid
def is_in_range(x, y):
    return 0 <= x < w and 0 <= y < h

# Build graph of warrior's possible moves
def build_warrior_graph(m, start):
    q = [start]
    g = {}
    neigh = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    seen = []
    while len(q) > 0:
        x, y = q.pop()
        if (x,y) in seen:
            continue
        seen.append((x, y))
        for dx, dy in neigh:
            nx, ny = x + dx, y + dy
            if is_in_range(nx, ny):
                if m[ny][nx] != '#':
                    if (x, y) not in g:
                        g[(x, y)]=[]
                    g[(x, y)].append((nx, ny))
                    q.append((nx, ny))
    return g

def build_dwarf_graph(m, start):
    q = deque([start]) # we need a queue for this one
    g = {}
    neigh = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    seen = []
    while len(q) > 0:
        x, y = q.popleft() 
        if (x, y) in seen:
            continue
        seen.append((x, y))
        for dx, dy in neigh:
            nx, ny = x + dx, y + dy
            if is_in_range(nx, ny):
                if m[ny][nx] != '#':
                    if (nx, ny) not in seen:
                        q.append((nx, ny))
                        if (x, y) not in g:
                            g[(x, y)] = []
                        g[(x, y)].append((nx, ny))
                elif m[ny][nx] == '#':
                    # Check if wall thickness is only 1 cell
                    if (is_in_range(nx+dx, ny+dy) and m[ny+dy][nx+dx] != "#"):
                        if (nx, ny) not in seen:
                            q.append((nx, ny))
                            if (x, y) not in g:
                                g[(x, y)] = []
                            g[(x, y)].append((nx, ny))

    return g

def build_elf_graph(m, start):
    q = [start]
    g = {}
    neigh = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    seen = []
    while len(q) > 0:
        x, y = q.pop()
        if (x,y) in seen:
            continue
        seen.append((x, y))
        for dx, dy in neigh:
            nx, ny = x + dx, y + dy
            if is_in_range(nx, ny):
                if m[ny][nx] != '#':
                    if (x, y) not in g:
                        g[(x, y)]=[]
                    g[(x, y)].append((nx, ny))
                    q.append((nx, ny))
    return g

def build_mage_graph(m, start):
    q = [start]
    g = {}
    neigh = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    seen = []
    while len(q) > 0:
        x, y = q.pop()
        if (x, y) in seen:
            continue
        seen.append((x, y))

        # Check all cells in straight line in the 4 direction
        for dx, dy in neigh:
            nx, ny = x + dx, y + dy
            while is_in_range(nx, ny) and m[ny][nx] != '#':
                if (nx, ny) not in seen:
                    if (x, y) not in g:
                        g[(x, y)] = []
                    g[(x, y)].append((nx, ny))
                    q.append((nx, ny))
            
                nx += dx
                ny += dy

    return g

def shortest_path(g, start, end):
    # Create a priority queue to store the nodes to visit
    queue = [(0, start)]
    # Keep track of the distance to each node from the start node
    distances = {start: 0}
    man_distances = {start: 1}
    # Keep track of the previous node in the path
    previous = {start: None}
    while queue:
        # Get the node with the smallest distance from the queue
        dist, current = heapq.heappop(queue)
        # If we've reached the end node, we can construct the path
        if current == end:
            path = [current]
            while previous[current] is not None:
                current = previous[current]
                path.append(current)
            return path[::-1]
        # Otherwise, update the distances and previous node for each neighbor
        for neighbor in g.get(current, []):
            cost = dist + 1
            # manhattan distance between the two, this acts as a tie breaker 
            # since we want to prioritize straight paths over diagonal ones
            man_cost = abs(current[0] - neighbor[0]) + abs(current[1] - neighbor[1]) 
            if neighbor not in distances or (cost, man_cost) < (distances[neighbor], man_distances[neighbor]):
                distances[neighbor] = cost
                man_distances[neighbor] = man_cost
                previous[neighbor] = current
                heapq.heappush(queue, (cost, neighbor))
    # If we didn't find a path, return None
    return None

def print_path_on_map(path, m):
    # Create a copy of the map so that the original map is not modified
    new_map = [row.copy() for row in m]
    for i in range(1, len(path)):
        x1, y1 = path[i-1]
        x2, y2 = path[i]
        dx, dy = x2 - x1, y2 - y1
        if abs(dx) == 1 and abs(dy) == 1:
            new_map[y1][x1] = 'o'  # diagonal
        elif dx < 0:
            new_map[y1][x1] = '<'  # left
        elif dx > 0:
            new_map[y1][x1] = '>'  # right
        elif dy < 0:
            new_map[y1][x1] = '^'  # up
        elif dy > 0:
            new_map[y1][x1] = 'v'  # down
    return new_map

warrior_g = build_warrior_graph(m, (sx, sy))
elf_g = build_elf_graph(m, (sx, sy))
mage_g = build_mage_graph(m, (sx, sy))
dwarf_g = build_dwarf_graph(m, (sx, sy))

all_graphs = [("WARRIOR", 2, warrior_g),
             ("DWARF", 3, dwarf_g),
             ("ELF", 4, elf_g),
             ("MAGE", 5, mage_g)
             ]
all_paths = [(n, c, shortest_path(g, (sx, sy), (ex, ey))) for n, c, g in all_graphs]
# filter None paths
all_paths = filter(lambda x:x[2] is not None, all_paths)
name, move_cost, best_path = min(all_paths, key=lambda x:x[1] * len(x[2]))

print(f"{name} {len(best_path) * move_cost}")
print(*map(''.join, print_path_on_map(best_path, m)), sep="\n")
