package main

import "fmt"

func main() {
	generator := &Generator{Length: 1024}

	go generator.Generate()
	for {
		fmt.Println(generator.GetCurrentKey())
	}
}
