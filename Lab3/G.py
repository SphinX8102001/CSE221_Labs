def findPostOrder(inOrder,preOrder):
    if inOrder == [] or preOrder == []:
        return []
    
    root = preOrder[0]
    root_index = inOrder.index(root)
    left_in_order = inOrder[:root_index]
    right_in_order = inOrder[root_index+1:]
    size_of_left_in_order = len(left_in_order)
    size_of_right_in_order = len(right_in_order)
    left_pre_order = preOrder[1:size_of_left_in_order+1]
    right_pre_order = preOrder[size_of_left_in_order+1:]
    return findPostOrder(left_in_order,left_pre_order) + findPostOrder(right_in_order,right_pre_order) + [root]

inOrder = [4,2,5 ,1 ,3]
preOrder = [1, 2, 4, 5, 3]
print(findPostOrder(inOrder,preOrder))