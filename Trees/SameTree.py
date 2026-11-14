#leetcode 100
class Solution:
    def sameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)