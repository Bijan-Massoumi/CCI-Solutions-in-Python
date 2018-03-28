import random as rand
from collections import defaultdict
import string

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

    def add_by_node(self,node):
        if self.num_elem == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node

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

    #problem 2.5
    @staticmethod
    def sum_lists(lst1,lst2):
        def get_val(node,is_forward,accu): #pass head or tai
            if node != None and is_forward:
                accu.append(node.data)
                return get_val(node.prev,True,accu)
            elif node != None and not is_forward:
                accu.append(node.data)
                return get_val(node.next,False,accu)
            else:
                print(accu)
                return int("".join(str(x) for x in accu))

        lft_int = get_val(lst1.head,True,[])
        rht_int = get_val(lst2.head,True, [])
        return lft_int + rht_int

    #problem 2.6
    def palindrone(self):
        def traverse(front, back, loop_pass, size):
            if front != back and loop_pass <= size/2:
                if front.data != back.data:
                    return False
                else:
                    return traverse(front.next,back.prev,loop_pass+1,size)
            else:
                return True

        return traverse(self.head,self.tail,1,self.num_elem)


    def get_elems(self):
        def traverse(node,accu):
            if node != None:
                accu.append(node.data)
                return traverse(node.next,accu)
            else:
                return accu
        return traverse(self.tail,[])

    #problem 2.7
    def loop_detection(self):
        def traverse(node,cache):
            if node != None and node not in cache: #the hunt goes on
                cache.append(node)
                return traverse(node.next,cache)
            elif node!= None and node in cache:
                return node #the sucker
            else:
                return None #no loop
        return traverse(self.tail,[])



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
        self.num_elem += 1

    def get_list(self):
        def traverse(node,accu):
            if node != None:
                accu.append(node.data)
                return traverse(node.next,accu)
            else:
                return accu
        return traverse(self.tail,[])

    #problem 2.2
    def kth_last(self,k):
        def traverse(node,accu,goal):
            if node != None:
                if accu == goal:
                    return node.data
                else:
                    return traverse(node.next, accu+1, goal)
        if k > self.num_elem:
            return self.tail.data
        else:
            return traverse(self.tail,0,self.num_elem-k)

    #problem 2.3
    def delete(self,del_node):
        def traverse(prev_node,curr_node,del_node):
            if curr_node != None:
                if curr_node == del_node:
                    if prev_node != None:
                        prev_node.next = curr_node.next
                    else: #indicates beginning of traversal
                        self.tail = curr_node.next
                else:
                    traverse(curr_node, curr_node.next, del_node)
        traverse(None,self.tail,del_node)

    #problem 2.4
    def partition(self,key):
        def traverse(node,key,lower_list,upper_list):
            if node != None:
                if node.data < key:
                    lower_list.push_front(node.data)
                else:
                    upper_list.push_front(node.data)
                return traverse(node.next,key,lower_list,upper_list)
            else:
                lower_list.head.next = upper_list.tail
                return lower_list
        return traverse(self.tail,key,Single_Linked(),Single_Linked())

    #problem 2.8
    @staticmethod
    def intersection(lst1,ls2):
        pass

def populate_list(list,k):
    for _ in range(k):
        list.push_front(rand.randint(1,6))

def load_pal(lst,correct):
    if correct:
        for i in "tacocat":
            lst.push_front(i)
    else:
        for i in range(rand.randint(5,8)):
            lst.push_front(rand.choice(string.ascii_letters))


if __name__ == "__main__":
    love = Doubly_Linked()
    loop_node = Double_Node(3)
    love.push_front(5)
    love.add_by_node(loop_node)
    love.push_front(7)
    love.add_by_node(loop_node)
    print(love.loop_detection() == loop_node)





