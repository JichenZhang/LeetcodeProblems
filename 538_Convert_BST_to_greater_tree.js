
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
} 

var max = 0;
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var convertBST = function(root) {
    if (root) {
        convertBST(root.right);
        root.val += max;
        max = root.val;
        convertBST(root.left);
        return root;
    }else{
        return null;
    }
};

