#include<iostream>

using namespace std;

int main()
{
    string s, temp; int c = 0;

    getline(cin, s);
    int n = s.length(); string flag = "01111110";

    for(int i=0; i<n; i++){

        if(s[i] == '1'){
            c++;

            if(c == 5){
                s.insert(i+1, "0");
            }
        }
        else{
            c = 0;
            continue;
        }
    }

     s.insert(0, flag); s.append(flag);
     
    cout << "After bit stuffing it looks like " << s << endl;
    return 0;
}