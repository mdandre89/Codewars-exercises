def pair_of_shoes(shoes):
    ls = [i[1] for i in shoes if i[0]==0]
    rs = [i[1] for i in shoes if i[0]==1]
    return all(x in ls for x in rs) and all(x in rs for x in ls)and len(ls)==len(rs) if len(shoes)>1 else False