def how_much_coffee(events):
    count = 0
    dictio = {"cw":1,"dog":1,"cat":1,"movie":1,"MOVIE":2,"CW":2,"CAT":2,"DOG":2}
    for i in events:
        count += dictio.get(i,0)
        
    return count if count <=3 else 'You need extra sleep'