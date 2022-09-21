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
    bool isValidBST(TreeNode* root) {
         long long int  min_v=-pow(2,31)-1;
        bool status=true;
        while(root){
        if(root->left){
            TreeNode *t=root->left;
            while(t->right && t->right!=root){
                t=t->right;
            }
            if(t->right==root){
                if(root->val<=min_v){
                    status= false;
                }
                min_v=root->val;
                t->right=NULL;
                root=root->right;
            }
            else{
                // ans.push_back(root->val);
                // cout<<t->val<<endl;
                t->right=root;
                root=root->left;
            }
        }
        else{
            // ans.push_back(root->val);
            if(root->val<=min_v){
                    status= false;
                }
                min_v=root->val;
            root=root->right;
        }
    }
        return status;
    }
};