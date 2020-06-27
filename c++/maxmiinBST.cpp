#include <iostream>
using namespace std;

void HeapSort(int *A, int n){
    for (int i=n/2-1; i>=0; i--){
        heapify(A, n,i);

    }
}

int main(){
    int A[] = {2, 7,3, 4,6,5};
    bubbleSort(A, 6);
    for(int i= 0; i<6;i++){
        cout<<A[i]<<" ";
    }
    cout<<"\n";
    return 0;
}
