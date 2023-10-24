def list_to_array(lst):
    t = []
    while lst.next:
        t.append(lst.value)
        lst = lst.next
    t.append(lst.value)
    return t