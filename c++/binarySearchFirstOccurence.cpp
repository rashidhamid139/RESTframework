#include<iostream>
using namespace std;

int BinarySearch(int A[], int n , int x){
    int low = 0;
    int high = n;
    int result = -1;
    cout<<"Hello World"<<" ";
    while(low<=high){
        int mid = (low + high)/2;
        if(x == A[mid]){
            result = mid;
            high = mid-1;
        }
        else if ( x < A[mid]){
            high = mid-1;
        }
        else {
            high = mid+1;
        }
    }
    return result;
}

int main(){
    int A[] = {2,4,10,10,10,18,20};
    int result = BinarySearch(A, 7, 10);
    cout<<result<<"in index of first occurence:";
}