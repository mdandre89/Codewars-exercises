class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    if not head:
        return Node(data)
    l = length(head)
    
    if index> l:
        raise
        
    ls = []
    for i in range(l):
        ls.append(head.data)
        head = head.next

    new_ls = ls[0:index] +  [data] + ls[index:]

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