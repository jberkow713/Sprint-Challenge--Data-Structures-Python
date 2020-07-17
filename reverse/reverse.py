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

    def reverse_list(self, node, prev):
        # if nothing exists, do nothing, do not reverse
        
        
        if node is None:
            return 
        # when the next node is None, set the current node to head node
        # and that head nodes.next will point to this node called prev
        # previous is set to None
        # but if prev is set to None, and is self.heads next node, then prev has to mean
        # opposite direction of next, as in not pointing normal route

        if node.next_node is None:
            self.head = node

            
            node.next_node = prev
            return self.head 
       

        #since prev means opposite direction of next, we can establish new variable called 
        #new_node, make it mean pointer of node, and set pointer of node to prev, meaning
        #new_node is pointing in opposite direction 

        # start of function       
        new_node = node.next_node
        # updating next node
        node.next_node = prev
        
        # reverse list is just scrolling through to find the end of the line, then labeling 
        #last element in that line as head
        # so when you call it recursively on this reverse direction, with node, its basically
        #heading opposite way from the head, down the line, swapping directions as it goes

        self.reverse_list(new_node, node)