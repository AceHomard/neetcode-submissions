# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.pos = {val: i for i, val in enumerate(inorder)}
        self.i = 0
        return self._build(0, len(inorder) - 1)

    def _build(self, l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        root = TreeNode(self.preorder[self.i])
        self.i += 1
        mid = self.pos[root.val]
        root.left = self._build(l, mid - 1)
        root.right = self._build(mid + 1, r)
        return root
