class Tree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    
def max_distance(tree: Tree) -> int:
    return max_distance_tree(tree)[0]

def max_distance_tree(tree: Tree, height=0) -> (int,int):
    if tree.left and tree.right:
        max_left, height_left = max_distance_tree(tree.left, height+1)
        max_right, height_right = max_distance_tree(tree.right, height+1)
        relative_height_left = height_left - height
        relative_height_right = height_right - height
        return (max(max_left,max_right, relative_height_left+relative_height_right),max(height_left, height_right))
    elif tree.left:
        max_left, height_left = max_distance_tree(tree.left, height+1)
        return (max(max_left, height_left),height_left)
    elif tree.right:
        max_right, height_right = max_distance_tree(tree.right, height+1)
        return (max(max_right, height_right),height_right)
    else:
        return (0, height)



def test_four_nodes_unbalanced():
    t = Tree()
    t.right = Tree()
    t.right.right = Tree()
    t.right.left = Tree()
    max_distance(t)
    
test_four_nodes_unbalanced()
