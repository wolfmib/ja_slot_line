

"""
 Start from slot-04:  In freegame,  in the middle of col, appear W1 , Enter Respin-Mode

Module for slot-04 and flexible in the future:
    - specific col             e.g. =  "2"   (col: 0,  1, 2, 3, 4, 5)
    - specific finding symbol, e.g. =  "W1"
    - return the counts of the searching symbol   ,  e.g. 0  1, 2, 3, etc...

"""




# Input: list_r , cnt_symbol 
    # [['SC', 'W', 'J'], ['SS', 'SD', 'W'], ['SC', 'SS', 'SD'], ['W', 'SC', 'SD'], ['W', 'SC', 'J']] , "SS" 
    # [['SC', 'W', 'J'], ['SS', 'B', 'SS'], ['SS', 'A', 'SD'], ['SS', 'SC', 'SD'], ['W', 'SC', 'J']] , "SS"

# Output: numbers of ss 
    # Case 1 , 3
    # Case 2 , 4


def run(input_list_r, input_symbol, input_col_index):
    return_cnts = 0


    # checking the index_col is doable
    len_of_cols = len(input_list_r)
    len_of_cols_max_index = len_of_cols - 1   # If len=5,  Max_col_index=4  e.g. col: 0 , 1, 2, 3, 4
    assert input_col_index <= len_of_cols_max_index or input_col_index >= 0

    # let's count the "W1" in the col of 3 (middle cols ) for example
    for col_index, any_list in enumerate(input_list_r):
        
        if col_index == input_col_index: 
            for any_symbol in any_list:
                if any_symbol == input_symbol:
                    return_cnts += 1

    return return_cnts


if __name__ == "__main__":

    test_case_zero     = [['H1', 'L1', 'L2'], ['L3', 'L4', 'L5'], ['H1', 'L1', 'H1'], ['L2', 'L3', 'L4'], ['L1', 'L2', ';3']]
    test_case_un       = [['H1', 'L1', 'L2'], ['L3', 'L4', 'L5'], ['W1', 'L1', 'H1'], ['L2', 'L3', 'L4'], ['L1', 'L2', ';3']]
    test_case_deux     = [['H1', 'L1', 'L2'], ['L3', 'L4', 'L5'], ['W1', 'L1', 'W1'], ['L2', 'L3', 'L4'], ['L1', 'L2', ';3']]
    test_case_trois    = [['H1', 'L1', 'L2'], ['L3', 'L4', 'L5'], ['W1', 'W1', 'W1'], ['L2', 'L3', 'L4'], ['L1', 'L2', ';3']]

    symbol = "W1"
    i_col_index = 2

    print("test_case_zero:      ",test_case_zero)
    print("symbol:            ",symbol)
    print("col_index:         ",i_col_index)
    print("Result for cns symbol  %s     =   %d"%(symbol,run(test_case_zero,symbol,i_col_index)))



    print("test_case_un:      ",test_case_un)
    print("symbol:            ",symbol)
    print("col_index:         ",i_col_index)
    print("Result for cns symbol  %s     =   %d"%(symbol,run(test_case_un,symbol,i_col_index)))

    print("test_case_deux:      ",test_case_deux)
    print("symbol:            ",symbol)
    print("col_index:         ",i_col_index)
    print("Result for cns symbol  %s     =   %d"%(symbol,run(test_case_deux,symbol,i_col_index)))

    print("test_case_trois:      ",test_case_trois)
    print("symbol:            ",symbol)
    print("col_index:         ",i_col_index)
    print("Result for cns symbol  %s     =   %d"%(symbol,run(test_case_trois,symbol,i_col_index)))