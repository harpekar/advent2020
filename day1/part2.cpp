#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h> 

using namespace std;

int main() {

    unordered_set <int> values;

    ifstream valueFile; 

    valueFile.open("values.txt");

    string line;

    if (valueFile.is_open()) {

        while (getline (valueFile, line)) {    
            
            int value = stoi(line, nullptr);

            values.insert(value);

        }

        valueFile.close();
    }

    for (auto i = values.begin(); i != values.end(); ++i) {

        cout << "First value is " << *i << endl; 

        //int leftOver = 2020 - *i;

        //cout << "Leftover is " << leftOver << endl;

        for (auto j = values.begin(); j != values.end(); ++j) {

            int leftOver = 2020 - *i - *j;

            cout << "Leftover is now " << leftOver << endl;

            if (values.find(leftOver) != values.end()) { // If the key exists in the set

                int answer = leftOver * (*i) * (*j);

                cout << "Found. Answer is " << answer << endl;

                return 0;
            }

        }

    }

}
