#include <iostream>
using namespace std;
int binearySearch(int matrix[4][4],int n,int m,int key){
    
    for (int i = 0; i < n ; i++){
        int st = 0;
        int end = m-1;
        while(st <= end){
            
            int mid = (st+end)/2;
            if (matrix[i][mid] == key ){
                return key;
            }
            else if( matrix[i][mid] < key ){
                st = mid+1;
            }
            else{
                end = mid-1;
            }
        }

    }
    return -1;

}
int main(){
    int matrix[4][4] = {{1,2,3,4},
                        {5,6,7,8},
                        {9,10,11,12},
                        {13,14,15,16}};
    
    cout<<binearySearch(matrix,4,4,12);
    return 0;
}