using System;
class Program {
    static void Main() {
        int[] values = { 12, 18, 21, 9, 31 };
        int total = 0;
        foreach (var value in values) total += value;
        Console.WriteLine($"Total: {total}");
        Console.WriteLine($"Average: {total / (double)values.Length:F2}");
    }
}
