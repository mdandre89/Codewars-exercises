def sorted_insert(head, data):
    if not head:
        return Node(data)
    l = length(head)
        
    ls = []
    for i in range(l):
        ls.append(head.data)
        head = head.next

    new_ls = sorted(ls + [data])

    one = head
    for index, value in enumerate(new_ls[::-1]):
        if index == 0:
            one = push(None, value)
        else:
            one = push(one, value)
    return one
        
        
        
def length(node):
    if not node:
        return 0
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng