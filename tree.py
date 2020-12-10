
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
        self.left_len = 0; #左子树的长度
        self.right_len = 0;#又子树的长度
    
    def add_node(self,node):
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

    #这样写，是每次添加节点都添加到数量较少的子树上，和上一种不同
    def add_node_by_digui(self,node):
        #如果发现子节点有空的，就添加
        if self.left_len == 0 :
            self.left = node;
            self.left_len += 1;
            return ;
        if self.right_len == 0 :
            self.right = node;
            self.right_len += 1;
            return ;
            
        #子节点没空，就把新节点加到数量少的那子棵树上
        if self.left_len <= self.right_len:
            self.left.add_node_by_digui(node);
            self.left_len += 1;
        else :
            self.right.add_node_by_digui(node);
            self.right_len += 1;
        
    def cengxu_add_node(self,node):
        #本质是层序遍历。每次遍历到空就加一个成员。然后返回
        q = [self];
        cur_visit_node = q[0];
        while len(q)>0:
            if cur_visit_node.left != None:
                q.append(cur_visit_node.left);
            
            if cur_visit_node.right != None:
                q.append(cur_visit_node.right)
            
            #父节点的两个子节点已经遍历完毕，弹出父节点
            q.pop(0);
            
            #更新当前要访问的节点
            if len(q)>0:
                cur_visit_node = q[0];
            else:
                #已经没有要访问的节点了，说明当前访问的已经是最后一个节点了，正是我们要添加新节点的位置
                #如果左子树为空，加到左边，左子树不为空，右子树为空，就加到右边
                if cur_visit_node.left == None:
                    cur_visit_node.left = node;
                else:
                    cur_visit_node.right = node;

    def tree_travel_cengxu(self):
        q = [self];
        cur_visit_node = q[0];
        #访问第一个节点
        print(cur_visit_node.data);
        while len(q)>0:
            
            if cur_visit_node.left != None:
                print(cur_visit_node.left.data);
                q.append(cur_visit_node.left);
            
            if cur_visit_node.right != None:
                print(cur_visit_node.right.data);
                q.append(cur_visit_node.right)
            
            #父节点的两个子节点已经遍历完毕，弹出父节点
            q.pop(0);
            
            #更新当前要访问的节点
            if len(q)>0:
                cur_visit_node = q[0];
    
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
    
    def zhognxu_travel(self):
        if self.left is not None:
            self.left.zhognxu_travel();
        #中序遍历
        print(self.data);
        if self.right is not None:
            self.right.zhognxu_travel();
        
    def houxu_travel(self):
        if self.left is not None:
            self.left.houxu_travel();        
        if self.right is not None:
            self.right.houxu_travel();
        print(self.data);    
        
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
    
    def create_tree(self,xianxu_list,index,zhongxu_list,list_len):
        if index >= len(xianxu_list) or list_len == 0:
            return;
        zhongxu_left_list = [];
        zhongxu_right_list = [];
        data = xianxu_list[index];
        data_index = zhongxu_list.index(data);
        zhongxu_left_list = zhongxu_list[:data_index];
        zhongxu_right_list = zhongxu_list[data_index+1:];
        if len(zhongxu_left_list) == 0:
            self.left = None;
            print("left is none");
            return;
        else:
            self.left = Tree(xianxu_list[index+1]);
            print("left add %d" %(xianxu_list[index+1]));
            
        if len(zhongxu_right_list) == 0:
            self.right = None;
            print("right is none");         
            return;
        else:
            for i in xianxu_list:
                if i in zhongxu_right_list:
                    break;
            self.right = Tree(i);
            print("right add %d" %(self.right.data));

        self.data = data;
        right_index = xianxu_list.index(self.right.data);
        self.left.create_tree(xianxu_list,index+1,zhongxu_left_list,len(zhongxu_left_list));
        self.right.create_tree(xianxu_list,right_index,zhongxu_right_list,len(zhongxu_right_list));
        pass
        

def constuct_tree(xianxu_list,zhongxu_list):
    if len(xianxu_list) == 0 or len(zhongxu_list) == 0:
        return None;
    #先把中序列表分开
    tree = Tree(xianxu_list[0]);
    list_len = len(xianxu_list);
    tree.create_tree(xianxu_list,0,zhongxu_list,list_len);
    return tree;
    
arr_list = [1,2,3,4,5,6];
tree = Tree(0);
for member in arr_list:
    node = Tree(member);
    #tree.xianxu_add(node,2);
    



xianxu_list = [0,1,2,3,4,5,6];
#zhognxu_list = [1,2,3,0,4,5,6];
zhongxu_list = [2,1,3,0,5,4,6];
tree = constuct_tree(xianxu_list,zhongxu_list);
tree.tree_travel();
print("中序:");
tree.zhognxu_travel();


#tree.exchange_tree();
#print("after change");
#tree.tree_travel();
#tree.conenct();
#tree.tree_travel();
#tree.cengxu_add_node(node);
#tree.tree_travel_cengxu();
#tree.la_zhi();
#tree.travel_lazhi();
