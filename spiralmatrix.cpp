#inc44lude <iostream>
using namespace std;

void spiralMatrix(int matix[][4],int n ,int m){
    int sr = 0;
    int er = n-1;
    int sc = 0;
    int ec = m-1;
    while(sr <= er && sc <= ec){
        //top
        for(int i = sr ; i <= ec ; i++){
            cout << matix[i][ec]<<" ";
        }
        //right
        for(int i = sc ; i <= er  ; i++){
            cout << matix[i][ec]<<" ";
        }
        //bottom
        for(int j = er-1 ; j >= sc ; j--){
            cout << matix[er][j]<<"   ";
        }
        //left
        for(int j = ec-1 ; j >= sr+1 ; j-- ){
            cout << matix[j][sc]<<" ";
        } 
        
        sr++ ; sc++;
        er-- ; ec--;
    }
    
   
    
}
int main(){
    int mar[4][4] = {{1,2,3,4},
                    {5,6,7,8},
                    {9,10,11,12},
                    {13,14,15,16}};

    spiralMatrix(mar,4,4);
    return 0;
}