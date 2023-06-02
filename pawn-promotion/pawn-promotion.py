def promotion(board):
    megamerge = ''.join(''.join(i) for i in board)
    if 'K' not in megamerge or 'P' not in megamerge:
        return []
    if 'K' in board[7]:
        return ['queen', 'rook']
    index_p = megamerge.index('P')
    index_k = megamerge.index('K')
    if (index_k - index_p)%8==0:
        return ['queen', 'rook']
    if abs(index_p - index_k) in (6, 10, 15, 17) and index_p//8 - index_k//8<=2: 
        return ['knight']
    if abs(index_p%8 - index_k%8) == abs(index_p//8 - index_k//8):
        return ['queen', 'bishop']
    return []