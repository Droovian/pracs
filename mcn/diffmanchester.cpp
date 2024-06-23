#include<iostream>
using namespace std;

int main()
{
    string s; int check = 0;
    getline(cin, s);

    for(int i=0; i<s.length(); i++){
        cout << "     " << s[i] << "     ";
    }

    cout << endl;

    // easy but just more cases to handle

    for(int i=0; i<s.length(); i++){

        if(s[i] == '0'){
            if(i == 0){ // initial pattern
                cout<<"|‾‾‾‾|____|";
                check = 0;
            }
            else{
                if(check == 0){
                    cout << "‾‾‾‾|____|";
                    check = 0;
                }
                else{
                    cout << "____|‾‾‾‾|";
                    check = 1;
                }
            }
        }
        else{ // if s[i] == '1'
            if(i == 0){
                cout << "|____|‾‾‾‾|";
                check = 1;
            }
            else{
                if(check == 0){
                    cout<<"_____|‾‾‾‾|";
                    check=1;
                }
                else{
                    cout<<"‾‾‾‾‾|____|";
                    check=0;
                }
            }
        }
    }

    cout << endl;

    return 0;
}