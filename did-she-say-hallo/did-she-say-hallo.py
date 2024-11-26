def validate_hello(greetings):
    greetings=greetings.lower()
    greeting=["hello","ciao","salut","hallo","hola","ahoj","czesc"]
    i=0
    for a in greeting:
        if a in greetings:
            i=1
        else:
            pass
    if i==1:
        return True
    else:
        return False
        