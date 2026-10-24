from collections import deque
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
queue = deque([(start, [])])
visited = {start}
while queue:
    state, path = queue.popleft()
    if state == goal:
        for step in path + [state]:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
        break
    zero = state.index(0)
    r, c = divmod(zero, 3)
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            new = list(state)
            new[zero], new[j] = new[j], new[zero]
            new = tuple(new)
            if new not in visited:
                visited.add(new)
                queue.append((new, path + [new]))

                N = 8
board = [-1] * N

def safe(row, col):
    for r in range(row):
        if board[r] == col:
            return False
        if abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    for r in range(N):
        print(" ".join("Q" if board[r] == c else "." for c in range(N)))

        from collections import deque

start = (0, 0)
goal = 2
queue = deque([(start, [])])
visited = {start}

while queue:
    (a, b), path = queue.popleft()

    if a == goal or b == goal:
        for step in path + [(a, b)]:
            print(step)
        break

    states = [
        (4, b), (a, 3), (0, b), (a, 0),
        (a - min(a, 3 - b), b + min(a, 3 - b)),
        (a + min(b, 4 - a), b - min(b, 4 - a))
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append((state, path + [(a, b)]))

            from itertools import permutations

letters = "SENDMORY"

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    if d["S"] == 0 or d["M"] == 0:
        continue

    send = 1000*d["S"] + 100*d["E"] + 10*d["N"] + d["D"]
    more = 1000*d["M"] + 100*d["O"] + 10*d["R"] + d["E"]
    money = (10000*d["M"] + 1000*d["O"] +
             100*d["N"] + 10*d["E"] + d["Y"])

    if send + more == money:
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break

    from collections import deque

start = (3, 3, 1)  # missionaries, cannibals, boat on left
goal = (0, 0, 0)

moves = [(1, 0), (2, 0), (0, 1),
         (0, 2), (1, 1)]

def safe(m, c):
    return (0 <= m <= 3 and 0 <= c <= 3 and
            (m == 0 or m >= c) and
            (3-m == 0 or 3-m >= 3-c))

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()
    m, c, boat = state

    if state == goal:
        for step in path + [state]:
            print(step)
        break

    for dm, dc in moves:
        if boat == 1:
            nm, nc, nb = m-dm, c-dc, 0
        else:
            nm, nc, nb = m+dm, c+dc, 1

        new = (nm, nc, nb)

        if safe(nm, nc) and new not in visited:
            visited.add(new)
            queue.append((new, path + [new]))

            rooms = {"A": "Dirty", "B": "Dirty"}
position = "A"

while "Dirty" in rooms.values():
    print("Vacuum at", position)

    if rooms[position] == "Dirty":
        rooms[position] = "Clean"
        print(position, "cleaned")
    else:
        position = "B" if position == "A" else "A"

print("Final status:", rooms)

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def bfs(start):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

bfs("A")

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(neighbour)

dfs("A")

from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = [1, 2, 3]
best_cost = float("inf")
best_route = None

for route in permutations(cities):
    path = (0,) + route + (0,)
    cost = sum(graph[path[i]][path[i+1]]
               for i in range(len(path)-1))

    if cost < best_cost:
        best_cost = cost
        best_route = path

print("Best route:", best_route)
print("Minimum cost:", best_cost)

import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("E", 1)],
    "D": [("G", 5)],
    "E": [("G", 2)],
    "G": []
}

h = {"A": 5, "B": 4, "C": 3,
     "D": 4, "E": 2, "G": 0}

start, goal = "A", "G"
pq = [(h[start], 0, start, [start])]
best = {start: 0}

while pq:
    f, cost, node, path = heapq.heappop(pq)

    if node == goal:
        print("Path:", path)
        print("Cost:", cost)
        break

    if cost != best[node]:
        continue

    for neighbour, weight in graph[node]:
        new_cost = cost + weight

        if new_cost < best.get(neighbour, float("inf")):
            best[neighbour] = new_cost
            heapq.heappush(
                pq, (new_cost + h[neighbour],
                     new_cost, neighbour,
                     path + [neighbour])
            )

            


