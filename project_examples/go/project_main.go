package main

import "fmt"

func main() {
    items := []int{12, 18, 21, 9, 31}
    total := 0
    for _, value := range items { total += value }
    fmt.Println("Total:", total)
    fmt.Printf("Average: %.2f\n", float64(total)/float64(len(items)))
}
