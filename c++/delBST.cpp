#include<iostream>
using namespace std;


struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};

struct Node* Delete(struct Node *root, int data){
    if(root == NULL) return root;
    else if (data <  root->data){ 
        root->left = Delete(root->left, data);
    }
    else if (data > root->data){
        root->right = Delete(root->right, data);
    };
};