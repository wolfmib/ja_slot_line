package main

import (
	"fmt"
	"math/rand"
)

/*

mg:
1:
{L6,H1,L1,L2,H4,L5,L1,L1,L5,L2,L4,L4,L6,L3,L4,H2,L1,L2,L1,L2,L6,L4,L6,L2,L4,L6,S1,W1,L5,L3,L1,L3,H1,L5,L5,H3,L3,L5,H2,L3,L3,L2,L1,L3,L4,W1,L3,L1,L3,L2,L6,L6,L4,L2,H4,L3,L5,L2,L2,H3,L5,L4,L5,S1,L3,L5,L5,L5,L4,L6,H1,L6,L4,L3,L3,L5,L6,L5,W1,L5,L5,L6,L6,L3,L6,L4,H1,L2,H4,L6,L3,L5,L6,L2,W1,H3,L6,L2,L6,L5,L6,L5,L6,L5,L6,L4,L2,L4,L4,L5,S1,L1,L1,L6,L4,S1,L5,L1,H4,L4,L2,L6,H2,L1,L2,H4,L4,L4,L4,H1,L5}

2:
{L6,H1,L1,L2,L4,L5,L1,L4,L5,L2,H3,L1,L6,L5,L4,L5,L1,L2,L1,H1,L3,L4,H2,L5,L6,L6,L6,W1,L5,L3,L1,L6,L1,L5,S1,H2,L3,L5,H2,L3,L3,L2,L1,L3,L4,W1,L3,L1,L3,H1,L6,L3,L4,L2,H4,L3,L5,L2,L2,H3,L5,L4,L5,S1,L3,L5,L1,L5,L4,L6,H1,L6,L4,L3,L3,L5,L6,H2,W1,L5,L5,L6,H2,L3,L6,L4,H1,L2,H4,L6,L3,L5,L6,L2,W1,H3,L6,L2,L6,L5,H3,H1,L6,H3,L6,L4,L2,L4,L4,L5,S1,L1,L1,L6,L4,S1,L5,L1,H4,L4,L2,L6,H2,L1,L2,H4,L4,L4,L4}

3:
{W1,L4,L3,L5,H2,L4,H4,L3,L3,L2,H1,L4,L6,L3,H4,L1,L1,L1,L6,L6,H1,L1,L5,S1,L1,H1,L4,L6,H2,L2,L4,H3,L6,L6,H1,L1,L6,H4,L1,L5,H2,L1,L2,L3,L2,H2,L3,L4,L4,L6,H3,L2,L2,L5,L5,H4,L4,L3,L4,L3,L6,L6,L6,L5,L5,L5,L1,L6,L2,L2,H1,L2,L4,L4,L6,L3,L3,L1,L3,L1,W1,L2,L1,L2,S1,L5,L6,H3,L1,L6,L1,H4,L4,L3,H2,L3,H4,L3,L4,L6,L2,H3,L5,L2,H4,L5,L6,L6,H1,L5,S1,L5,L4,H2,L5,L5,H3,W1,L5,H2,L1,L4,L6,L5,H1,L4,L5,L5,H3,L5,L4,L2,S1,L3,L3,H4,L4,L4,H3,L3,L2,H3,L2,L6,L6,W1,L1,L3,L2}

4:
{W1,L2,H2,L2,S1,L4,H3,L6,L2,H4,L4,L3,L5,L5,L5,L4,H3,L3,L6,L4,H2,L1,L3,L6,L1,L4,L4,L3,W1,L6,L1,H4,L3,L3,H3,H2,L4,L4,L3,L2,H3,H2,L5,H1,L5,L4,L3,L4,H4,L5,H1,L6,L1,L1,L3,H2,H4,L2,H4,L3,L3,H3,L6,L2,S1,H3,W1,L2,L1,H1,L6,L5,L1,H3,L4,L4,L6,H1,L3,L4,L6,H3,L2,S1,L5,H4,L6,L2,L6,W1,L2,H2,H4,L6,L1,L5,L4,L6,L6,L5,H1,L1,L4,L5,H3,L2,L1,H3,L3,L4,H2,H4,L5,H1,L5,H2,L6,H1,L6,L1,H2,L5,L5,H4,L6,L2,H4,L3,L5,H1,S1,H1,L5,H2,L6,H1,L6,L1,H2}

5:
{L6,L2,H2,L2,S1,L4,H3,L6,L2,H4,L4,L3,L5,L5,L5,L4,H3,L3,L6,L4,H2,L1,L3,W1,L1,L4,L4,L3,W1,L6,L1,H4,L3,L3,H3,H2,L4,L4,L3,L2,H3,H2,L5,H1,L5,L4,L3,L4,H4,L5,H1,L6,L1,L1,L3,H2,H4,L2,H4,L3,L3,H3,L6,L2,S1,H3,W1,L2,L1,H1,L6,L5,L1,H3,L4,L4,L6,H1,L3,L4,L6,H3,L2,S1,L5,H4,L6,L2,L6,W1,L2,H2,H4,L6,L1,L5,L4,L6,L6,L5,H1,L1,L4,L5,H3,L2,L1,H3,L3,L4,H2,H4,L5,H1,L5,H2,L6,H1,L6,L1,H2,L5,L5,H4,L6,L2,H4,L3,L5,H1,S1,H1,L5,H2,L6,H1,L6}

*/

// e.g. input_index = 100
// random return 0, 1,2,3,4,5....99
func obtenir_random_integer(input_index int) int {
	return rand.Intn(input_index)
}

/*

a = [3][4]int{
   {0, 1, 2, 3} ,     initializers for row indexed by 0
   {4, 5, 6, 7} ,     initializers for row indexed by 1
   {8, 9, 10, 11}     initializers for row indexed by 2
}

*/

/*
1	1	1	1	1
0	0	0	0	0
2	2	2	2	2
0	1	2	1	0
2	1	0	1	2
0	0	1	0	0
2	2	1	2	2
1	0	0	0	1
1	2	2	2	1
0	1	1	1	0
2	1	1	1	2
0	1	0	1	0
2	1	2	1	2
1	0	1	0	1
1	2	1	2	1
1	1	0	1	1
1	1	2	1	1
0	2	0	2	0
2	0	2	0	2
1	0	2	0	1
*/

type one_pay_list struct {
	one int
	two int
	thr int
	fou int
	fiv int
}

/*

H1	10	50	500	2000
H2	8	40	300	1500
H3	0	25	175	1000
H4	0	15	100	750
L1	0	12	75	250
L2	0	12	75	250
L3	0	10	50	150
L4	0	10	50	150
L5	0	5	25	100
L6	0	5	25	100
S1	0	5	25	200
W1	60	600	3000	10000

*/


"""
jira-tickect note:
	jason:  I am thinking about using single_line for simulation in golang, that helps speed-up. 
			c'est bon pour moi to calculate you mother fucker !! haha 


"""

// Main Function:
func main() {

	//make map
	//lineable_list := []string{"H1", "H2", "H3", "H4", "L1", "L2", "L3", "L4", "L5", "L6", "W1", "S1"}
	symbols_map_by_str := make(map[string]int)
	symbols_map_by_str["H1"] = 0
	symbols_map_by_str["H2"] = 1
	symbols_map_by_str["H3"] = 2
	symbols_map_by_str["H4"] = 3
	symbols_map_by_str["L1"] = 4
	symbols_map_by_str["L2"] = 5
	symbols_map_by_str["L3"] = 6
	symbols_map_by_str["L4"] = 7
	symbols_map_by_str["L5"] = 8
	symbols_map_by_str["L6"] = 9
	symbols_map_by_str["W1"] = 10
	symbols_map_by_str["S1"] = 11

	symbols_map_by_id := make(map[int]string)
	symbols_map_by_id[0] = "H1"
	symbols_map_by_id[1] = "H2"
	symbols_map_by_id[2] = "H3"
	symbols_map_by_id[3] = "H4"
	symbols_map_by_id[4] = "L1"
	symbols_map_by_id[5] = "L2"
	symbols_map_by_id[6] = "L3"
	symbols_map_by_id[7] = "L4"
	symbols_map_by_id[8] = "L5"
	symbols_map_by_id[9] = "L6"
	symbols_map_by_id[10] = "W1"
	symbols_map_by_id[11] = "S1"

	/*H1	10	50	500	2000 */
	var h1 one_pay_list
	h1.one = 0
	h1.two = 10
	h1.thr = 50
	h1.fou = 500
	h1.fiv = 2000

	/*H2	8	40	300	1500*/
	var h2 one_pay_list
	h1.one = 0
	h1.two = 8
	h1.thr = 40
	h1.fou = 300
	h1.fiv = 1500

	//  明天做這邊 ......
	var h3 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var h4 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var l1 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var l2 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var l3 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var l4 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var l5 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var l6 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var w1 one_pay_list
	h1.one = 0
	h1.two = 100000
	h1.thr = 500000
	h1.fou = 5000000
	h1.fiv = 20000000

	var s1 one_pay_list
	s1.one = 0
	s1.two = 0
	s1.thr = 50000
	s1.fou = 250000
	s1.fiv = 2000000

	pay_make := make([]one_pay_list, 0)
	pay_make = append(pay_make, s1)
	pay_make = append(pay_make, h1)

	fmt.Println("Check the pay-table with make map")
	fmt.Println(pay_make)

	// 20 line
	line_setting := [20][5]int{
		{1, 1, 1, 1, 1},
		{0, 0, 0, 0, 0},
		{2, 2, 2, 2, 2},
		{0, 1, 2, 1, 0},
		{2, 1, 0, 1, 2},
		{0, 0, 1, 0, 0},
		{2, 2, 1, 2, 2},
		{1, 0, 0, 0, 1},
		{1, 2, 2, 2, 1},
		{0, 1, 1, 1, 0},
		{2, 1, 1, 1, 2},
		{0, 1, 0, 1, 0},
		{2, 1, 2, 1, 2},
		{1, 0, 1, 0, 1},
		{1, 2, 1, 2, 1},
		{1, 1, 0, 1, 1},
		{1, 1, 2, 1, 1},
		{0, 2, 0, 2, 0},
		{2, 0, 2, 0, 2},
		{1, 0, 2, 0, 1},
	}

	fmt.Println("Loop line")
	for i, list := range line_setting {
		fmt.Println(i, list)
	}

	lineable_list := []string{"H1", "H2", "H3", "H4", "L1", "L2", "L3", "L4", "L5", "L6", "W1", "S1"}

	fmt.Println("Loop liable list:")
	for i, symbol := range lineable_list {
		fmt.Println(i, symbol)
	}

	const i_one_size = 131
	const i_one_size_extend = i_one_size + 2

	const i_two_size = 129
	const i_two_size_extend = i_two_size + 2

	const i_thr_size = 149
	const i_thr_size_extend = i_thr_size + 2

	const i_fou_size = 139
	const i_fou_size_extend = i_fou_size + 2

	const i_fiv_size = 137
	const i_fiv_size_extend = i_fiv_size + 2

	//#######################################################################

	// Let's copy the main game symbols: 131 129 149 139 137
	mg_col_un := [i_one_size_extend]string{"L6", "H1", "L1", "L2", "H4", "L5", "L1", "L1", "L5", "L2", "L4", "L4", "L6", "L3", "L4", "H2", "L1", "L2", "L1", "L2", "L6", "L4", "L6", "L2", "L4", "L6", "S1", "W1", "L5", "L3", "L1", "L3", "H1", "L5", "L5", "H3", "L3", "L5", "H2", "L3", "L3", "L2", "L1", "L3", "L4", "W1", "L3", "L1", "L3", "L2", "L6", "L6", "L4", "L2", "H4", "L3", "L5", "L2", "L2", "H3", "L5", "L4", "L5", "S1", "L3", "L5", "L5", "L5", "L4", "L6", "H1", "L6", "L4", "L3", "L3", "L5", "L6", "L5", "W1", "L5", "L5", "L6", "L6", "L3", "L6", "L4", "H1", "L2", "H4", "L6", "L3", "L5", "L6", "L2", "W1", "H3", "L6", "L2", "L6", "L5", "L6", "L5", "L6", "L5", "L6", "L4", "L2", "L4", "L4", "L5", "S1", "L1", "L1", "L6", "L4", "S1", "L5", "L1", "H4", "L4", "L2", "L6", "H2", "L1", "L2", "H4", "L4", "L4", "L4", "H1", "L5",
		"L6", "H1"}
	mg_col_de := [i_two_size_extend]string{"L6", "H1", "L1", "L2", "L4", "L5", "L1", "L4", "L5", "L2", "H3", "L1", "L6", "L5", "L4", "L5", "L1", "L2", "L1", "H1", "L3", "L4", "H2", "L5", "L6", "L6", "L6", "W1", "L5", "L3", "L1", "L6", "L1", "L5", "S1", "H2", "L3", "L5", "H2", "L3", "L3", "L2", "L1", "L3", "L4", "W1", "L3", "L1", "L3", "H1", "L6", "L3", "L4", "L2", "H4", "L3", "L5", "L2", "L2", "H3", "L5", "L4", "L5", "S1", "L3", "L5", "L1", "L5", "L4", "L6", "H1", "L6", "L4", "L3", "L3", "L5", "L6", "H2", "W1", "L5", "L5", "L6", "H2", "L3", "L6", "L4", "H1", "L2", "H4", "L6", "L3", "L5", "L6", "L2", "W1", "H3", "L6", "L2", "L6", "L5", "H3", "H1", "L6", "H3", "L6", "L4", "L2", "L4", "L4", "L5", "S1", "L1", "L1", "L6", "L4", "S1", "L5", "L1", "H4", "L4", "L2", "L6", "H2", "L1", "L2", "H4", "L4", "L4", "L4",
		"L6", "H1"}
	mg_col_tr := [i_thr_size_extend]string{"W1", "L4", "L3", "L5", "H2", "L4", "H4", "L3", "L3", "L2", "H1", "L4", "L6", "L3", "H4", "L1", "L1", "L1", "L6", "L6", "H1", "L1", "L5", "S1", "L1", "H1", "L4", "L6", "H2", "L2", "L4", "H3", "L6", "L6", "H1", "L1", "L6", "H4", "L1", "L5", "H2", "L1", "L2", "L3", "L2", "H2", "L3", "L4", "L4", "L6", "H3", "L2", "L2", "L5", "L5", "H4", "L4", "L3", "L4", "L3", "L6", "L6", "L6", "L5", "L5", "L5", "L1", "L6", "L2", "L2", "H1", "L2", "L4", "L4", "L6", "L3", "L3", "L1", "L3", "L1", "W1", "L2", "L1", "L2", "S1", "L5", "L6", "H3", "L1", "L6", "L1", "H4", "L4", "L3", "H2", "L3", "H4", "L3", "L4", "L6", "L2", "H3", "L5", "L2", "H4", "L5", "L6", "L6", "H1", "L5", "S1", "L5", "L4", "H2", "L5", "L5", "H3", "W1", "L5", "H2", "L1", "L4", "L6", "L5", "H1", "L4", "L5", "L5", "H3", "L5", "L4", "L2", "S1", "L3", "L3", "H4", "L4", "L4", "H3", "L3", "L2", "H3", "L2", "L6", "L6", "W1", "L1", "L3", "L2",
		"W1", "L4"}
	mg_col_qu := [i_fou_size_extend]string{"W1", "L2", "H2", "L2", "S1", "L4", "H3", "L6", "L2", "H4", "L4", "L3", "L5", "L5", "L5", "L4", "H3", "L3", "L6", "L4", "H2", "L1", "L3", "L6", "L1", "L4", "L4", "L3", "W1", "L6", "L1", "H4", "L3", "L3", "H3", "H2", "L4", "L4", "L3", "L2", "H3", "H2", "L5", "H1", "L5", "L4", "L3", "L4", "H4", "L5", "H1", "L6", "L1", "L1", "L3", "H2", "H4", "L2", "H4", "L3", "L3", "H3", "L6", "L2", "S1", "H3", "W1", "L2", "L1", "H1", "L6", "L5", "L1", "H3", "L4", "L4", "L6", "H1", "L3", "L4", "L6", "H3", "L2", "S1", "L5", "H4", "L6", "L2", "L6", "W1", "L2", "H2", "H4", "L6", "L1", "L5", "L4", "L6", "L6", "L5", "H1", "L1", "L4", "L5", "H3", "L2", "L1", "H3", "L3", "L4", "H2", "H4", "L5", "H1", "L5", "H2", "L6", "H1", "L6", "L1", "H2", "L5", "L5", "H4", "L6", "L2", "H4", "L3", "L5", "H1", "S1", "H1", "L5", "H2", "L6", "H1", "L6", "L1", "H2",
		"W1", "L2"}
	mg_col_ci := [i_fiv_size_extend]string{"L6", "L2", "H2", "L2", "S1", "L4", "H3", "L6", "L2", "H4", "L4", "L3", "L5", "L5", "L5", "L4", "H3", "L3", "L6", "L4", "H2", "L1", "L3", "W1", "L1", "L4", "L4", "L3", "W1", "L6", "L1", "H4", "L3", "L3", "H3", "H2", "L4", "L4", "L3", "L2", "H3", "H2", "L5", "H1", "L5", "L4", "L3", "L4", "H4", "L5", "H1", "L6", "L1", "L1", "L3", "H2", "H4", "L2", "H4", "L3", "L3", "H3", "L6", "L2", "S1", "H3", "W1", "L2", "L1", "H1", "L6", "L5", "L1", "H3", "L4", "L4", "L6", "H1", "L3", "L4", "L6", "H3", "L2", "S1", "L5", "H4", "L6", "L2", "L6", "W1", "L2", "H2", "H4", "L6", "L1", "L5", "L4", "L6", "L6", "L5", "H1", "L1", "L4", "L5", "H3", "L2", "L1", "H3", "L3", "L4", "H2", "H4", "L5", "H1", "L5", "H2", "L6", "H1", "L6", "L1", "H2", "L5", "L5", "H4", "L6", "L2", "H4", "L3", "L5", "H1", "S1", "H1", "L5", "H2", "L6", "H1", "L6",
		"L6", "L2"}

	fmt.Println(mg_col_un[0], mg_col_un[1], mg_col_un[2])
	fmt.Println(mg_col_de[0], mg_col_de[1], mg_col_de[2])
	fmt.Println(mg_col_tr[0], mg_col_tr[1], mg_col_tr[2])
	fmt.Println(mg_col_qu[0], mg_col_qu[1], mg_col_qu[2])
	fmt.Println(mg_col_ci[0], mg_col_ci[1], mg_col_ci[2])

	i_un := obtenir_random_integer(i_one_size)
	i_de := obtenir_random_integer(i_two_size)
	i_tr := obtenir_random_integer(i_thr_size)
	i_qu := obtenir_random_integer(i_fou_size)
	i_ci := obtenir_random_integer(i_fiv_size)

	fmt.Println("Random Table:")
	mg_table := [5][3]string{
		{mg_col_un[i_un], mg_col_un[i_un+1], mg_col_un[i_un+2]},
		{mg_col_de[i_de], mg_col_de[i_de+1], mg_col_de[i_de+2]},
		{mg_col_tr[i_tr], mg_col_tr[i_tr+1], mg_col_tr[i_tr+2]},
		{mg_col_qu[i_qu], mg_col_qu[i_qu+1], mg_col_qu[i_qu+2]},
		{mg_col_ci[i_ci], mg_col_ci[i_ci+1], mg_col_ci[i_ci+2]},
	}

	fmt.Println(mg_table)

	//S1:
	curr_s1_cnt := 0
	curr_s1_enter_fg_flag := 0
	fmt.Println("Each Symbol in Table:")
	for col_index, col_list := range mg_table {
		for row_index, symbol := range col_list {
			fmt.Println("(col, row) = ", col_index, " , ", row_index, "  = ", symbol)
			if symbol == "S1" {
				curr_s1_cnt += 1
			}
		}
	}

	// Pay S1
	if curr_s1_cnt == 2 {
		fmt.Println(" Win S1-2")
	} else if curr_s1_cnt == 3 {
		fmt.Println(" Win S1-3")
		curr_s1_enter_fg_flag = 1
	} else if curr_s1_cnt == 4 {
		fmt.Println(" Win S1-4")
		curr_s1_enter_fg_flag = 1
	} else if curr_s1_cnt == 5 {
		fmt.Println(" Win S1-5")
		curr_s1_enter_fg_flag = 1
	}

	fmt.Println("S1 cnts =  ", curr_s1_cnt)
	fmt.Println("S1 flag =  ", curr_s1_enter_fg_flag)

	// loop each line
	for line_index, tem_list := range line_setting {
		tem_symbol := make([]string, 0)
		for i := 0; i < 5; i++ {
			_tem_symbol := mg_table[i][tem_list[i]]
			fmt.Println("line_index: ", line_index, " with col: ", i, "symbol: ", _tem_symbol)
			tem_symbol = append(tem_symbol, _tem_symbol)
		}

		// display
		fmt.Println("Outside of the loop")
		fmt.Println(tem_symbol)

	}

	var name_str = "Jean "
	fmt.Printf("Bonjour %s !\n", name_str)

}
