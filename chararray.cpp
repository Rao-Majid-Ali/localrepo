#include <iostream>
using namespace std;
void toUpper(char *word,int n){
    for(int i = 0; i<n ; i++){
        char ch = word[i];
       
        if(ch >= 'a' && ch <= 'z'){
            word[i] = ch-'a'+'A';
        }

        cout<<word[i]<<" ";
    }

}

void tolower(char *word,int n){
    for(int i = 0; i<n ; i++){
        char ch = word[i];
       
        if(ch >= 'A' && ch <= 'Z'){
            word[i] = ch-'A'+'a';
        }

        cout<<word[i]<<" ";
    }

}
int main() {
    char str[5] = {'H', 'e', 'l', 'l', 'o'};
    cout << str[0] << str[1] << str[2] << str[3] << str[4] << endl;

    char  work[] = "code"; 
    cout << work << endl;

    char str2[20] = {'W', 'o', 'r', 'k', 'i', 'n', 'g', '\0'};
    cout << str2 << endl;

    char sentence[30];
    cin.getline(sentence, 30);
    cout << "You entered: " << sentence << endl;

    char word[15]  = "Applecountdown";
    toUpper(word,15);
    cout<<endl;
    tolower(word,15);
    return 0;
}