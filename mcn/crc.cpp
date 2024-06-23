#include<iostream>

using namespace std;

string do_xor(const string&a, const string& b){
    string res = "";
    for(int i=1; i<b.length(); i++){
        if(a[i] == b[i]){
            res += "0";
        }
        else{
            res += "1";
        }
    }
    return res;
}

string mod2division(string& dividend, string& divisor){

    int pick = divisor.length();

    string temp = dividend.substr(0, pick);

    int n = dividend.length();

    while( pick < n ){

        if(temp[0] == '1'){
            temp = do_xor(divisor, temp) + dividend[pick];
        }
        else {
            temp = do_xor(std::string(pick, '0'), temp) + dividend[pick];
        }
        pick += 1;
    }

    if(temp[0] == '1'){
        temp = do_xor(divisor, temp);
    }
    else{
        temp = do_xor(std::string(pick, '0'), temp);
        return temp;
    }

}

void encode_data(string& data, string& key){
    int key_length = key.length();

    string append = (data + string(key_length - 1, '0'));
    string remainder = mod2division(append, key);

    string codeword = data + remainder;

    cout << "Remainder: " << remainder << "\n";
    cout << "Encoded data (data + remainder) : " << codeword << "\n";
}

int main()
{
    string data, key;

    cout << "Sender side :" << endl;

    cout << "Enter the data: " << endl;
    cin >> data;

    cout << "Enter generator: " << endl;
    cin >> key;

    encode_data(data, key);

    return 0;
}