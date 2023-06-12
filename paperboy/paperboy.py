def cheapest_quote(n):
    t=0
    if n==0:
        return 0
    else:
        q=int(n/40)
        r=n-q*40
        if r==0:
            return 3.85*q
        else:
            t=3.85*q+t
            q=int(r/20)
            r=r-q*20
            if r==0:
                return t+1.93*q
            else:
                t=1.93*q+t
                q=int(r/10)
                r=r-q*10
                if r==0:
                    return round(t+0.97*q,4)
                else:
                    t=0.97*q+t
                    q=int(r/5)
                    r=r-q*5
                    if r==0:
                        return round(t+0.49*q,4)
                    else:
                        t=0.49*q+t
                        print r
                        
                        return round(t+r*0.1,4)