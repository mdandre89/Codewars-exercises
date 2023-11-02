class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    print(listA, listB)
    lA = length(listA)
    lB = length(listB)
    
    lsA = []
    for i in range(lA):
        lsA.append(listA.data)
        listA = listA.next
        
    lsB = []
    for i in range(lB):
        lsB.append(listB.data)
        listB = listB.next
        
    one = listA
    for index, value in enumerate((lsA+lsB)[::-1]):
        if index == 0:
            one = push(None, value)
        else:
            one = push(one, value)
    return one

def push(head, data):
    if head:
        c =  Node(data)
        c.next = head
        return c
    else:
        return Node(data)
        
def length(node):
    if not node:
        return 0
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng