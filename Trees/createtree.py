class Solution:

    def preorder(self, root):
        if root is None:
            return
        print(root.val)
        print(root.left)
        print(root.right)   