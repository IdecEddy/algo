class Tree:
    def __init__(self, cargo, left=None, right=None):
            self.cargo = cargo
            self.left  = left
            self.right = right

def validate_tree(tree, lower, upper):
    if not tree: 
        return True 
    val = tree.cargo
    if val <= lower or val >= upper:
        return False
    if not validate_tree(tree.right, val, upper):
        return False
    if not validate_tree(tree.left, lower, val):
        return False
    return True 


tree = Tree(5 , Tree(1) , Tree(6 , Tree(4), Tree(7)))
if validate_tree(tree, float('-inf') , float('inf')) == False:
    print "this is not a vlaid tree", tree 
else:
    print "this is a valid tree", tree
tree = Tree(5 , Tree(1) , Tree(7 , Tree(6), Tree(8)))

if validate_tree(tree, float('-inf') , float('inf')) == False:
    print "this is not a vlaid tree", tree 
else:
    print "this is a valid tree", tree
