#python

def findLCA(self, root,l,h):
        if not root:
            return None
        if root.data >= l and root.data <= h:
            return root
        l_s = self.findLCA(root.left,l,h)
        r_s = self.findLCA(root.right,l,h)
        
        if l_s is not None:
            return l_s
        else:
            return r_s
        
    def LCA(self, root, n1, n2):
        # your code here
        l = min(n1.data,n2.data)
        h = max(n1.data,n2.data)
        
        lca = self.findLCA(root,l,h)
        
        return lca
