#include <iostream>
#include <vector>
int main() {
    std::vector<int> items = {12, 18, 21, 9, 31};
    int total = 0;
    for (int value : items) total += value;
    std::cout << "Total: " << total << '\n';
    std::cout << "Average: " << (total / static_cast<double>(items.size())) << '\n';
}
