def gas_station(obj, cF, fC):
    ls = map(lambda x : (x,(60-cF)*obj[x]["price"]+2*obj[x]["price"]*obj[x]["distance"]*fC/100) if obj[x]["distance"]*fC/100 < cF else (None,0), obj)
    try:
        return min(filter(lambda x:x[1]>0,ls),key=lambda x: x[1])[0]
    except:
        return None