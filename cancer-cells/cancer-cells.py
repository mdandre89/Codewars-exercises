import re
def cut_cancer_cells(organism):
    organism = re.sub(r'[a-z]?C[a-z]?|c', '', organism)
    return organism