class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    l1 = length(source)
        
    ls1 = []
    for i in range(l1):
        ls1.append(source.data)
        source = source.next
        
    l2 = length(dest)
    ls2 = []
    for i in range(l2):
        ls2.append(dest.data)
        dest = dest.next
        
    one = source
    for index, value in enumerate(ls1[1:][::-1]):
        if index == 0:
            one = push(None, value)
        else:
            one = push(one, value)
            
    two = dest
    for index, value in enumerate(([ls1[0]] + ls2)[::-1]):
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