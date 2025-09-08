def chess_board_cell_color(cell1, cell2):
    leto= "ABCDEFGH"
    if(leto.index(cell1[0])-leto.index(cell2[0])+int(cell1[1])-int(cell2[1]) )%2:
        return False
    return True