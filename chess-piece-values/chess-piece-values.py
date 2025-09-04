values = {
    'queen': 9,
    'rook': 5,
    'bishop': 3,
    'knight': 3,
    'pawn': 1,
    'king': 0,
}
import re
def pieces_value(arr, s):
    return sum(values[item] for item in re.findall(rf'{s[0]}-(\w+)', "\n".join(",".join(line) for line in arr)))