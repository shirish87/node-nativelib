package main

import "C"
import "fmt"


func init() {}

func main() {}

//export CallFn
func CallFn() {
    fmt.Println("I was called")
}

