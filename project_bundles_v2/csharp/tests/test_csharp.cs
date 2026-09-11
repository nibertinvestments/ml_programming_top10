using System;
using System.IO;
class Program {
    static void Main() {
        var lines = File.ReadAllLines("input.csv");
        Console.WriteLine(lines.Length);
    }
}
