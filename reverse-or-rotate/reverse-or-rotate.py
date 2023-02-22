def revrot(stg, sz):
    if sz <=0 or stg =="" or sz > len(stg):
        return ""
    ls = [stg[i:i+sz] for i in range(0,len(stg),sz) if len(stg[i:i+sz])==sz]    
    return "".join([j[::-1] if sum([int(z)**3 for z in j])%2==0 else j[1:]+j[0] for j in ls])     