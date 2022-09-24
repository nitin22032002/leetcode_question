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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        auto ans=get(root,targetSum);
        for(auto &val:ans){
            reverse(val.begin(),val.end());
        }
        return ans;
    }
    vector<vector<int>> get(TreeNode *root,int target){
            vector<vector<int>> ans;
        if(root){
            if(!root->left && !root->right){
                if(root->val==target){
                    vector<int> t={root->val};
                    ans.push_back(t);
                }
                return ans;
            }
            ans=get(root->left,target-root->val);
            for(auto &val:ans){
                val.push_back(root->val);
            }
            auto a=get(root->right,target-root->val);
            for(auto &val:a){
                val.push_back(root->val);
                ans.push_back(val);
            }
            return ans;
        }
        return ans;
    }
};