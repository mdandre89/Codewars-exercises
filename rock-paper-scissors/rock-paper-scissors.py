def rps(p1, p2):
    if p1==p2:
        return "Draw!"
    else:
        if p1=="rock":
            if p2=="scissors":
                return "Player 1 won!"
            else:
                return "Player 2 won!"
        elif p1=="scissors":
            if p2=="rock":
                return "Player 2 won!"
            else:
                return "Player 1 won!"
        else:
            if p2=="rock":
                return "Player 1 won!"
            else:
                return "Player 2 won!"
                