class Solutions:
    def PathSum(self, root, targetsum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetsum == root.val
        remaining = targetsum - root.val
        return (
            self.PathSum(root.left, remaining) or 
            self.PathSum(root.right, remaining)
        )