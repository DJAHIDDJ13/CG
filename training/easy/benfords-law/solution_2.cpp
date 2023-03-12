#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int N;
    cin >> N; cin.ignore();
    int log[10] = {0};
    for (int i = 0; i < N; i++) {
        string transaction;
        getline(cin, transaction);
        for(int j = 0; j < transaction.length(); j++) {
            if(transaction[j] >= '1' && transaction[j] <= '9') {
                log[transaction[j]-'1'] ++;
                break;
            }
        }
    }
    double ben[] = {30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6};
    for(int i = 0; i < 9; i++) {
        if(abs(log[i] * 100.0 / N - ben[i]) > 10) {
            cout << "true" << endl;
            exit(0);
        }
    }
    cout << "false" << endl;
}