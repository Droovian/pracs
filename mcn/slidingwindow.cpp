#include<iostream>
#include<cstdlib>
#include<ctime>
#include<string>
#include <thread>
#include <chrono>

const int WINDOW_SIZE = 3;
const int TIMEOUT_DURATION = 2000;
const double ACK_LOSS_PROBABILITY = 0.1;
const int TRANSMISSION_DELAY = 1000;

using namespace std;

struct Packet{

    int seq_no;
    bool isAcked;
    string data;

};

void delay(int milliseconds){
    this_thread::sleep_for(chrono::milliseconds(milliseconds));
}

bool isAckLost(){
    return (rand() / (RAND_MAX + 1.0)) < ACK_LOSS_PROBABILITY;
}

void sender(Packet packets[], int numPackets){
    int base = 0;

    while(base < numPackets){

        for(int i=base; i< min(base + WINDOW_SIZE, numPackets); i++){
            if(!packets[i].isAcked){
                delay(TRANSMISSION_DELAY);
                cout << "Sending packet with sequence no" << packets[i].seq_no << endl;
            }
        }

        for(int i=base; i<min(base + WINDOW_SIZE, numPackets); i++){
            if(!packets[i].isAcked){
                if(!isAckLost()){
                    cout << "Received ACK for packet with sequence no" << packets[i].seq_no << endl;
                    packets[i].isAcked = true;
                }
            }
        }

        while(base < numPackets && packets[base].isAcked){
            ++base;
        }

    }
}

void receiver(Packet packets[], int numPackets) {
    int expectedSeqNum = 0;

    for (int i = 0; i < numPackets; ++i) {
        // Simulate transmission delay
        delay(TRANSMISSION_DELAY);

        // Simulate packet loss
        if (!isAckLost()) {
            if (packets[i].seq_no == expectedSeqNum) {
                cout << "Received packet with sequence number " << packets[i].seq_no << endl;
                ++expectedSeqNum;
            }
            // Send ACK
            cout << "Sending ACK for packet with sequence number " << packets[i].seq_no << endl;
        } else {
            cout << "Packet with sequence number " << packets[i].seq_no << " lost." << endl;
        }
    }
}

int main()
{
    srand(time(0));
    const int numPackets = 10;

    Packet packets[numPackets];

    for(int i=0; i<numPackets; i++){
        packets[i].seq_no = i;
        packets[i].isAcked = false;
        packets[i].data = "Packet" + to_string(i);
    }

    cout << "Sender:" << endl;
    sender(packets, numPackets);

    cout << "Receiver:" << endl;
    receiver(packets, numPackets);

    return 0;
}