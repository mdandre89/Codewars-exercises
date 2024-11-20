def distribute(nodes, workload):
    t = []
    s = iter(range(workload))
    for i in range(nodes):
        if i< workload%nodes:
            t.append([next(s) for j in range(workload//nodes+1)])
        else:
            t.append([next(s) for j in range(workload//nodes)])
    return t