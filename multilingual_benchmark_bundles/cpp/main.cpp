#include <iostream>
#include <vector>
int main() { std::vector<int> values = {12,18,21,9,31}; int total = 0; for (int v : values) total += v; std::cout << "Total: " << total << '\n'; std::cout << "Average: " << (total / static_cast<double>(values.size())) << '\n'; }