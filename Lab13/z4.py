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


treelist=[[1,2],[0,3,4],[0,5,6],[1,7,8],[1,9,10],[2,11,12],[2,13,14],[3],[3],[4],[4],[5],[5],[6],[6]]
tree=BinaryTree(treelist, [i for i in range(0,15)])
leaves=0
for node in tree.storage:
    if node.left==-1 and node.right==-1:
        leaves+=1
print('Количество листьев:',leaves)