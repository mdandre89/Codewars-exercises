def maze_runner(maze, directions):
    maze2 = sum(maze,[])
    l = len(maze[0])
    x,y = maze2.index(2)%l, maze2.index(2)//l
    for i in directions:
        if i=="N":
            y-=1
        if i=="S":
            y+=1
        if i=="W":
            x-=1
        if i=="E":
            x+=1
        if x<0 or y<0:
            return "Dead"
        try:
            if maze[y][x]==1:
                return "Dead"
            elif maze[y][x]==3:
                return "Finish"
        except:
            return "Dead"
    return "Lost"