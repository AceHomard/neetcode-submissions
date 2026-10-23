# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _recurcheck(self, root, borne_basse, borne_haute) -> bool:
        if not root:
            return True
        if borne_basse < root.val < borne_haute:
            return self._recurcheck(root.left, borne_basse, root.val) and self._recurcheck(root.right, root.val, borne_haute)
        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._recurcheck(root, float("-inf"), float("inf"))