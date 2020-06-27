#include<iostream>
using namespace std;


void insertionSort(int A[], int n){
    for(int i=1; i<n; i++){
        int value = A[i];
        int hole = i;
        while(hole>0 && A[hole-1]>A[hole]){
            swap(A[hole], A[hole-1]);
            hole--;
        };
        A[hole] = value;
    };
};


int main(){
    int A[] = {2,4,7,1,5,3};
    insertionSort(A, 6);
    for(int i =0; i<6; i++){
        cout<<A[i]<<" "<<endl;
    }


}