#include <iostream>

using namespace std;

int main() {
    char c;
    int floor = 0;
    int char_position = 1;
    
    while ( cin >> c ) {
        if ( c == '(' ) {
            floor++;
        } else floor--;

        if ( floor == -1) {
            cout << char_position << endl;
            break;
        }

        char_position++;
    }

}