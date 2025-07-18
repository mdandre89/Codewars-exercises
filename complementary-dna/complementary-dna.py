def DNA_strand(dna):
    dictio = {"A":"T", "G":"C","C":"G","T":"A"}
    return "".join([dictio[i] for i in dna])