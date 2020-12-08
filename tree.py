
class Node():
    def __init__(self,number):
        self.number = number;
        self.left = None;
        self.right = None;
 

class Tree():
    def __init__(self,data):
        self.data = data;
        self.left = None;
        self.right = None;
        self.li = [self];
    
    def add_node(self,node):
        #本质是层序遍历。每次遍历到空就加一个成员。然后返回
        while True:
            cur_added_node = self.li[0];
            if cur_added_node.left == None:
                cur_added_node.left = node;
                print("add to left node=%d" %node.data);
                self.li.append(cur_added_node.left);
                return;
            elif cur_added_node.right == None:
                cur_added_node.right = node;
                print("add to right node=%d" %node.data);
                self.li.append(cur_added_node.right);
                self.li.pop(0);
                return ;
            else:
                return ;


    def tree_travel(self):
        if self.data == None:
            print("There is no member");
            return ;
        #先序遍历
        print(self.data);
        if self.left is not None:
            self.left.tree_travel();
        if self.right is not None:
            self.right.tree_travel();
        
        
        

arr_list = [1,2,3,4,5,6,7,8];
tree = Tree(0);
for member in arr_list:
    node = Tree(member);
    tree.add_node(node);
    
tree.tree_travel();