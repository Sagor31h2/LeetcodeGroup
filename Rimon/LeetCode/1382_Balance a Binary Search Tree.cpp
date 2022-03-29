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
    vector<TreeNode*> st;
    void inOrder(TreeNode* root){
        if (root!=NULL){
        
            
            inOrder(root->left);
            st.push_back(root);
            inOrder(root->right); 
        }
        
    }
    TreeNode* createBST(int s,int e){
        if(s>e)
            return NULL;
        int mid = (s + e)/2;
        TreeNode *temp = st.at(mid);
        temp->left = createBST(s,mid-1);
        temp->right = createBST(mid+1,e);
        return temp;
    }
    TreeNode* balanceBST(TreeNode* root) {
        inOrder(root);
        int l = st.size();
        return createBST(0,l-1);
    }
};