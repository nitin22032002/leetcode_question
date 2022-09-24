/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        auto ans=lca(root,p,q);
        return ans.second;
    }
    pair<int,TreeNode*> lca(TreeNode *root,TreeNode *p,TreeNode* q){
        if(root){
            auto a=lca(root->left,p,q);
            if(a.second){
                return a;
            }
            auto b=lca(root->right,p,q);
            if(b.second){
                return b;
            }
            a.first+=b.first;
            if(p==root){
                a.first+=1;
            }
            if(q==root){
                a.first+=1;
            }
            if(a.first==2){
                return {0,root};
            }
            return {a.first,NULL};
        }
        return {0,NULL};
    }
};