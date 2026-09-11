package main

import (
    "fmt"
    "os"
)

func main() {
    data, _ := os.ReadFile("input.csv")
    fmt.Println(len(data))
}
