class Node():

    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node 

root_node = Node(1)

prev_node = root_node
for i in range(2, 11):
    temp_node = Node(i)
    prev_node.next_node = temp_node
    prev_node = temp_node

def print_list(root):
    while root!=None:
        print(root.val)
        root = root.next_node

# print_list(root_node)

def get_list_size(root):
    size=0
    while(root!=None):
        size+=1
        root = root.next_node
    return size

def list_shuffle(root):
    if(root == None):
        return root

    odd = root
    even = root.next_node

    first_even = even

    while(1):
        
        if(odd==None or even==None or even.next_node==None):
            odd.next_node = first_even
            break
    
        odd.next_node = even.next_node
        odd = even.next_node

        if(odd.next_node == None):
            even.next_node = None
            odd.next_node = first_even
            break
        
        even.next_node = odd.next_node
        even = odd.next_node

# list_shuffle(root_node)
# print_list(root_node)
#detecting loops insisde the linked list

def loops_detection(root):

    if root==None:
        return None

    storage_set = set()

    storage_set.add(root)

    while root.next_node!=None:
        
        if root.next_node in storage_set:
            return root
        else:
            storage_set.add(root.next_node)
            root = root.next_node
    
    return None


# new_root = Node(1)
# new_root2 = Node(2)
# new_root3 = Node(3)
# new_root.next_node=new_root2
# new_root2.next_node=new_root3
# new_root3.next_node=new_root
# print(new_root3)
# #testing loop
# print(loops_detection(new_root))






