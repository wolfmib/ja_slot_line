package main

import (
	//"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
)

func main() {
	// Open the file
	csvfile, err := os.Open("ja_actuary_line_csv.csv")
	if err != nil {
		log.Fatalln("Couldn't open the csv file", err)
	}

	// Parse the file
	r := csv.NewReader(csvfile)
	//r := csv.NewReader(bufio.NewReader(csvfile))

	// Iterate through the records

	col_un_cnt := 0
	col_de_cnt := 0
	col_tr_cnt := 0
	col_qu_cnt := 0
	col_ci_cnt := 0

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
		}

		if record[1] != "" {
			col_de_cnt++
		}

		if record[2] != "" {
			col_tr_cnt++
		}

		if record[3] != "" {
			col_qu_cnt++
		}

		if record[4] != "" {
			col_ci_cnt++
		}

		fmt.Printf("Loading:  %s, %s, %s, %s, %s\n",
			record[0], record[1], record[2], record[3], record[4])

	}

	// Afficher the size
	fmt.Printf("The final col(0,1,2,3,4) =  (%2d, %2d, %2d, %2d, %2d) ",
		col_un_cnt, col_de_cnt, col_tr_cnt, col_qu_cnt, col_ci_cnt)
}
