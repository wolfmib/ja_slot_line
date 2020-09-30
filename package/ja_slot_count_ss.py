# Input: list_r , cnt_symbol 
    # [['SC', 'W', 'J'], ['SS', 'SD', 'W'], ['SC', 'SS', 'SD'], ['W', 'SC', 'SD'], ['W', 'SC', 'J']] , "SS" 
    # [['SC', 'W', 'J'], ['SS', 'B', 'SS'], ['SS', 'A', 'SD'], ['SS', 'SC', 'SD'], ['W', 'SC', 'J']] , "SS"

# Output: numbers of ss 
    # Case 1 , 3
    # Case 2 , 4


def run(input_list_r, input_symbol):
    return_cnts = 0

    for any_list in input_list_r:
        for any_symbol in any_list:
            if any_symbol == input_symbol:
                return_cnts += 1

    return return_cnts


if __name__ == "__main__":

    test_case1 = [['SC', 'W', 'J'], ['SS', 'SD', 'W'], ['SC', 'SS', 'SD'], ['W', 'SC', 'SD'], ['W', 'SC', 'J']]
    test_case2 = [['SC', 'W', 'J'], ['SS', 'B', 'SS'], ['SS', 'A', 'SD'], ['SS', 'SC', 'SD'], ['W', 'SC', 'J']]

    symbol = "SS"

    print("test_case1:      ",test_case1)
    print("Result for cns symbol  %s     =   %d"%(symbol,run(test_case1,symbol)))





    print("test_case2:      ",test_case2)
    print("Result for cns symbol  %s     =   %d"%(symbol,run(test_case2,symbol)))