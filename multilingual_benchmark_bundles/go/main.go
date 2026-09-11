package main
import "fmt"
func main() { values := []int{12,18,21,9,31}; total:=0; for _, v := range values { total += v }; fmt.Println('Total:', total); fmt.Printf('Average: %.2f\n', float64(total)/float64(len(values))) }