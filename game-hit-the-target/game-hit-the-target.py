def solution(mtrx):
    for row in mtrx:
        line = ''.join(i for i in row if i!=' ')
        if '>x' in line or 'x<' in line:
            return True
    return False
            