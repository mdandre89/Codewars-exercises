value = "A23456789TJQK"
seed = "cdhs"
def encode(cards):
    return sorted( value.index(card[0]) + 13*seed.index(card[1])  for card in cards)

def decode(cards):
    return sorted((value[cards%13] + seed[cards//13] for cards in cards), key=lambda x: (seed.index(x[1]), value.index(x[0]) ) )