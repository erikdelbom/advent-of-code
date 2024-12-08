#include <iostream>
#include <cstdint>
#include <string>
#include <vector>
#include <fstream>
#include <chrono>

using namespace std;


vector<string> read_input(const string & filename) 
{
    vector<string> result;
    ifstream istream{filename, ios::in};
    string line;

    while ( getline(istream, line) ) 
    {
        result.push_back(line);
    }

    return result;
}


int part_1(const vector<string> & input) 
{
    return 0;
}


int part_2(const vector<string> & input) 
{
    return 0;
}


int main(int argc, char *argv[]) 
{
    string filename = argv[1];
    vector<string> input = read_input(filename);

    /* Part 1 */
    {
        auto start = chrono::high_resolution_clock::now();
        int result = part_1(input);
        auto stop = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::seconds>(stop-start);

        std::cout << "Part 1: " << result << " - " << duration.count() << " s" << std::endl;
    }

    /* Part 2 */
    {
        auto start = chrono::high_resolution_clock::now();
        int result = part_2(input);
        auto stop = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::seconds>(stop-start);

        std::cout << "Part 2: " << result << " - " << duration.count() << " s" << std::endl;
    }

    return 0;
}
