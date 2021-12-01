#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string line;

    while ( getline(cin, line) ) {
        vector<int> dimensions{};
        string tmp = "";
        for ( auto c : line) {
            if (c == 'x') {
                dimensions.push_back(stoi(tmp));
                tmp = "";
            } else {
                tmp += c;
            }
        }

        dimensions.push_back(stoi(tmp));

        for ( auto d : dimensions ) {
            cout << d << "x";
        }
    }

    return 0;
}