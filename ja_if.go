package main

import (
	"fmt"
)

/*
  基本上只測試H1 -H5, L1-L6 , without considering wild_line yet!!
  完整code will be in main.go!!

*/

func main() {

	// 測試單線
	line_setting := [25][5]int{
		{0, 0, 0, 0, 0}, // 1
		{0, 0, 0, 0, 0}, // 2
		{0, 0, 0, 0, 0}, // 3
		{0, 0, 0, 0, 0}, // 4
		{0, 0, 0, 0, 0}, // 5
		{0, 0, 0, 0, 0}, // 6
		{0, 0, 0, 0, 0}, // 7
		{0, 0, 0, 0, 0}, // 8
		{0, 0, 0, 0, 0}, // 9
		{0, 0, 0, 0, 0}, // 10
		{0, 0, 0, 0, 0}, // 11
		{0, 0, 0, 0, 0}, // 12
		{0, 0, 0, 0, 0}, // 13
		{0, 0, 0, 0, 0}, // 14
		{0, 0, 0, 0, 0}, // 15
		{0, 0, 0, 0, 0}, // 16
		{0, 0, 0, 0, 0}, // 17
		{0, 0, 0, 0, 0}, // 18
		{0, 0, 0, 0, 0}, // 19
		{0, 0, 0, 0, 0}, // 20
		{0, 0, 0, 0, 0}, // 21
		{0, 0, 0, 0, 0}, // 22
		{0, 0, 0, 0, 0}, // 23
		{0, 0, 0, 0, 0}, // 24
		{0, 0, 0, 0, 0}, // 25
	}

	mg_table := [5][3]string{
		{"W1", "L2", "H1"},
		{"W1", "H1", "L2"},
		{"W1", "W1", "W1"},
		{"W1", "L1", "L1"},
		{"W1", "L1", "L1"},
	}

	// H1, 2, 3, 4, 5, L1, 2, 3, 4, 5, 6
	pay_table := map[string][]int{
		"H1": {0, 2, 30, 200, 750}, // h1
		"H2": {0, 2, 30, 100, 750}, // h2
		"H3": {0, 0, 25, 75, 400},  // h3
		"H4": {0, 0, 20, 75, 300},  // h4
		"H5": {0, 0, 20, 75, 300},  // h5
		"L1": {0, 0, 15, 30, 150},  // l1

		"L2": {0, 0, 15, 30, 150}, // l2

		"L3": {0, 0, 10, 25, 130}, // l3
		"L4": {0, 0, 10, 25, 130}, // l4
		"L5": {0, 0, 5, 20, 100},  // l5
		"L6": {0, 0, 5, 20, 100},  // l6
	}

	valid_wild_map := map[string]bool{"W1": true}

	check_obj := ""
	input_obj := "L2"
	var current_win_line int
	var currentGain int
	bet_amount := 10000 // this means 1 ....
	const numberOfLine = 25

	for line_index, tem_list := range line_setting {

		count := 0
		current_win_line = 0

		fmt.Printf("[Stage_01]                   : line_index: %d  , count:  %d,                            input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, input_obj, check_obj, current_win_line)
		//fmt.Printf("[Stage_02]                   : line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)
		//fmt.Printf("[Stage_03_If                 : line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)
		//fmt.Printf("[Stage_03_Else_If: valid_wild: line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)
		//fmt.Printf("[Stage_03: CurrentSymbol=inpu: line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)

		for col_index := 0; col_index < 5; col_index++ {

			count++
			current_symbol := mg_table[col_index][tem_list[col_index]]

			fmt.Printf("[Stage_02]                   : line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)

			if current_symbol != input_obj && !valid_wild_map[current_symbol] {
				fmt.Printf("[Stage_03_If                 : line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)
				break
			} else if valid_wild_map[current_symbol] {
				fmt.Printf("[Stage_03_Else_If: valid_wild: line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)
				if !valid_wild_map[input_obj] {
					current_win_line = count
				} else {
					check_obj = input_obj
					current_win_line = count
				}
			} else if current_symbol == input_obj {
				fmt.Printf("[Stage_03: CurrentSymbol=inpu: line_index: %d  , count:  %d,   current_symbol:   %s ,   input_obj:  %s     check_obj:   %s,  current_win_line:  %d,   \n", line_index, count, current_symbol, input_obj, check_obj, current_win_line)
				check_obj = input_obj
				current_win_line = count
			}
		}

		// 等等做bet amount
		if current_win_line >= 2 && check_obj != "" {
			// 💰
			win_line_to_index := current_win_line - 1
			currentGain = bet_amount * pay_table[check_obj][win_line_to_index] * 1 / numberOfLine

			fmt.Println("Bet amount = ", bet_amount, " pay: ", pay_table[check_obj][win_line_to_index], " currentGain: ", currentGain)
			fmt.Printf("Winning with obj:  %s   ,  winning_line:  %d,  win_number: %d\n", input_obj, line_index+1, current_win_line)
		}
	}
}
