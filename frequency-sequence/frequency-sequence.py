def freq_seq(s, sep):
    t = ""
    return sep.join([t + str(s.count(i)) for i in s])