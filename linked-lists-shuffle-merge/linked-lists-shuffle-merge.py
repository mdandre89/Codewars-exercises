def shuffle_merge(first, second):
        
    l1 = length(first)
    ls1 = []
    for i in range(l1):
        ls1.append(first.data)
        first = first.next
    
    l2 = length(second)
    ls2 = []
    for i in range(l2):
        ls2.append(second.data)
        second = second.next
        
    one = None
    itera1 = iter(ls1)
    itera2 = iter(ls2)

    ls3 = []
    for i in range(l1 + l2):
        if i<2*min(l1, l2):
            if i%2==0:
                element = next(itera1)
            else:
                element = next(itera2)
        else:
            element = next(itera1) if l1 > l2 else next(itera2)
        ls3.append(element)

    one = None
    for index,value in enumerate(ls3[::-1]):
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

def push(head, data):
    if head:
        c =  Node(data)
        c.next = head
        return c
    else:
        return Node(data)