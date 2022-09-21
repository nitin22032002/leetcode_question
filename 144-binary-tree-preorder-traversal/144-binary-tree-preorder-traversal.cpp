/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
         vector<int> ans;
        while(root){
        if(root->left){
            TreeNode *t=root->left;
            while(t->right && t->right!=root){
                t=t->right;
            }
            if(t->right==root){
                t->right=NULL;
                root=root->right;
            }
            else{
                ans.push_back(root->val);
                // cout<<t->val<<endl;
                t->right=root;
                root=root->left;
            }
        }
        else{
            ans.push_back(root->val);
            root=root->right;
        }
    }
        return ans;
    }
};