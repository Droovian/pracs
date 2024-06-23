#include<iostream>

using namespace std;

int C=0;
string output;

char add(char a, char b){
    if(C == 0 && (a == '1' && b == '1')){
        C = 1;
        return '0';
    }
    else if(C == 0 && (a == '1' || b == '1')){
        C = 0;
        return '1';
    }
    else if(C==0 && (a== '0' && b == '0')){
        C = 0;
        return '0';
    }
    else if(C == 1 && (a == '1' && b == '1')){
        C = 1;
        return '1';
    }
    else if (C == 1 && (a == '1' || b == '1')) 
    {
        C = 1;
        return '0';
    } else
    {
        C = 0;
        return '1';
    }
}

void complement(int& b_size){
    for(int k=3; k>=0; k--){
        if(output[k] == '1'){
            output[k] = '0';
        }
        else{
            output[k] = '1';
        }
    }
}

void compute_sum(string& data, int& b_size) {
    string temp;
    output = data.substr(0, b_size);

    for (int i = b_size; i < data.length(); i += b_size) {
        int x = 0;
        temp = data.substr(i, b_size);

        for (int k = b_size - 1; k >= 0; k--)
            output[k] = add(output[k], temp[k]);

        if (C == 1) {
            for (int k = b_size - 1; k >= 0; k--) {
                if (C == 1) {
                    C = 0;
                    output[k] = add(output[k], '1');
                }
            }
        }
    }
    complement(b_size);
}

int main() {
    int ch, i, found, b_size;
    string one,data;
    while (1) {
        cout << "\nChecksum\n1. Sender Side\n2. Receiver side\n3. Exit\nEnter choice: ";
        cin >> ch;
        switch (ch) {
        case 1:
            cout << "Enter data stream: ";
            cin >> data;
            cout << "Enter block size: ";
            cin >> b_size;
            compute_sum(data, b_size);
            cout << "The checksum is: " << output << "\n";

            // Append the checksum to the data
            data.append(output);
            cout << "The data with checksum is: " << data << "\n";
            break;
        case 2:
            cout << "Enter data stream: ";
            cin >> data;
            cout << "Enter block size: ";
            cin >> b_size;

            compute_sum(data, b_size);
            data = data.substr(0, data.length() - b_size);
            one = "1";
            found = output.find(one);
            if (found) 
            {
                cout << "\nNo error present \nComplement of sum is  " << output;
                cout << "\nActual data is  " << data << "\n";
            } else 
            {
                cout << "Error present in code \n";
                cout << "\nComplement of sum is  " << output;
                cout << "\nSince complement is not equal to 0 error is present\n\n";
            }
            break;
        case 3:
            exit(0);
        default:
            cout << "Enter valid choice\n";
        }
    }
}