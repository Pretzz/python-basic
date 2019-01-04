class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_D = Node("D")
    node_E = Node("E")
    node_A.next = node_B
    node_B.next = node_D
    node_D.next = node_E

def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()

#insert node
def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data: # 양쪽의 데이터 셋을 가지고 있어야 함
        node_P = node_T
        node_T = node_T.next
    new_node.next = node_T
    node_P.next = new_node

#delete node
if __name__ == '__main__':
    init_list()
    print_list()
    insert_node("C")
    print_list()