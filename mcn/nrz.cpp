#include<iostream>
using namespace std;

int main()
{
    string s;
    getline(cin, s);

    for(int i=0; i<s.length(); i++){
        cout << "   " << s[i] << "   ";
    }

    cout << endl;

    for(int i=0; i<s.length(); i++){
        if(s[i] == '0'){
            cout << "______|";
        }
        else{
            cout << "‾‾‾‾‾‾|";
        }
    }
    cout << endl;

    return 0;
}