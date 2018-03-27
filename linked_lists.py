
class Double_Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data

class Doubly_Linked:


    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elem = 0

    def push_front(self,val):
        new_node = Double_Node(val)
        if self.num_elem == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head.next = new_node
            new_node.prev = self.head
            self.head = new_node
        self.num_elem += 1

    def push_back(self,val):
        new_node = Double_Node(val)
        if self.num_elem == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.prev = new_node
            new_node.next = self.tail
            self.tail = new_node
        self.num_elem += 1

    #problem 2.1
    def remove_dups(self):
        def traverse_and_rm(node,val):
            if node != None:
                if node.data == val:
                    if node.next != None:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                    else:
                        node.prev.next = None
                traverse_and_rm(node.next,val)

        curr_node = self.tail
        while curr_node != None:
            traverse_and_rm(curr_node.next, curr_node.data)
            curr_node = curr_node.next

    def print_list(self):
        def traverse(node):
            if node != None:
                print(node.data)
                traverse(node.next)
        traverse(self.tail)



class Single_Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_Linked:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elem = 0

    def push_front(self,data):
        new_node = Single_Node(data)
        if self.num_elem > 0:
            self.head.next = new_node
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def print_list(self):
        def traverse(node):
            if node != None:
                print(node.data)
                traverse(node.next)
        traverse(self.tail)



if __name__ == "__main__":
    love = Doubly_Linked()
    love.push_front(5)
    love.push_front(5)
    love.push_front(5)
    love.push_front(7)
    love.push_front(7)
    love.push_front(5)
    love.push_front(5)
    love.push_front(6)
    love.push_front(7)
    love.push_front(8)
    love.push_back(9)
    love.push_back(9)
    love.remove_dups()
    love.print_list()

