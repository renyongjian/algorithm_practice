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
                    




result = -1;
index = 0;
arr_list = [5,3,6,2,4,None,None,1];
add_index = 0;

tree_list = Tree(0);
#tree_list.cengxu_add(arr_list);
tree_list.xianxu_add(arr_list);
tree_list.xianxu_travel();
print("zhongxu");
tree_list.zhongxu_travel(1);
print(result);