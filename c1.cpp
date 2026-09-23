#include <iostream>
using namespace std;

void swap(int *arr,int start, int end){
    int temp = arr[start];
    arr[start] = arr[end] ;
    arr[end] = temp;

}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(int);
    int start = 0;
    int end = n-1;
    while(start < end){
        swap(arr,start,end);
        start++;
        end--;
    }




    // int copyarr[n];
    // for(int i = 0 ; i < n  ; i++){
    //     int j = n-i-1;
    //     copyarr[i] = arr[j];
    // }
    // for(int i = 0 ; i < n  ; i++){
    //     arr[i] = copyarr[i];
    // }
    for(int i = 0 ; i < n ; i++){
        cout<<arr[i]<<"   ";
    }
    return 0;
}