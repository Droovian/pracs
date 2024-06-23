#include<iostream>

using namespace std;

// byte stuffing

int main()
{
    string s, temp;

    getline(cin, s); int n = s.length();

    string flag = "01111110", esc = "11100000";

    s.insert(0, flag);
    s.append(flag);

    for(int i=8; i <= n+8; i+=8){
        temp = s.substr(i, 8);

        if(flag == temp || temp == esc){ // escape the flag or escape the escape present in the data
            s.insert(i, esc); i = i + 8;
        }
    }
     cout << "\n" << s << endl;

    return 0;
}