class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root:
        print(root.val)
        root.left, root.right = root.right, root.left
        invertTree(root.left)
        invertTree(root.right)
        return root


def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    invRoot = invertTree(root)
    print("solution...\n")
    printTree(invRoot)


if __name__ == '__main__':
    main()
