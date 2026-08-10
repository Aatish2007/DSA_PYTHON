# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        inorder(root)
        dummy=TreeNode(0)
        curr=dummy 
        for v in vals:
            curr.right=TreeNode(v)
            curr=curr.right
        return dummy.right

#Approach-2 inplace pointer manipulation
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        self.curr = dummy
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.curr.right = node
            self.curr = node
            inorder(node.right)
            
        inorder(root)
        return dummy.right  # Must be indented inside increasingBST!
'''
#approach-3 morris traversal
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy=TreeNode(0)
        tail=dummy
        curr=root
        while curr:
            if not curr.left:
                tail.right=curr
                tail=curr
                curr=curr.right
            else:
                pred=curr.left
                while pred.right:
                    pred=pred.right
                pred.right=curr
                next_node=curr.left
                curr.left=None
                curr=next_node
        return dummy.right
