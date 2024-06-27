import datetime
def get_start_time(schedules, duration):
    ls = sorted([i for j in schedules for i in j],key=lambda x: (datetime.datetime.strptime(x[0],'%H:%M').time(),datetime.datetime.strptime(x[1],'%H:%M').time()) )
    s = []
    for i in ls:
        if not s:
            s.append(i)
        else:
            t = s.pop()
            if compare(t[1],i[0]):
                if not compare(t[1],i[1]):
                    newt = [t[0],i[1]]
                    s.append(newt)
                else:
                    newt = [t[0],t[1]]
                    s.append(newt)                    
            else:
                s.append(t)
                s.append(i)
    if datetime.datetime.strptime('09:00','%H:%M') + datetime.timedelta(minutes=duration)<=datetime.datetime.strptime(s[0][0],'%H:%M'):
        return '09:00'
    for i,j in enumerate(s[:-1]):
        l = datetime.datetime.strptime(j[1],'%H:%M')
        m = l + datetime.timedelta(minutes=duration)
        if m <= datetime.datetime.strptime(s[i+1][0],'%H:%M'):
            return j[1]
    if datetime.datetime.strptime(s[-1][1],'%H:%M') + datetime.timedelta(minutes=duration)<=datetime.datetime.strptime('19:00','%H:%M'):
        return s[-1][1]
    return None
        
def compare(h1,h2):
    return datetime.datetime.strptime(h1,'%H:%M').time() >= datetime.datetime.strptime(h2,'%H:%M').time()