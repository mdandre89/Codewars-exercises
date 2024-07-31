def presentation_agenda(dictio):
    ls = [i for j in dictio for i in j['dest'] ]
    for i in dictio:
        i['dest'] = [i for i in i['dest'] if ls.count(i)<=1]
    return list(filter(lambda x: x['dest']!= [], dictio))