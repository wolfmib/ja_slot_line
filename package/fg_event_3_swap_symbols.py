



"""


李白  🍺
SWAP SYMBOL
Re-spin期間，每次spin都將會在盤面上任意位置，隨機產生1~5個wild。  [避掉Wild Table]

Performance
李白角色快速向前移動出畫面，出現在畫面前，攻擊動作演出後身影消失，多道劍影朝盤面上砍，盤面上任意1~5個symbol轉換成wild symbol。


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





def get_row():
    return int(random.choice([0,1,2]))

def get_col():
    return int(random.choice([0,1,2,3,4]))


#  wild_weight_list=[50,40,10] to give 3 wilds, 4 wilds or 5 wilds. 
def swap_wilds(input_list_r,\
                wild_weight_list=[50,20,15,10,5],\
                wild_nb_setting=[1,2,3,4,5],
                i_symbol = "W1"):


    # 👨‍⚕️: calculate W symbols static for further analysis
    wild_cnts = 0 


    # 🧊: for example: make 3,4,5  random wilds first with weight[ 50, 40, 10]
    pick_value = jason_random_generator_v1(1,100)

    if pick_value >=1 and pick_value <= wild_weight_list[0]:
        wild_cnts = wild_nb_setting[0]
    elif pick_value > wild_weight_list[0] and pick_value <= (wild_weight_list[0]+wild_weight_list[1]):
        wild_cnts = wild_nb_setting[1]

    elif pick_value > wild_weight_list[1] and pick_value <= (wild_weight_list[0]+wild_weight_list[1]+wild_weight_list[2]):
        wild_cnts = wild_nb_setting[2]

    elif pick_value > wild_weight_list[2] and pick_value <= (wild_weight_list[0]+wild_weight_list[1]+wild_weight_list[2]+wild_weight_list[3]):
        wild_cnts = wild_nb_setting[3]

    elif pick_value > (wild_weight_list[0]+wild_weight_list[1]+wild_weight_list[2]+wild_weight_list[3]) and pick_value <= 100:
        wild_cnts = wild_nb_setting[4]




    # Parameters
    wilds_being_set = 0
    initial_col_et_row_map_list = []
    return_list_r = copy.deepcopy(input_list_r)


    # wild_cnts = 3, 4, or 5 for example
    while wilds_being_set < wild_cnts:

        # get row et col
        curr_row = get_row()
        curr_col = get_col()

        tem_col_et_row = [curr_col,curr_row]

        if tem_col_et_row not in initial_col_et_row_map_list and input_list_r[curr_col][curr_row] != i_symbol:

            # set wilds
            return_list_r[curr_col][curr_row] = i_symbol

            # add set cnts
            wilds_being_set += 1

            # save to check_map
            initial_col_et_row_map_list.append(tem_col_et_row)

        else:
            pass
    
    return return_list_r, wild_cnts





# RANDOM.CHOICE(LIST)
def test_generator():
    list_symbol = ["H1","H2","H3","H4","L1","L2","L3","L4","L5","L6"]
    return_list = []
    for _col in range(5):
        row_list = []
        for _row in range(3):
            row_list.append(random.choice(list_symbol))
            
        return_list.append(row_list)
    
    return return_list




if __name__ == "__main__":
    print("Bonjour !")


    change_wild_symbol = "W1"
    i_wilds_nb = [1,2,3,4,5]
    i_wilds_weight = [50,20,15,10,5]
    



    wild_cnt_dict ={
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }


    run = 10000
    for i in range(run):
        
        #input_list_r = test_generator()

        input_list_r =[
            ["W1","W1","W1"],
            ["W1","W1","W1"],
            ["W1","W1","W1"],
            ["O","O","O"],
            ["O","O","O"]
        ]

        print("which run      ",i)
        print("input_lis=     ",input_list_r)
        print("----------------------------------------------")

        curr_list_r , curr_wild_cnts  =  swap_wilds(input_list_r,i_wilds_weight,i_wilds_nb,"W1")
        print("curr_list=                    ",curr_list_r)
        print("curr wild cnts =     ",curr_wild_cnts)
        print("--------------------------------------\n\n")

        wild_cnt_dict[curr_wild_cnts] += 1

    
    print(i_wilds_weight)
    for cnt_key in range(1,6):
        tem_ratio = float(wild_cnt_dict[cnt_key]/run)
        print("[%2d]:   with ratio   %.4f"%(cnt_key,tem_ratio))
    
        




