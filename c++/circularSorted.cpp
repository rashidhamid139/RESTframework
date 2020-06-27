#include<iostream>
using namespace std;


int FindRotationCount(int A[], int n){
    int low=0, high = n-1;
    while (low<=high){
        if(A[low] <= A[high]) return low;
        int mid = (low+high)/2;
        int next = (mid+1)%n;
        int prev = (mid +n -1)%n;
        cout<<A[mid]<<" ";
        if(A[mid] <= A[next] && A[mid]<=A[prev]){
            return mid;
        }
        else if (A[mid] <= A[high]){
            high = mid-1;
        }
        else if(A[mid] >= A[low]){
            low = mid+1;
        }
    };
    return -1;
}

int main(){
    int A[]={15, 22, 23,6,8,10,12};
    int count = FindRotationCount(A, 7);
    cout<<"The array is roatated"<<count<<"times:";
}