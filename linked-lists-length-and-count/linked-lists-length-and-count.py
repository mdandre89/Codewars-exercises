class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    t = 0
    curr = node
    while curr:
        curr = curr.next
        t+=1
    return t
  
def count(node, data):
    c = 0
    curr = node
    while curr:
        t_data = curr.data
        curr = curr.next
        if t_data == data:
            c+=1
    return c