def outed(meet, boss):
    l = (sum(list(meet.values()))+ (boss in meet)*meet[boss])/len(meet)
    if l > 5:
        return 'Nice Work Champ!'
    else:
        return 'Get Out Now!'