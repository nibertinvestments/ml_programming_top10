using System;
class Program {
    static void Main() {
        int[] items = { 12, 18, 21, 9, 31 };
        int total = 0;
        foreach (int value in items) total += value;
        Console.WriteLine($"Total: {total}");
        Console.WriteLine($"Average: {total / (double)items.Length:F2}");
    }
}
