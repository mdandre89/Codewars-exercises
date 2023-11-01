class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    if not node:
        raise 
    l = length(node)
    if l > index>=0:
        for i in range(0, index):
            node = node.next
        return node
    else:
        raise

def length(node):
    if not node:
        return 0
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng