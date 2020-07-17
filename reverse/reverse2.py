class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value, next_node=None)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node):
        # if nothing exists, do nothing, do not reverse
        
        
        if node is None:
            return 
        # when the next node is None, set the current node to head node
        # and that head nodes.next will point to this node called prev
        # previous is set to None

        if node.next_node is None:
            self.head = node

            
            node.next_node = None 
            return self.head  
       

        # reverse_list function is scrolling down the line, until it reaches the end
        # when it reaches the end, it sets the node before null equal to the head

        # new_node is a pointer , pointing to the nodes next node
        # nodes next node is equal to prev, which is a node        
        new_node = node.next_node.next_node 
        new_node = node.next_node 
        node.next_node = None 
       

        self.reverse_list(new_node, node)