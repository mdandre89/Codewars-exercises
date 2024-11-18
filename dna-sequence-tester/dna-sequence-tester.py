dictio = {'G':'C','C':'G','A':'T','T':'A'}
def check_DNA(seq1, seq2):
    s = ''
    if len(seq1) >= len(seq2) :
        s = seq2
        base = seq1
    else:
        s = seq1
        base = seq2
    c = ''.join([dictio[i] for i in s])
    return c in base or c[::-1] in base