def sort_the_inner_content(words):   
    t=""
    for i in words.split():    
        if len(i)>3:
            t +="".join([i[0]]+sorted(list(i[1:-1]),reverse=True)+[i[-1]]) + " " 
        else:
            t += i + " "
    return t.strip()