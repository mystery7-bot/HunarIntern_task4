def displayPathToPrincess(n, grid):
    
    # Find bot and princess positions
    for i in range(n):
        for j in range(n):
            
            if grid[i][j] == 'm':
                bot_row = i
                bot_col = j
                
            elif grid[i][j] == 'p':
                princess_row = i
                princess_col = j

    # Move vertically
    while bot_row > princess_row:
        print("UP")
        bot_row -= 1

    while bot_row < princess_row:
        print("DOWN")
        bot_row += 1

    # Move horizontally
    while bot_col > princess_col:
        print("LEFT")
        bot_col -= 1

    while bot_col < princess_col:
        print("RIGHT")
        bot_col += 1
        
n = int(input())

grid = []
for _ in range(n):
    grid.append(input().strip())

displayPathToPrincess(n, grid)