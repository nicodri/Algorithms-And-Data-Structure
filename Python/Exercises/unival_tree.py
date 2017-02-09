from collections import deque


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_tree(root):
    print_response = ''
    if not root:
        return print_response
    current_layer = deque([root])
    next_layer = deque()
    while (current_layer):
        current_node = current_layer.popleft()
        if current_node:
            print_response += str(current_node.value) + ' '
            next_layer.append(current_node.left)
            next_layer.append(current_node.right)
        if not current_layer:
            print_response += ' \n'
            temp = current_layer
            current_layer = next_layer
            next_layer = temp
    return print_response


def countUnival(root):
    b, v, c = countUnival_helper(root)
    return c


def countUnival_helper(root):
    '''
    We use a bottom-up approach: when the call is done on a root, 
    the whole subtree it starts is processed.
    The tuple return is (bool, value, vount):
        bool: True if the current subtree is unival
        value: if current subtree is unival its value, ow None
        count: unival counts of the processed subtree
    '''
    # Case empty root
    if not root:
        return True, None, 0
    # Case leaf
    if not root.left and not root.right:
        return True, root.value, 1

    b_left, v_left, c_left = countUnival_helper(root.left)
    b_right, v_right, c_right = countUnival_helper(root.right)

    # Check if both subtree children are unival and if the root continues it
    # Case of only one child handled with the check for None
    if b_left and b_right and (v_left == v_right or not root.right or not root.left):
        return True, v_left, 1 + c_right + c_left
    # Case no unival sequence
    else:
        return False, None, c_right + c_left

if __name__ == '__main__':
    node0 = Node(5)
    node0_bis = Node(5, node0)
    node1 = Node(5, node0, node0)
    node2 = Node(5, node0, Node(4))
    node3 = Node(5, node1, node1)
    node4 = Node(5, node1, node2)
    node5 = Node(5, node2, node2)

    nodes = [node0, node0_bis, node1, node2, node3, node4, node5]

    for i, n in enumerate(nodes):
        print 'Test {}:'.format(i)
        print 'Unival subtrees count: {}'.format(countUnival(n))
        print 'Tree is:'
        print print_tree(n)
        
