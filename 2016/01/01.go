package main

import (
	"bufio"
	"fmt"
	//"math"
	"os"
	"strconv"
	"strings"
)

type position struct {
	x int
	y int
}

func main() {
	s := bufio.NewScanner(os.Stdin)

	direc := [4][2]int{
		{1, 0},
		{0, 1},
		{-1, 0},
		{0, -1},
	}
	m := make(map[string]int)
	fmt.Println(direc)
	ind := 0
	pos := [2]int{0, 0}
	result2 := 0
	for s.Scan() {
		b := s.Bytes()
		fmt.Println(string(b))
		mystring := string(b)
		mystring_arr := strings.Split(mystring, ",")
		for x := range mystring_arr {
			ss := strings.TrimLeft(mystring_arr[x], " ")
			v, _ := strconv.Atoi(ss[1:])
			key_str := ""
			if string(ss[0]) == "R" {
				ind += 1
				ind %= 4
			} else if string(ss[0]) == "L" {
				ind += 3
				ind %= 4
			} else {
				fmt.Println("WTF")
			}
			for xx := range v {
                fmt.Println(xx)
				pos[0] += direc[ind][0] 
				pos[1] += direc[ind][1]
				pos_x := strconv.Itoa(pos[0])
				pos_y := strconv.Itoa(pos[1])
				key_str = pos_x + "," + pos_y
				m[key_str] += 1
				if m[key_str] == 2 && result2 == 0 {
					if pos[1] < 0 {
						pos[1] *= -1
					}

					if pos[0] < 0 {
						pos[0] *= -1
					}
					result2 = pos[0] + pos[1]
				}
			}

		}
	}
	if pos[1] < 0 {
		pos[1] *= -1
	}

	if pos[0] < 0 {
		pos[0] *= -1
	}
	result1 := pos[0] + pos[1]
	fmt.Println(pos)
	fmt.Println("ans1: ", result1)
	fmt.Println("ans2: ", result2)

}
