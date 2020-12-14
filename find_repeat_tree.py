
class Tree():
    def __init__(self,data):
        self.data = data;
        self.left = None;
        self.right = None;
        self.li = [self];
        self.pnext = None;
        self.left_len = 0; #左子树的长度
        self.right_len = 0;#又子树的长度
        self.hash_value = '';

        
        
    def xianxu_add(self,node,height):
        #如果已经是最下层了，就不要加了
        if height == 0:
            return;
        
        #左子树没有满，并且左孩子是空的时候添加
        if self.left == None :
            self.left = node;
            self.left_len += 1;
            print("%d's left add node = %d,cnt=%d,left_len=%d" %(self.data,node.data,(1<<height)-1,self.left_len));
            return ;
        
        #左子树满了，才开始添加又子树
        if self.left_len >= ((1<<height) -1) and self.right == None:
            self.right = node;
            self.right_len += 1;
            print("%d's right add node = %d,cnt=%d,left_len=%d" %(self.data,node.data,(1<<height)-1,self.left_len));
            return ;
            
        #左子树还没有满，添加到左子树
        if self.left_len < ((1<<height)-1):
            self.left.xianxu_add(node,height-1);
            self.left_len += 1;
        #左子树满了，添加到右子树
        else :
            self.right.xianxu_add(node,height-1);
            self.right_len += 1;
    
    
    def tree_travel(self):
        #先序遍历

        print(self.data);
        if self.left is not None:
            self.left.tree_travel();
        #中序遍历
        #print(self.data);
        if self.right is not None:
            self.right.tree_travel();
        #后续遍历
        #print(self.data);  

        
    def find_repeat_tree(self,tree_list,find_list):
        if self.left != None:
            self.left.find_repeat_tree(tree_list,find_list);
        if self.right != None:
            self.right.find_repeat_tree(tree_list,find_list);
        
        left_data = 'left=';
        right_data = 'right=';
        if self.left != None:
            left_data += str(self.left.hash_value);
        
        if self.right != None:
            right_data += str(self.right.hash_value);
        
        self.hash_value = hash(left_data+right_data+str(self.data));
        if self.hash_value in tree_list.keys():
            find_list.append(self.data);
        tree_list[self.hash_value] = self;
        return ;
        
       
find_list = [];
tree_list = {};   
arr_list = [1,2,3,1,2,3];
tree = Tree(0);
for member in arr_list:
    node = Tree(member);
    tree.xianxu_add(node,2);

#tree.tree_travel();
tree.find_repeat_tree(tree_list,find_list);
print(find_list);

