



"""

后羿 🏹
EXPANDING SYMBOL
Re-spin期間，當盤面上出現wild symbol時，都會被延展成全排wild。

Performance
后羿角色快速向前移動出畫面並在第一次中獎表演結束後，出現在畫面，拉弓射箭並召喚出鳳凰飛過盤面，盤面上的wild symbol延展動態演出，再次進行中獎判斷演出。

"""


import random
import copy



####################### Readme ###########################
# slot_bet_rate_agent() -> slot_bet_rate_class()
##########################################################

# random geneartor python verrsion (compare to golang version):
    # This is version is not good
    # --------------------------------
        # Obtenir la loop from randint(1,5)
        # Prends  seed  +=  random number (1,100000) avec serveral times
        # Obtenir la numero et mettre dans la seed
        # Prends la random number (1, 131) etc..
    #----------------------
    # Try another one
        #  Obtenir la loop from randint(1,5)
        #  Prends for loop , random_number = randint(1,131)
        #  Prends la derineer random number

# Jira-Ticket: DAT-147

def jason_random_generator_v1(low_number, high_number):
    # Obtenir times 
    """
    get_times = random.randint(1,5)
    my_seed      = 0 
    for _ in range(get_times):
        my_seed += random.randint(1,100000)
    random.seed(my_seed)
    """
    get_times = random.randint(1,5)
    for _ in range(get_times):
        my_random = random.randint(low_number,high_number)
    
    return my_random



#
def expand_symbols(input_list_r,
         i_symbol="H1"):

    # 👨‍⚕️: calculate W symbols static for further analysis
    wild_cnts = 0 

    # copy template
    tem_list_r = copy.deepcopy(input_list_r)

    # return_list
    return_list_r = []

    # H1 -> W1 et sticky 
    for col_ ,any_col_list in enumerate(tem_list_r):
        
        # symbol in any row_list ["O","O","V" ]
        if i_symbol in any_col_list:

            # Expand!
            make_tem_list = []
            for _ in any_col_list:
                make_tem_list.append(i_symbol)
                wild_cnts += 1
            return_list_r.append(make_tem_list)

        else:
            # Copy original tem_list.
            return_list_r.append(any_col_list)
    return return_list_r, wild_cnts




# RANDOM.CHOICE(LIST)
def test_generator():
    list_symbol = ["H1","H2","H3","H4","L1","L2","L3","L4","L5","L6","W1"]
    return_list = []
    for _col in range(5):
        row_list = []
        for _row in range(3):
            row_list.append(random.choice(list_symbol))
            
        return_list.append(row_list)
    
    return return_list




if __name__ == "__main__":
    print("Bonjour !")


    expected_expand_symbol = "W1"
    
    for i in range(10):
        
        input_list_r = test_generator()

        print("which run      ",i)
        print("input_lis=     ",input_list_r)
        print("mask_list=     ",expected_expand_symbol)
        print("----------------------------------------------")

        curr_list_r , curr_expand_cnts  =  expand_symbols(input_list_r,expected_expand_symbol)
          
        print("curr_list=                    ",curr_list_r)
        print("curr expand symbol cnts =     ",curr_expand_cnts)
        print("--------------------------------------\n\n")



    
    # Let's try the static for each single spin.
    wilds_cnt = 0
    run = 1000
    run_cnt = 0
    for i in range(run):
        run_cnt += 1
        input_list_r = [ ["W1","O","O"],["O","O","O"],["O","O","O"],["X","O","O"],["X","O","O"],["X","O","O"],]
    
        curr_list_r, curr_expand_cnts = expand_symbols(input_list_r,expected_expand_symbol)

        wilds_cnt += curr_expand_cnts
        if run % 100 == 1:
            print("run:   %4d  with current wild_cnts :    %4d"%(run_cnt,wilds_cnt))

    
    single_wild_avg = float(wilds_cnt / run)
    print("run:  %4d    , with wild_avg  %.4f "%(run,single_wild_avg))










