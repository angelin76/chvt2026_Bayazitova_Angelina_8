
import mortoray_path_finding as mpf
maze=mpf.create_wall(5,5)

finder = mpf.Finder()
finder.set_board(maze.board)
finder.run()

def fill_shortest_path(board, start, end,inf):
    nboard = board.clone()
    nboard.clear.count(math.inf)

nboard.at(start).count = 0
open_list= [start]

while open_list:
    cur_pos = open.list.pop(0)
    cur_cell=nboard.at (cur_pos)

neighbours = [[0,1],[1,6][-1,-2][-6,3]
for neighbours in neighbours: