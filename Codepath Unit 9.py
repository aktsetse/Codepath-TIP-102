from collections import deque 

# class TreeNode():
#      def __init__(self, quantity, left=None, right=None):
#         self.val = quantity
#         self.left = left
#         self.right = right

# def merge_orders(order1, order2):
#     if not order1:
#         return order2
#     if not order2:
#         return order1
#     if not order1 and not order2:
#         return None
    
#     order1.val += order2.val


#     order1.left = merge_orders(order1.left, order2.left)
#     order1.right = merge_orders(order1.right, order2.right)
    
#     return order1

# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)
# def build_tree(values):
#   if not values:
#       return None

#   def get_key_value(item):
#       if isinstance(item, tuple):
#           return item[0], item[1]
#       else:
#           return None, item

#   key, value = get_key_value(values[0])
#   root = TreeNode(value, key)
#   queue = deque([root])
#   index = 1

#   while queue:
#       node = queue.popleft()
#       if index < len(values) and values[index] is not None:
#           left_key, left_value = get_key_value(values[index])
#           node.left = TreeNode(left_value, left_key)
#           queue.append(node.left)
#       index += 1
#       if index < len(values) and values[index] is not None:
#           right_key, right_value = get_key_value(values[index])
#           node.right = TreeNode(right_value, right_key)
#           queue.append(node.right)
#       index += 1

#   return root




# # Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))


class Puff():
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return []
    result = []
    queue = deque([design])
    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    print(result)



croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)
