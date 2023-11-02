class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    l1 = length(head)
    if l1 <=1:
        raise
        
    ls1 = []
    for i in range(l1):
        ls1.append(head.data)
        head = head.next
        
    one = head
    for index, value in enumerate(ls1[0::2][::-1]):
        if index == 0:
            one = push(None, value)
        else:
            one = push(one, value)
            
    two = head
    for index, value in enumerate(ls1[1::2][::-1]):
        if index == 0:
            two = push(None, value)
        else:
            two = push(two, value)
        
        
    return Context(one, two)

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