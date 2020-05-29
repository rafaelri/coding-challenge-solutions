from avl import AVL
class RunningMedian():
    def __init__(self):
        self.tree = AVL()
        self.count = 0

    def add(self, val):
        self.count+=1
        self.tree.insert(val)
        if self.count % 2 == 1:
            return self.tree.root.key
        else:
            return (self.get_other_for_median() + self.tree.root.key)/2

            if not self.tree.root.right or (self.tree.root.left and self.tree.root.right.height < self.tree.root.left.height):
                return (self.tree.root.key + self.tree.root.left.key)/2
            else:
                return (self.tree.root.key + self.tree.root.right.key)/2
    
    def get_other_for_median(self):
        highest_left = self.get_highest_left(self.tree.root.left, 0)
        lowest_right = self.get_lowest_right(self.tree.root.right, 0)

        if not highest_left or (lowest_right and lowest_right[1] > highest_left[1]):
            return lowest_right[0]
        else:
            return highest_left[0]

    def get_highest_left(self, node, height):
        if not node and not height:
            return None
        if not node.right:
            return (node.key, height)
        else:
            return self.get_highest_left(node.right, height+1)

    def get_lowest_right(self, node, height):
        if not node and not height:
            return None
        if not node.left:
            return (node.key, height)
        else:
            return self.get_lowest_right(node.left, height+1)            