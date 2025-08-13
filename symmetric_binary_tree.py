from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.traverse_list = []

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if (not root.left and root.right) or (root.left and not root.right):
            return False
        right_mirror = self.mirror(root.right)
        self.pre_order_traverse(right_mirror)
        right_mirror_traverse = self.traverse_list
        self.traverse_list = []
        self.pre_order_traverse(root.left)
        return self.traverse_list == right_mirror_traverse

    def mirror(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = root.left
        root.left = self.mirror(root.right)
        root.right = self.mirror(left)
        return root

    def pre_order_traverse(self, root: Optional[TreeNode]):
        if not root:
            return
        self.traverse_list.append(root.val)
        self.traverse_list.append(self.pre_order_traverse(root.left))
        self.traverse_list.append(self.pre_order_traverse(root.right))


def print_tree(root: Optional[TreeNode], level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


def test():

    s = Solution()

    left_root = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    left_root.left = node_2
    left_root.right = node_3
    node_2.left = node_4
    node_3.left = node_5

    right_root = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    right_root.left = node_2
    right_root.right = node_3
    node_2.left = node_4
    node_3.left = node_5

    print("Left tree:")
    print_tree(left_root)

    s.mirror(right_root)
    print("Right tree:")
    print_tree(right_root)

    node_0 = TreeNode(0)
    node_0.left = left_root
    node_0.right = right_root

    print(f'is symmetric: {s.isSymmetric(node_0)}')


if __name__ == '__main__':
    test()
