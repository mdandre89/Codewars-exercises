def reverse_complement(dna):
    new = ""
    dictio = {"T":"A","A":"T","C":"G","G":"C"}
    if dna =="":   
        return ''
    else:
        for i in dna[::-1]:
            if i not in ["T","A", "C","G"]:
                return "Invalid sequence"
            else:
                new = new + dictio[i]
    return new