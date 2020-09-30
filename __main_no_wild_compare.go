package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"math/rand"
	"os"
	"time"
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

/*
jira-tickect note:
	jason:  I am thinking about using single_line for simulation in golang, that helps speed-up.
			c'est bon pour moi to calculate you mother fucker !! haha


*/

// Main Function:
func main() {

	rand.Seed(time.Now().UnixNano())

	//make map:
	//lineable_list := []string{"H1", "H2", "H3", "H4", "L1", "L2", "L3", "L4", "L5", "L6", "W1", "S1"}
	symbols_map_by_str := make(map[string]int)
	symbols_map_by_str["H1"] = 0
	symbols_map_by_str["H2"] = 1
	symbols_map_by_str["H3"] = 2
	symbols_map_by_str["H4"] = 3
	symbols_map_by_str["H5"] = 4
	symbols_map_by_str["L1"] = 5
	symbols_map_by_str["L2"] = 6
	symbols_map_by_str["L3"] = 7
	symbols_map_by_str["L4"] = 8
	symbols_map_by_str["L5"] = 9
	symbols_map_by_str["L6"] = 10
	symbols_map_by_str["W1"] = 11
	symbols_map_by_str["S1"] = 12

	symbols_map_by_id := make(map[int]string)
	symbols_map_by_id[0] = "H1"
	symbols_map_by_id[1] = "H2"
	symbols_map_by_id[2] = "H3"
	symbols_map_by_id[3] = "H4"
	symbols_map_by_id[4] = "H5"
	symbols_map_by_id[5] = "L1"
	symbols_map_by_id[6] = "L2"
	symbols_map_by_id[7] = "L3"
	symbols_map_by_id[8] = "L4"
	symbols_map_by_id[9] = "L5"
	symbols_map_by_id[10] = "L6"
	symbols_map_by_id[11] = "W1"
	symbols_map_by_id[12] = "S1"

	// how to access:
	// reel_value = ja_random_geneartor()
	// actuary_check_random_cnt_distribution[col_0][reel_value] += 1
	// ...................
	// reel_value = ja_random_geneartor()
	// actuary_check_random_cnt_distribution[col_4][reel_value] += 1
	actuary_check_random_cnt_distribution := [5][141]int{}

	//[col_index: 0,1,2,3,4] [0,1,2,3 -> H1, h2, h3 ..]
	actuary_Col_SymbolIndex_cnt_distribution := [5][13]int{}

	// 25 line

	line_setting := [25][5]int{
		{1, 1, 1, 1, 1}, // 1
		{0, 0, 0, 0, 0}, // 2
		{2, 2, 2, 2, 2}, // 3

		{0, 1, 2, 1, 0}, // 4
		{2, 1, 0, 1, 2}, // 5
		{0, 0, 1, 0, 0}, // 6

		{2, 2, 1, 2, 2}, // 7
		{1, 2, 2, 2, 1}, // 8
		{1, 0, 0, 0, 1}, // 9

		{1, 0, 1, 0, 1}, // 10
		{1, 2, 1, 2, 1}, // 11
		{0, 1, 0, 1, 0}, // 12

		{2, 1, 2, 1, 2}, // 13
		{1, 1, 0, 1, 1}, // 14
		{1, 1, 2, 1, 1}, // 15

		{0, 1, 1, 1, 0}, // 16
		{2, 1, 1, 1, 2}, // 17
		{0, 2, 0, 2, 0}, // 18

		{2, 0, 2, 0, 2}, // 19
		{0, 2, 2, 2, 0}, // 20
		{2, 0, 0, 0, 2}, // 21

		{0, 0, 2, 0, 0}, // 22
		{2, 2, 0, 2, 2}, // 23
		{0, 2, 1, 2, 0}, // 24
		{2, 0, 1, 0, 2}, // 25
	}

	// 測試單線
	/*
		line_setting := [25][5]int{
			{1, 1, 1, 1, 1}, // 1
			{1, 1, 1, 1, 1}, // 2
			{1, 1, 1, 1, 1}, // 3
			{1, 1, 1, 1, 1}, // 4
			{1, 1, 1, 1, 1}, // 5
			{1, 1, 1, 1, 1}, // 6
			{1, 1, 1, 1, 1}, // 7
			{1, 1, 1, 1, 1}, // 8
			{1, 1, 1, 1, 1}, // 9
			{1, 1, 1, 1, 1}, // 10
			{1, 1, 1, 1, 1}, // 11
			{1, 1, 1, 1, 1}, // 12
			{1, 1, 1, 1, 1}, // 13
			{1, 1, 1, 1, 1}, // 14
			{1, 1, 1, 1, 1}, // 15
			{1, 1, 1, 1, 1}, // 16
			{1, 1, 1, 1, 1}, // 17
			{1, 1, 1, 1, 1}, // 18
			{1, 1, 1, 1, 1}, // 19
			{1, 1, 1, 1, 1}, // 20
			{1, 1, 1, 1, 1}, // 21
			{1, 1, 1, 1, 1}, // 22
			{1, 1, 1, 1, 1}, // 23
			{1, 1, 1, 1, 1}, // 24
			{1, 1, 1, 1, 1}, // 25
		}
	*/

	fmt.Println("Loop line")
	for i, list := range line_setting {
		fmt.Println(i, list)
	}

	//先不考慮S1, S1另外算拉.
	lineable_list := []string{"H1", "H2", "H3", "H4", "H5", "L1", "L2", "L3", "L4", "L5", "L6"}
	//wild_list := []string{"W1"}
	valid_wild_map := map[string]bool{"W1": true}

	fmt.Println("Loop liable list:")
	for i, symbol := range lineable_list {
		fmt.Println(i, symbol)
	}

	// H1, 2, 3, 4, 5, L1, 2, 3, 4, 5, 6
	pay_table := map[string][]int{
		"H1": {0, 2, 30, 200, 750}, // h1
		"H2": {0, 2, 30, 100, 750}, // h2
		"H3": {0, 0, 25, 75, 400},  // h3
		"H4": {0, 0, 20, 75, 300},  // h4
		"H5": {0, 0, 20, 50, 300},  // h5
		"L1": {0, 0, 15, 30, 150},  // l1
		"L2": {0, 0, 15, 30, 150},  // l2
		"L3": {0, 0, 10, 25, 130},  // l3
		"L4": {0, 0, 10, 25, 130},  // l4
		"L5": {0, 0, 5, 20, 100},   // l5
		"L6": {0, 2, 5, 20, 100},   // l6
	}

	// W1
	wild_pay_table := []int{0, 35, 250, 2500, 10000}

	const i_one_size = 127
	const i_one_size_extend = i_one_size + 2

	const i_two_size = 131
	const i_two_size_extend = i_two_size + 2

	const i_thr_size = 141
	const i_thr_size_extend = i_thr_size + 2

	const i_fou_size = 139
	const i_fou_size_extend = i_fou_size + 2

	const i_fiv_size = 137
	const i_fiv_size_extend = i_fiv_size + 2

	const bet_amount = 10000
	const numberOfLine = 25
	const setting_runs = 500000 // 1000w

	//#######################################################################
	// 👩🏽‍🏫 laisser-moi vous expliquer dans un example simple , vous  xx.
	// 👩🏽‍🏫 laissez-moi                                       , vous imbecile.

	// 👩🏽‍🏫 i_one_size = 4 ,   [ "H1", "H2", "H3","H4"],
	// 👩🏽‍🏫 index=0 , h1,h2,h3,  index=1, h2,h3,h4,  index=2, h3,h4,h1,  index-3, h4,h1,h2
	// 👩🏽‍🏫     random index from 0~3, so ja_random_generator(4)  >>  (formula: i_one_size )
	// 👩🏽‍🏫

	/*******************************************  Loading CSV !!!!! String  ********************************************/

	// Open the file
	csvfile, err := os.Open("ja_actuary_line_csv_no_wild.csv")
	if err != nil {
		log.Fatalln("Couldn't open the csv file", err)
	}

	mg_col_un := make([]string, 0)
	mg_col_de := make([]string, 0)
	mg_col_tr := make([]string, 0)
	mg_col_qu := make([]string, 0)
	mg_col_ci := make([]string, 0)

	// Parse the file
	r := csv.NewReader(csvfile)

	col_un_cnt := 0
	col_de_cnt := 0
	col_tr_cnt := 0
	col_qu_cnt := 0
	col_ci_cnt := 0

	// Acrtuary  check the random geneartoir

	for {
		// Read each record from csv
		record, err := r.Read()

		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		if record[0] != "" {
			col_un_cnt++
			mg_col_un = append(mg_col_un, record[0])

			// cnt += 1 [col_0][symbol_index]
			actuary_Col_SymbolIndex_cnt_distribution[0][symbols_map_by_str[record[0]]] += 1
		}
		if record[1] != "" {
			col_de_cnt++
			mg_col_de = append(mg_col_de, record[1])
			actuary_Col_SymbolIndex_cnt_distribution[1][symbols_map_by_str[record[1]]] += 1
		}

		if record[2] != "" {
			col_tr_cnt++
			mg_col_tr = append(mg_col_tr, record[2])
			actuary_Col_SymbolIndex_cnt_distribution[2][symbols_map_by_str[record[2]]] += 1
		}

		if record[3] != "" {
			col_qu_cnt++
			mg_col_qu = append(mg_col_qu, record[3])
			actuary_Col_SymbolIndex_cnt_distribution[3][symbols_map_by_str[record[3]]] += 1
		}

		if record[4] != "" {
			col_ci_cnt++
			mg_col_ci = append(mg_col_ci, record[4])
			actuary_Col_SymbolIndex_cnt_distribution[4][symbols_map_by_str[record[4]]] += 1
		}

		fmt.Printf("Loading:  %s, %s, %s, %s, %s\n",
			record[0], record[1], record[2], record[3], record[4])
	}

	// Afficher the size
	fmt.Printf("[Loading] the csv file:  col(0,1,2,3,4) =  (%2d, %2d, %2d, %2d, %2d) \n",
		col_un_cnt, col_de_cnt, col_tr_cnt, col_qu_cnt, col_ci_cnt)

	// 尾巴加上兩個. [0] [1]
	mg_col_un = append(mg_col_un, mg_col_un[0])
	mg_col_un = append(mg_col_un, mg_col_un[1])
	fmt.Printf("Converted Extend Col_Un at the end.... please check\n%s\n\n", mg_col_un)
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	fmt.Println(text)

	// 尾巴加上兩個. [0] [1]
	mg_col_de = append(mg_col_de, mg_col_de[0])
	mg_col_de = append(mg_col_de, mg_col_de[1])
	fmt.Printf("Converted Extend Col_de at the end.... please check\n%s\n\n", mg_col_de)
	reader = bufio.NewReader(os.Stdin)
	text, _ = reader.ReadString('\n')
	fmt.Println(text)

	// 尾巴加上兩個. [0] [1]
	mg_col_tr = append(mg_col_tr, mg_col_tr[0])
	mg_col_tr = append(mg_col_tr, mg_col_tr[1])
	fmt.Printf("Converted Extend Col_tr at the end.... please check\n%s\n\n", mg_col_tr)
	reader = bufio.NewReader(os.Stdin)
	text, _ = reader.ReadString('\n')
	fmt.Println(text)

	// 尾巴加上兩個. [0] [1]
	mg_col_qu = append(mg_col_qu, mg_col_qu[0])
	mg_col_qu = append(mg_col_qu, mg_col_qu[1])
	fmt.Printf("Converted Extend Col_qu at the end.... please check\n%s\n\n", mg_col_qu)
	reader = bufio.NewReader(os.Stdin)
	text, _ = reader.ReadString('\n')
	fmt.Println(text)

	// 尾巴加上兩個. [0] [1]
	mg_col_ci = append(mg_col_ci, mg_col_ci[0])
	mg_col_ci = append(mg_col_ci, mg_col_ci[1])
	fmt.Printf("Converted Extend Col_ci at the end.... please check\n%s\n\n", mg_col_ci)
	reader = bufio.NewReader(os.Stdin)
	text, _ = reader.ReadString('\n')
	fmt.Println(text)

	// 確認比對試算表
	fmt.Println("Distribution:  with each symbols [0] ........       ", actuary_Col_SymbolIndex_cnt_distribution[0])
	fmt.Println("Distribution:  with each symbols [1] ........       ", actuary_Col_SymbolIndex_cnt_distribution[1])
	fmt.Println("Distribution:  with each symbols [2] ........       ", actuary_Col_SymbolIndex_cnt_distribution[2])
	fmt.Println("Distribution:  with each symbols [3] ........       ", actuary_Col_SymbolIndex_cnt_distribution[3])
	fmt.Println("Distribution:  with each symbols [4] ........       ", actuary_Col_SymbolIndex_cnt_distribution[4])
	reader = bufio.NewReader(os.Stdin)
	text, _ = reader.ReadString('\n')
	fmt.Println(text)

	/********************************************************************************************************/

	// Let's copy the main game symbols: 131 129 149 139 137
	//mg_col_un := [i_one_size_extend]string{"L6", "H1", "L1", "L2", "H4", "L5", "L1", "L1", "L5", "L2", "L4", "L4", "L6", "L3", "L4", "H2", "L1", "L2", "L1", "L2", "L6", "L4", "L6", "L2", "L4", "L6", "S1", "W1", "L5", "L3", "L1", "L3", "H1", "L5", "L5", "H3", "L3", "L5", "H2", "L3", "L3", "L2", "L1", "L3", "L4", "W1", "L3", "L1", "L3", "L2", "L6", "L6", "L4", "L2", "H4", "L3", "L5", "L2", "L2", "H3", "L5", "L4", "L5", "S1", "L3", "L5", "L5", "L5", "L4", "L6", "H1", "L6", "L4", "L3", "L3", "L5", "L6", "L5", "W1", "L5", "L5", "L6", "L6", "L3", "L6", "L4", "H1", "L2", "H4", "L6", "L3", "L5", "L6", "L2", "W1", "H3", "L6", "L2", "L6", "L5", "L6", "L5", "L6", "L5", "L6", "L4", "L2", "L4", "L4", "L5", "S1", "L1", "L1", "L6", "L4", "S1", "L5", "L1", "H4", "L4", "L2", "L6", "H2", "L1", "L2", "H4", "L4", "L4", "L4", "H1", "L5",
	//	"L6", "H1"} // 🌽 add extra [0], [1] to the end of the list.
	//mg_col_de := [i_two_size_extend]string{"L6", "H1", "L1", "L2", "L4", "L5", "L1", "L4", "L5", "L2", "H3", "L1", "L6", "L5", "L4", "L5", "L1", "L2", "L1", "H1", "L3", "L4", "H2", "L5", "L6", "L6", "L6", "W1", "L5", "L3", "L1", "L6", "L1", "L5", "S1", "H2", "L3", "L5", "H2", "L3", "L3", "L2", "L1", "L3", "L4", "W1", "L3", "L1", "L3", "H1", "L6", "L3", "L4", "L2", "H4", "L3", "L5", "L2", "L2", "H3", "L5", "L4", "L5", "S1", "L3", "L5", "L1", "L5", "L4", "L6", "H1", "L6", "L4", "L3", "L3", "L5", "L6", "H2", "W1", "L5", "L5", "L6", "H2", "L3", "L6", "L4", "H1", "L2", "H4", "L6", "L3", "L5", "L6", "L2", "W1", "H3", "L6", "L2", "L6", "L5", "H3", "H1", "L6", "H3", "L6", "L4", "L2", "L4", "L4", "L5", "S1", "L1", "L1", "L6", "L4", "S1", "L5", "L1", "H4", "L4", "L2", "L6", "H2", "L1", "L2", "H4", "L4", "L4", "L4",
	//	"L6", "H1"} // 🌽 add extra
	//mg_col_tr := [i_thr_size_extend]string{"W1", "L4", "L3", "L5", "H2", "L4", "H4", "L3", "L3", "L2", "H1", "L4", "L6", "L3", "H4", "L1", "L1", "L1", "L6", "L6", "H1", "L1", "L5", "S1", "L1", "H1", "L4", "L6", "H2", "L2", "L4", "H3", "L6", "L6", "H1", "L1", "L6", "H4", "L1", "L5", "H2", "L1", "L2", "L3", "L2", "H2", "L3", "L4", "L4", "L6", "H3", "L2", "L2", "L5", "L5", "H4", "L4", "L3", "L4", "L3", "L6", "L6", "L6", "L5", "L5", "L5", "L1", "L6", "L2", "L2", "H1", "L2", "L4", "L4", "L6", "L3", "L3", "L1", "L3", "L1", "W1", "L2", "L1", "L2", "S1", "L5", "L6", "H3", "L1", "L6", "L1", "H4", "L4", "L3", "H2", "L3", "H4", "L3", "L4", "L6", "L2", "H3", "L5", "L2", "H4", "L5", "L6", "L6", "H1", "L5", "S1", "L5", "L4", "H2", "L5", "L5", "H3", "W1", "L5", "H2", "L1", "L4", "L6", "L5", "H1", "L4", "L5", "L5", "H3", "L5", "L4", "L2", "S1", "L3", "L3", "H4", "L4", "L4", "H3", "L3", "L2", "H3", "L2", "L6", "L6", "W1", "L1", "L3", "L2",
	//	"W1", "L4"} // 🌽 add
	//mg_col_qu := [i_fou_size_extend]string{"W1", "L2", "H2", "L2", "S1", "L4", "H3", "L6", "L2", "H4", "L4", "L3", "L5", "L5", "L5", "L4", "H3", "L3", "L6", "L4", "H2", "L1", "L3", "L6", "L1", "L4", "L4", "L3", "W1", "L6", "L1", "H4", "L3", "L3", "H3", "H2", "L4", "L4", "L3", "L2", "H3", "H2", "L5", "H1", "L5", "L4", "L3", "L4", "H4", "L5", "H1", "L6", "L1", "L1", "L3", "H2", "H4", "L2", "H4", "L3", "L3", "H3", "L6", "L2", "S1", "H3", "W1", "L2", "L1", "H1", "L6", "L5", "L1", "H3", "L4", "L4", "L6", "H1", "L3", "L4", "L6", "H3", "L2", "S1", "L5", "H4", "L6", "L2", "L6", "W1", "L2", "H2", "H4", "L6", "L1", "L5", "L4", "L6", "L6", "L5", "H1", "L1", "L4", "L5", "H3", "L2", "L1", "H3", "L3", "L4", "H2", "H4", "L5", "H1", "L5", "H2", "L6", "H1", "L6", "L1", "H2", "L5", "L5", "H4", "L6", "L2", "H4", "L3", "L5", "H1", "S1", "H1", "L5", "H2", "L6", "H1", "L6", "L1", "H2",
	//	"W1", "L2"} // 🌽 add
	//mg_col_ci := [i_fiv_size_extend]string{"L6", "L2", "H2", "L2", "S1", "L4", "H3", "L6", "L2", "H4", "L4", "L3", "L5", "L5", "L5", "L4", "H3", "L3", "L6", "L4", "H2", "L1", "L3", "W1", "L1", "L4", "L4", "L3", "W1", "L6", "L1", "H4", "L3", "L3", "H3", "H2", "L4", "L4", "L3", "L2", "H3", "H2", "L5", "H1", "L5", "L4", "L3", "L4", "H4", "L5", "H1", "L6", "L1", "L1", "L3", "H2", "H4", "L2", "H4", "L3", "L3", "H3", "L6", "L2", "S1", "H3", "W1", "L2", "L1", "H1", "L6", "L5", "L1", "H3", "L4", "L4", "L6", "H1", "L3", "L4", "L6", "H3", "L2", "S1", "L5", "H4", "L6", "L2", "L6", "W1", "L2", "H2", "H4", "L6", "L1", "L5", "L4", "L6", "L6", "L5", "H1", "L1", "L4", "L5", "H3", "L2", "L1", "H3", "L3", "L4", "H2", "H4", "L5", "H1", "L5", "H2", "L6", "H1", "L6", "L1", "H2", "L5", "L5", "H4", "L6", "L2", "H4", "L3", "L5", "H1", "S1", "H1", "L5", "H2", "L6", "H1", "L6",
	//	"L6", "L2"} // 🌽 add ...

	fmt.Println(mg_col_un[0], mg_col_un[1], mg_col_un[2])
	fmt.Println(mg_col_de[0], mg_col_de[1], mg_col_de[2])
	fmt.Println(mg_col_tr[0], mg_col_tr[1], mg_col_tr[2])
	fmt.Println(mg_col_qu[0], mg_col_qu[1], mg_col_qu[2])
	fmt.Println(mg_col_ci[0], mg_col_ci[1], mg_col_ci[2])

	total_gain := 0
	main_rtp := 0

	actuary_h1_win_two_cnt := 0
	actuary_h2_win_two_cnt := 0
	actuary_h3_win_two_cnt := 0
	actuary_h4_win_two_cnt := 0
	actuary_h5_win_two_cnt := 0
	actuary_l1_win_two_cnt := 0
	actuary_l2_win_two_cnt := 0
	actuary_l3_win_two_cnt := 0
	actuary_l4_win_two_cnt := 0
	actuary_l5_win_two_cnt := 0
	actuary_l6_win_two_cnt := 0
	actuary_w1_win_two_cnt := 0

	actuary_rtp_de := 0
	actuary_rtp_tr := 0
	actuary_rtp_qu := 0
	actuary_rtp_ci := 0

	for run_cnt := 0; run_cnt < setting_runs; run_cnt++ {

		//隨機選
		i_un := obtenir_random_integer(i_one_size)
		i_de := obtenir_random_integer(i_two_size)
		i_tr := obtenir_random_integer(i_thr_size)
		i_qu := obtenir_random_integer(i_fou_size)
		i_ci := obtenir_random_integer(i_fiv_size)

		//精算確認:
		actuary_check_random_cnt_distribution[0][i_un] += 1
		actuary_check_random_cnt_distribution[1][i_de] += 1
		actuary_check_random_cnt_distribution[2][i_tr] += 1
		actuary_check_random_cnt_distribution[3][i_qu] += 1
		actuary_check_random_cnt_distribution[4][i_ci] += 1

		//取得盤面
		fmt.Println("Random Table:")
		mg_table := [5][3]string{
			{mg_col_un[i_un], mg_col_un[i_un+1], mg_col_un[i_un+2]},
			{mg_col_de[i_de], mg_col_de[i_de+1], mg_col_de[i_de+2]},
			{mg_col_tr[i_tr], mg_col_tr[i_tr+1], mg_col_tr[i_tr+2]},
			{mg_col_qu[i_qu], mg_col_qu[i_qu+1], mg_col_qu[i_qu+2]},
			{mg_col_ci[i_ci], mg_col_ci[i_ci+1], mg_col_ci[i_ci+2]},
		}

		/*
			fmt.Println("Skip the ..... random value ", i_un, i_de, i_tr, i_qu, i_ci)
			mg_table := [5][3]string{
				{"W1", "L1", "l1"},
				{"W1", "L2", "L2"},
				{"L6", "H1", "H1"},
				{"L4", "L4", "L4"},
				{"L5", "L5", "L5"},
			}
		*/

		// Output
		fmt.Println("The run id: ", run_cnt, "\n", mg_table)

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

		//count each obj and gain

		// loop each obj
		var current_win_line int
		var currentGain int     //obj_gain
		var currentWildGain int //wild_gain
		var finalGain int       //Finalgain, eigher obj_gain or wild_gain
		var count int
		for _, input_obj := range lineable_list {
			// loop each line
			for line_index, tem_list := range line_setting {
				check_obj := "" //不包括Ｓ1,另外算.
				count = 0
				current_win_line = 0

				currentGain = 0
				currentWildGain = 0

				// ❶Debug_01: tem_symbol := make([]string, 0)
				for col_index := 0; col_index < 5; col_index++ {
					count++
					current_symbol := mg_table[col_index][tem_list[col_index]]

					if current_symbol != input_obj && !valid_wild_map[current_symbol] {

						// fmt.Println("幹: the current_symbol != input_obj && !valid_wild_map[current_symbol")
						// fmt.Println("   current_symbol: ", current_symbol)
						// fmt.Println("   input_obj     : ", input_obj)
						// fmt.Println("   count         : ", count)

						// 停一下
						// reader = bufio.NewReader(os.Stdin)
						// text, _ = reader.ReadString('\n')
						// fmt.Println(text)

						break
					} else if valid_wild_map[current_symbol] {
						if !valid_wild_map[input_obj] {
							current_win_line = count

							fmt.Println("Current_win_line:  ", current_win_line)
							reader = bufio.NewReader(os.Stdin)
							text, _ = reader.ReadString('\n')
							fmt.Println(text)

						} else {
							check_obj = input_obj
							current_win_line = count
						}
					} else if current_symbol == input_obj {
						check_obj = input_obj
						current_win_line = count
					}

					//fmt.Println("obj: ", obj, " line_index: ", line_index, " with col: ", col_index, "symbol: ", _tem_symbol)
					// ❶Debug_01: tem_symbol = append(tem_symbol, _tem_symbol)

					// 等等做bet amount
					if current_win_line >= 2 && check_obj != "" {
						// 💰: set currentGain
						win_line_to_index := current_win_line - 1
						currentGain = bet_amount * pay_table[check_obj][win_line_to_index] * 1 / numberOfLine

						fmt.Println(run_cnt, ":[Found]: Bet amount = ", bet_amount, " pay: ", pay_table[check_obj][win_line_to_index], " currentGain: ", currentGain, " obj: ", input_obj, " win_line: ", current_win_line)

						// 💰 來確認一下Wild吧
						wild_count := 0
						wild_current_win_line := 0
						for checkW_col_index := 0; checkW_col_index < 5; checkW_col_index++ {
							wild_count++
							current_symbol = mg_table[checkW_col_index][tem_list[checkW_col_index]]

							// If the current_symbol in wild_list
							if valid_wild_map[current_symbol] {
								wild_current_win_line = wild_count
							} else { //means the curr_obj is not wild
								break
							}
						}

						// 💰: set currentWildGain
						if wild_current_win_line >= 2 {

							wild_win_line_to_index := wild_current_win_line - 1
							currentWildGain = bet_amount * wild_pay_table[wild_win_line_to_index] * 1 / numberOfLine
							fmt.Println(run_cnt, ":[Found]: Bet amount = ", bet_amount, " pay: ", wild_pay_table[wild_win_line_to_index], " currentWildGain: ", currentWildGain, " 'W1':  wild_win_line ", wild_current_win_line)

						} else {
							currentWildGain = 0
						}

						// 💰: Compare wild_gain and obj_gain !!
						if currentGain > currentWildGain {

							//💰:
							finalGain += currentGain // currentGain = obj_gain
							total_gain += currentGain
							fmt.Printf("[Finally}: Winning with obj:  %s   ,  winning_line:  %d,  win_number: %d, with currentGain:  %d\n\n", input_obj, line_index+1, current_win_line, currentGain)

							// See See win_two distribution
							if current_win_line == 2 {

								//💰 check line 2,3,4,5 distribution
								actuary_rtp_de += currentGain

								if input_obj == "H1" {
									actuary_h1_win_two_cnt++
								}

								if input_obj == "H2" {
									actuary_h2_win_two_cnt++
								}

								if input_obj == "H3" {
									actuary_h3_win_two_cnt++
								}

								if input_obj == "H4" {
									actuary_h4_win_two_cnt++
								}

								if input_obj == "H5" {
									actuary_h5_win_two_cnt++
								}

								if input_obj == "L1" {
									actuary_l1_win_two_cnt++
								}
								if input_obj == "L2" {
									actuary_l2_win_two_cnt++
								}
								if input_obj == "L3" {
									actuary_l3_win_two_cnt++
								}
								if input_obj == "L4" {
									actuary_l4_win_two_cnt++
								}
								if input_obj == "L5" {
									actuary_l5_win_two_cnt++
								}
								if input_obj == "L6" {
									actuary_l6_win_two_cnt++
								}

							} else if current_win_line == 3 {
								//💰 check line 2,3,4,5 distribution
								actuary_rtp_tr += currentGain
							} else if current_win_line == 4 {
								//💰 check line 2,3,4,5 distribution
								actuary_rtp_qu += currentGain
							} else if current_win_line == 5 {
								//💰 check line 2,3,4,5 distribution
								actuary_rtp_ci += currentGain
							}

						} else if currentGain < currentWildGain {
							//💰:
							finalGain += currentWildGain //currentWildGain , wild_gain
							total_gain += currentWildGain
							fmt.Printf("[Finally}: Winning with obj:  %s   ,  winning_line:  %d,  win_number: %d, with currentWildGain:  %d\n\n", "W1", line_index+1, wild_current_win_line, currentWildGain)

							if wild_current_win_line == 2 {
								actuary_w1_win_two_cnt++
							}

							if wild_current_win_line == 2 {
								//💰 check line 2,3,4,5 distribution
								actuary_rtp_de += currentWildGain
							} else if wild_current_win_line == 3 {
								//💰 check line 2,3,4,5 distribution
								actuary_rtp_tr += currentWildGain
							} else if wild_current_win_line == 4 {
								//💰 check line 2,3,4,5 distribution
								actuary_rtp_qu += currentWildGain
							} else if wild_current_win_line == 5 {
								//💰 check line 2,3,4,5 distribution
								actuary_rtp_ci += currentWildGain
							}

						} else if currentGain == 0 && currentWildGain == 0 {
							continue
						} else {
							panic("Wild_gain =  Obj_gain, please check")
						}
					}
				}

				// Display each line_index
				//fmt.Println("obj: ", obj, "  Outside of the loop")
				// ❶Debug_01: fmt.Println(tem_symbol)
			}
		}

		//show each run
		if run_cnt != 0 {
			fmt.Printf("[%d]:  with current_gain  %4d with toal_gain  %4d,   curr_rtp  %4d\n", run_cnt, finalGain, total_gain, total_gain/(run_cnt+1))
		}

		finalGain = 0

		/*
			fmt.Printf("[Jean]: Bonjour !\nThe rtp*10000  est:    %4d    \n", main_rtp)
			fmt.Println("The actuary_check win_line_two:      h1     cnt=   ", actuary_h1_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      h2     cnt=   ", actuary_h2_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      h3     cnt=   ", actuary_h3_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      h4     cnt=   ", actuary_h4_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      h5     cnt=   ", actuary_h5_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      l1     cnt=   ", actuary_l1_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      l2     cnt=   ", actuary_l2_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      l3     cnt=   ", actuary_l3_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      l4     cnt=   ", actuary_l4_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      l5     cnt=   ", actuary_l5_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      l6     cnt=   ", actuary_l6_win_two_cnt) //cnt / 25 !!
			fmt.Println("The actuary_check win_line_two:      w1     cnt=   ", actuary_w1_win_two_cnt) //cnt / 25 !!

			// Input...
			reader = bufio.NewReader(os.Stdin)
			text, _ = reader.ReadString('\n')
			fmt.Println(text)
		*/

	}

	// 精算確認Random Generator
	fmt.Println("The random geneargor distribution:                 ", actuary_check_random_cnt_distribution[0])
	fmt.Println("The random geneargor distribution:                 ", actuary_check_random_cnt_distribution[1])
	fmt.Println("The random geneargor distribution:                 ", actuary_check_random_cnt_distribution[2])
	fmt.Println("The random geneargor distribution:                 ", actuary_check_random_cnt_distribution[3])
	fmt.Println("The random geneargor distribution:                 ", actuary_check_random_cnt_distribution[4])

	main_rtp = total_gain / setting_runs
	fmt.Printf("[Jean]: Bonjour !\nThe rtp*10000  est:    %4d    \n", main_rtp)
	fmt.Println("The actuary_check win_line_two:      h1     cnt=   ", actuary_h1_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      h2     cnt=   ", actuary_h2_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      h3     cnt=   ", actuary_h3_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      h4     cnt=   ", actuary_h4_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      h5     cnt=   ", actuary_h5_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      l1     cnt=   ", actuary_l1_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      l2     cnt=   ", actuary_l2_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      l3     cnt=   ", actuary_l3_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      l4     cnt=   ", actuary_l4_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      l5     cnt=   ", actuary_l5_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      l6     cnt=   ", actuary_l6_win_two_cnt/numberOfLine) //cnt / 25 !!
	fmt.Println("The actuary_check win_line_two:      w1     cnt=   ", actuary_w1_win_two_cnt/numberOfLine) //cnt / 25 !!

	//Check each rtp ,2,3,4,5
	fmt.Printf("The fucking win 2, 3, 4, 5 distribution rtp ext [*1000]   %4d", actuary_rtp_de/setting_runs)
	fmt.Printf("The fucking win 2, 3, 4, 5 distribution rtp ext [*1000]   %4d", actuary_rtp_tr/setting_runs)
	fmt.Printf("The fucking win 2, 3, 4, 5 distribution rtp ext [*1000]   %4d", actuary_rtp_qu/setting_runs)
	fmt.Printf("The fucking win 2, 3, 4, 5 distribution rtp ext [*1000]   %4d", actuary_rtp_ci/setting_runs)

}
