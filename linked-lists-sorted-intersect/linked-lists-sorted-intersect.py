class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
def sorted_intersect(first, second):
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
    for index,value in enumerate(sorted(list(set(ls1) & set(ls2)))[::-1]):
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