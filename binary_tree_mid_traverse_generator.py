import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root: Node):
        self.root = root
        self.traverse_list = []

    def insert(self, node_to_insert: Node):
        curr_root = self.root

        while True:
            if node_to_insert.value < curr_root.value:
                if curr_root.left:
                    curr_root = curr_root.left
                    continue
                else:
                    curr_root.left = node_to_insert
                    break
            else:
                if curr_root.right:
                    curr_root = curr_root.right
                    continue
                else:
                    curr_root.right = node_to_insert
                    break

    def purge_traverse_result(self):
        self.traverse_list.clear()

    def get_traverse_result(self) -> list:
        return self.traverse_list

    def mid_order_traverse(self, root: Node):
        if not root:
            return
        else:
            if root.left:
                self.mid_order_traverse(root.left)

            self.traverse_list.append(root.value)

            if root.right:
                self.mid_order_traverse(root.right)


class TestBinaryTree(unittest.TestCase):
    def test_create_and_insert_binary_tree(self):
        # Create tree with root
        root = Node(10)
        tree = BinaryTree(root)

        # Test root creation
        self.assertEqual(tree.root.value, 10)
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)

        # Insert nodes
        tree.insert(Node(5))
        tree.insert(Node(15))
        tree.insert(Node(3))
        tree.insert(Node(7))
        tree.insert(Node(12))
        tree.insert(Node(20))

        # Test tree structure
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 15)
        self.assertEqual(tree.root.left.left.value, 3)
        self.assertEqual(tree.root.left.right.value, 7)
        self.assertEqual(tree.root.right.left.value, 12)
        self.assertEqual(tree.root.right.right.value, 20)

    def test_mid_order_traverse(self):
        # Create tree with root
        root = Node(10)
        tree = BinaryTree(root)

        # Insert nodes to create a balanced tree
        tree.insert(Node(5))
        tree.insert(Node(15))
        tree.insert(Node(3))
        tree.insert(Node(7))
        tree.insert(Node(12))
        tree.insert(Node(20))

        # Clear any previous traverse results
        tree.purge_traverse_result()

        # Perform mid-order traversal
        tree.mid_order_traverse(tree.root)

        # In-order traversal should return sorted values
        expected = [3, 5, 7, 10, 12, 15, 20]
        self.assertEqual(tree.get_traverse_result(), expected)

        # Test with empty tree
        tree.purge_traverse_result()
        tree.mid_order_traverse(None)
        self.assertEqual(tree.get_traverse_result(), [])

        # Test with single node tree
        tree.purge_traverse_result()
        single_tree = BinaryTree(Node(42))
        single_tree.mid_order_traverse(single_tree.root)
        self.assertEqual(single_tree.get_traverse_result(), [42])


if __name__ == "__main__":
    unittest.main()
