#include <iostream>
using namespace std;
void swap(int *a, int *b){

}

void bubbleSort(int A[], int n){
    for(int k=0; k<n; k++){
        int count = 0;
        for(int i=0; i<n-k-1; i++){
            if(A[i]>A[i+1]){
                swap(A[i], A[i+1]);
                count = 1;
            };
        };
        if (count == 0){
            cout<<"Exiting Loop After!!!"<<k-1<<" pass"<<endl;
            break;
        }
    };
};

int main(){
    int A[] = {1, 7,3, 4,6,5};
    bubbleSort(A, 6);

    for(int i= 0; i<6;i++){
        cout<<A[i]<<" ";
    }
    cout<<"\n";
    return 0;
}
