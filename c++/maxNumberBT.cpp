#include<bits/stdc++.h>
#include<iostream>
using namespace std;

class Node {
    public:
    int data;
    Node* left, *right;

    Node(int data){
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

int findMax(Node* root){
    if (root == NULL){
        return INT_MIN;
    }

    int res = root->data;
    int lres = findMax(root->left);
    int rres = findMax(root->right);
    if(lres > res){
        res = lres;
    }
    if (rres > res){
        res = rres;
    }
    return res;

}


int main(){

    Node* newRoot = NULL;
    Node *root = new Node(2);
    root->left = new Node(7);
    root->right = new Node(5);
    root->left->right = new Node(6);
    root->left->right->left = new Node(1);
    root->left->right->right = new Node(11);
    root->right->right = new Node(9);
    root->right->right->left = new Node(4);

    cout<<"Maximum Element is:"<<findMax(root)<<endl;

    return 0;
}
