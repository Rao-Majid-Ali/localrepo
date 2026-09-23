#include <iostream>
using namespace std;
void print(int *arr,int n){
    for (int i = 0; i < n ; i++){
        cout<<arr[i]<<" ";
    }
}
void selectionsort(int *arr,int n){
    for(int i = 0 ; i < n-1 ; i++){
        int minidx = i;
        for(int j = i+1 ; j < n ; j++){
            if(arr[j] > arr[minidx]){
                minidx  = j;
            }   
        }
        swap(arr[i],arr[minidx]);
    }
    print(arr,n);
}


int main(){
    int arr[6] = {7,2,5,4,6,3};
    int n = 6;
    selectionsort(arr,n);
    return 0;
}