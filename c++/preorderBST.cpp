#include<iostream>
using namespace std;


struct Node {
    char data;
    Node* left;
    Node* right;
};


void LevelOrder(Node* root){
    if(root == NULL){
        return ;
    }
}