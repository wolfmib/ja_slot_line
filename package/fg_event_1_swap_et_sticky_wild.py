



"""


張飛 🕵🏻‍♂️

SWAP WILD &  STICKY WILD
    Re-spin期間，當盤面上出現張飛symbol時，都會被轉換成wild並綁定在盤面上，直到re-spin次數結束。

Performance
    張飛角色快速向前移動出畫面，出現在畫面前，怒吼後便形成獸型態，盤面上所有張飛symbol轉換成wild。

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
def swap_et_sticky(input_list_r,
         mask_list_r,
         i_from="H1",
         i_to  ="W1"):

    # copy template
    tem_list_r = copy.deepcopy(input_list_r)


    # 👨‍⚕️: calculate W symbols static for further analysis
    wild_cnts = 0 


    # H1 -> W1 et sticky 
    for col_ ,any_col_list in enumerate(tem_list_r):
        for row_ , any_obj in enumerate(any_col_list):

            # Faire Mask
            if any_obj == i_from:  #obj == H1
                mask_list_r[col_][row_] = i_to # W1
            else:
                pass
        
    # Overlap with mask:  Check W1 then replace
    for _col , any_col_list in enumerate(mask_list_r):
        for _row, any_obj in enumerate(any_col_list):

            if any_obj == i_to: #mask appear W1
                #faire list pour return 
                tem_list_r[_col][_row] = i_to  #overlap anyobj -> W1

                #each mask_overlap counts !! 
                wild_cnts += 1

    return tem_list_r, mask_list_r, wild_cnts




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


    

    _mask_list = [[  '  ', '  ', '  '], ['  '  , '  '  , '  '],['  '  , '  ' , '  ']  , ['  ' ,  '  ' ,  '  '],  [ '  ' ,  '  ' , '  ' ]]
    
    
    for i in range(3):
        
        input_list_r = test_generator()

        print("which run      ",i)
        print("input_lis=     ",input_list_r)
        print("mask_list=     ",_mask_list)
        print("----------------------------------------------")

        curr_list_r , _mask_list =  swap_et_sticky(input_list_r,_mask_list)
          
        print("curr_list=     ",curr_list_r)
        print("mask_list=     ",_mask_list)
        print("--------------------------------------\n\n")
    







