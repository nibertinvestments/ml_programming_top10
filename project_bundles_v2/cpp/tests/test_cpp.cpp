#include <fstream>
#include <iostream>
int main() {
    std::ifstream file("input.csv");
    std::string line;
    int count = 0;
    while (std::getline(file, line)) ++count;
    std::cout << count << '\n';
}
