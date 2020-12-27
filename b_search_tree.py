class Tree():
    def __init__(self,data):
        self.data = data;
        self.left = None;
        self.right = None;
    def xianxu_travel(self):
        if self.data != None:
            print(self.data);
        if self.left != None:
            self.left.xianxu_travel();
        if self.right != None:
            self.right.xianxu_travel();
    
    def zhongxu_travel(self,k):
        global index,result;
        if self.left != None:
            self.left.zhongxu_travel(k);
        index += 1;
        if k == index:
            result = self.data;
        if self.data != None:
            print(self.data);
        
        if self.right != None:
            self.right.zhongxu_travel(k);
        
        return ;
    
    def select_nth(self,k):
        pass
    
    def xianxu_add(self,arr_list):
        global index;
        self.data = arr_list[index];
        index += 1;
        if index >= len(arr_list):
            return;
        
        if arr_list[index] != None:
            if self.left == None:
                self.left = Tree(0);
            print('左子树 添加 %d' %(arr_list[index]));
            self.left.xianxu_add(arr_list);
        else:
            index += 1;
        
        if index >= len(arr_list):
            return;
        if arr_list[index] != None:
            if self.right == None:
                self.right = Tree(0);
            print('右子树 添加 %d' %(arr_list[index]));
            self.right.xianxu_add(arr_list);
        else:
            index += 1;
        
        return;
        
    def cengxu_add(self,arr_list):
        self.data = arr_list[0];
        q = [];
        q.append(self);
        for data in arr_list[1:]:
            while True:
                cur_visit_node = q[0];
                if cur_visit_node.left == None:
                    cur_visit_node.left = Tree(0);
                    cur_visit_node.left.data = data;
                    q.append(cur_visit_node.left);
                    break;
                
                if cur_visit_node.right == None:
                    cur_visit_node.right = Tree(0);
                    cur_visit_node.right.data = data;
                    q.append(cur_visit_node.right);
                    break;
                
                q.pop(0);
                
                if len(q) == 0:
                    break;
                    
    def b_search_sum_tree(self):
        global sum_result;
        if self.right != None:
            self.right.b_search_sum_tree();
        
        if self.data != None:
            self.data += sum_result;
            sum_result = self.data;
    
        
        if self.left != None:
            self.left.b_search_sum_tree();
    
    def is_valid_b_search_tree_node(self,max_node,min_node):
        if self.data == None:
            return True;
        
        if max_node != None and max_node.data <= self.data:
            return False;
        if min_node != None and min_node.data >= self.data:
            return False;
        
        is_left_node_valid = True;
        is_right_node_valid = True;
        if self.left != None:
            is_left_node_valid = self.left.is_valid_b_search_tree_node(self,min_node);
        
        if self.right != None:
            is_right_node_valid = self.right.is_valid_b_search_tree_node(max_node,self);

        return  is_right_node_valid and is_left_node_valid
        
    def is_valid_b_search_tree(self):
        return self.is_valid_b_search_tree_node(None,None);
    
        
        
        

result = -1;
index = 0;
arr_list = [5,3,6,2,4,None,None,1];
add_index = 0;
sum_result = 0;

tree_list = Tree(0);
tree_list.cengxu_add(arr_list);
#tree_list.xianxu_add(arr_list);
#tree_list.xianxu_travel();
#print("zhongxu");
#tree_list.zhongxu_travel(1);
#print(result);
#print('累加树');
#tree_list.b_search_sum_tree();
#print('再次中序');
#tree_list.zhongxu_travel(1);
print(tree_list.is_valid_b_search_tree());
