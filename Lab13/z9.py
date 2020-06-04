class TreeNode:
    def __init__(self, left=-1, right=-1, data=-1):
        self.left=left
        self.right=right
        self.data=data

    def change_side_of_child(self):
        if self.left==-1:
            self.left=self.right
            self.right=-1
        if self.right==-1:
            self.right=self.left
            self.left=-1

    def print_node(self):
        d=str(self.data)
        if type(self.left)==TreeNode:
            l=str(self.left.data)
        else:
            l=str(self.left)
        if type(self.right)==TreeNode:
            r=str(self.right.data)
        else:
            r=str(self.right)
        print('('+d, l, r+')')


class BinaryTree:
    def __init__(self, tr, nodes):
        def find_node_by_data(tree_f, dt):
            for node_i in tree_f.storage:
                if node_i.data == dt:
                    return node_i
            return -1
        self.storage=[TreeNode() for i in range(len(tr))]
        for i in range(len(tr) - 1, -1, -1):
            self.storage[i].data = nodes[i]
            if len(tr[i])==1 and i==0:
                self.storage[i].left = self.storage[i+1]
                self.storage[i].right = -1
            elif len(tr[i])==1 and i!=0:
                self.storage[i].left=-1
                self.storage[i].right=-1
            elif len(tr[i])==2 and i!=0:
                self.storage[i].left = self.storage[i+1]
                self.storage[i].right = -1
            elif len(tr[i])==2 and i==0:
                self.storage[i].left = self.storage[i+1]
                self.storage[i].right=self.storage[i+2]
            else:
                self.storage[i].left = find_node_by_data(self,tr[i][1])
                self.storage[i].right = find_node_by_data(self,tr[i][2])

    def add_node(self, left, right, data):
        node=TreeNode(left,right, data)
        self.storage.append(node)

    def print_tree(self):
        for i in self.storage:
            i.print_node()


lst=[int(i) for i in input().split(' ')]
N=len(lst)
treelist=[[] for i in lst]
for i in range(1,N):
    treelist[i].append(lst[i-1])
for i in range(0,N-1):
    treelist[i].append(lst[i+1])
tree=BinaryTree(treelist, lst)
for i in range(0, N - 1):
    tree.storage[i].change_side_of_child()
    #по умолчанию дочерние вершины являются левыми, метод позволяет изменить их на правые
tree.print_tree()
print(tree.storage[0])