
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
        self.pnext = None;
    
    def add_node(self,node):
        #本质是层序遍历。每次遍历到空就加一个成员。然后返回
        while True:
            cur_added_node = self.li[0];
            if cur_added_node.left == None:
                cur_added_node.left = node;
                self.li.append(cur_added_node.left);
                return;
            elif cur_added_node.right == None:
                cur_added_node.right = node;
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
        if self.pnext != None:
            print(self.pnext.data);
        if self.left is not None:
            self.left.tree_travel();
        if self.right is not None:
            self.right.tree_travel();
        
    def exchange_tree(self):
        if self.left == None and self.right == None:
            return;
        self.left,self.right = self.right,self.left;
        if self.left != None:
            self.left.exchange_tree();
            
        if self.right != None:
            self.right.exchange_tree();
        
    def give_next(self,left_node,right_node):
        if left_node == None or right_node == None:
            return ;
        left_node.pnext = right_node;
        self.give_next(left_node.left,left_node.right);
        self.give_next(right_node.left,right_node.right);
        self.give_next(left_node.right,right_node.left);
        
    def conenct(self):
        self.give_next(self.left,self.right);
    
    def la_zhi(self):
        if self.left != None:
            self.left.la_zhi();
        if self.right != None:
            self.right.la_zhi();
        
        tmp = self.right;
        #左子树变右子树
        self.right = self.left;
        #右子树追加到左子树最后
        tmp_left = self;
        while tmp_left.right !=  None:
            tmp_left = tmp_left.right;
        #找到了最后的那个，赋值
        tmp_left.right = tmp;
    
    def travel_lazhi(self):
        print(self.data);
        if self.right != None:
            self.right.travel_lazhi();
        
arr_list = [1,2,3,4,5,6];
tree = Tree(0);
for member in arr_list:
    node = Tree(member);
    tree.add_node(node);

#tree.tree_travel();
#tree.exchange_tree();
#print("after change");
#tree.tree_travel();
#tree.conenct();
#tree.tree_travel();

tree.la_zhi();
tree.travel_lazhi();