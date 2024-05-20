def crossover(chr1, chr2, index):
    return [chr1[:index]+chr2[index:], chr2[:index]+chr1[index:]]