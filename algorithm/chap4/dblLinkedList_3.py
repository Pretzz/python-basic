class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_B.prev = node_A
    node_D.next = node_E
    node_D.prev = node_B

'''Insert
'''
def insert_list(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data<=data:
        node_P = node_T
        node_T = node_T.next
    new_node.next = node_T
    new_node.prev = node_P
    node_P.next = new_node
    node_T.prev = new_node

'''Delete
'''
def delete_list(data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next

    if pre_node.data == data:
        node_A = pre_node.next
        del pre_node

    while next_node:
        if next_node.data == data:
            pre_node.next = next_node.next
            next_node.next.prev = pre_node
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next




def print_init():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()

if __name__ == "__main__":
    init_list()
    print_init()
    insert_list("C")
    print_init()
    delete_list("D")
    print_init()