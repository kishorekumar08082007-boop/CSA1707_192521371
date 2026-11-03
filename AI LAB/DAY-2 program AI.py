colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

color_map = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if color_map.get(neighbor) == color:
            return False
    return True

def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            color_map[region] = color

            if solve(regions[1:]):
                return True

            del color_map[region]

    return False

if solve(list(graph.keys())):
    print("Map Coloring Solution:")
    for region, color in color_map.items():
        print(region, ":", color)
else:
    print("No solution found")

    board = [' ' for i in range(9)]

def display():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def check_win(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

player = 'X'

for turn in range(9):
    display()
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position! Try again.")
        continue

    board[pos] = player

    if check_win(player):
        display()
        print(player, "Wins!")
        break

    player = 'O' if player == 'X' else 'X'

else:
    display()
    print("Match Draw!")
