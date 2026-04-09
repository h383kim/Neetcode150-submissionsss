# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = set()
        depths.add(0)
        self.tag(root, 1)
        self.search(root, depths)
        return max(depths)

    def search(self, root, depths):
        if root == None:
            return
        else:
            depths.add(root.val)
        
        if root.left:
            self.search(root.left, depths)
        if root.right:
            self.search(root.right, depths)


    def tag(self, root, depth):
        if root == None:
            return

        root.val = depth
        depth += 1
        if root.left:
            self.tag(root.left, depth)
        if root.right:
            self.tag(root.right, depth)
        