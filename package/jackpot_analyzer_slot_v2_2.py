import os
import xlrd
import random
import collections
import sys
import copy
import json
from datetime import date
import datetime
import argparse
import numpy as np
import time

import requests
import json

import pandas as pd

# 🏢 load package first, it's important
try:
    import package.analyzer_system as ana_sys
except:
    import analyzer_system as na_sys







"""
🎹 🎹 v2 version: 
    - support S1, E1, H1, W1 etc.. format
    - support output package print out
    - for example, if we meet W1, W2, W3 , we can pick first char [0] == W  


#  🌟🌟   load v2.1 version:  
#                 1. support prevent checking S1 inside the rtp_agent.run() . 
#                 2. S1 count logic is being iplement outside the libs.

##        load v2.2 version:
#                 1. let's add the return , 2, 3, 4, 5 gain.
"""





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
    


# become_which_target = "W" for example
def slot_overwrite_list_by_target(input_list_r, overwrite_target, become_which_target):
    for col_index, col_list in enumerate(input_list_r):
        for row_index, _ in enumerate(col_list):
            if input_list_r[col_index][row_index] == overwrite_target:
                del input_list_r[col_index][row_index]
                input_list_r[col_index].insert(row_index,become_which_target)
    return input_list_r

def slot_overwrite_list_by_target_with_lock_list(input_list_r,lock_list, become_which_target):

    return_update_list_r = []
    return_update_list_r = slot_shallow_copy_to_origin_value_by_list_r(input_list_r)

    for col_index, col_list in enumerate(input_list_r):
        for row_index, _ in enumerate(col_list):
            if lock_list[col_index][row_index] == 1:
                return_update_list_r[col_index][row_index] = become_which_target
    return return_update_list_r

# Par Example: vois la "W", return la positon à "1", else à "0"
def slot_obtenir_lock_list_by_target(input_list_r,check_target):

    # [Attension]: If you use:  lock_list = input_list_r.copy(), when iterating the lock_list, still affect the input_list_r, 
    #############  which i don't know why:

    # Copie la input_list_r's shape use manually code.
    lock_list = []
    for index_one_list in input_list_r:
        tem_index_one_list = []
        for value in index_one_list:
            tem_index_one_list.append(value)
        lock_list.append(tem_index_one_list)
    
    
    #lock_list = input_list_r.copy()
    for col_index, col_list in enumerate(lock_list):
        for row_index, _ in enumerate(col_list):
            if lock_list[col_index][row_index] == check_target:
                get_the_target = 1
                del lock_list[col_index][row_index]
                lock_list[col_index].insert(row_index, get_the_target)
            else:
                didnt_get_the_target = 0
                del lock_list[col_index][row_index]
                lock_list[col_index].insert(row_index, didnt_get_the_target)
   
    return lock_list

def slot_shallow_copy_to_zero_by_list_r(input_list_r):
    return_list = []
    for index_one_list in input_list_r:
        tem_index_one_list = []
        for _ in index_one_list:
            value = 0
            tem_index_one_list.append(value)
        return_list.append(tem_index_one_list)
    return return_list


def slot_shallow_copy_to_origin_value_by_list_r(input_list_r):
    return_list = []
    for index_one_list in input_list_r:
        tem_index_one_list = []
        for value in index_one_list:
            tem_index_one_list.append(value)
        return_list.append(tem_index_one_list)
    return return_list
    

# Used to input, roll_table > output > 3_line, 4_line, 5_line, probability > pre_calculate_rtp.
class slot_line_setting_analysis():
    def __init__(self,input_number_of_cols, input_number_rows_in_each_col_list):
        self.name               = "[ana_slot:slot_line_setting_analysis]: "
        self.number_of_row_list = input_number_rows_in_each_col_list
        self.number_of_cols     = input_number_of_cols
        self.max_len            = 0

    def ajouter_mg_roll_table(self,input_mg_roll_list_list):
        # Copy
        mg_roll_list_list = input_mg_roll_list_list.copy()

        # Save roll_table_final_index_pos [ 25, 19, 22, 26, 29]
        self.roll_table_final_index_pos = [ len(any_list) for any_list in mg_roll_list_list]

        # Obtenir all_equal_list_list 
        all_equal_size_list = []

        # Obtenir max_len
        len_list = [ len(_list) for _list in mg_roll_list_list]
        max_len  = max(len_list)
        self.max_len = max_len  # pour calculate_linable_pro_distribuion()

        # Faire all_equal_list_list
        for any_list in mg_roll_list_list:
            if len(any_list) < max_len:
                any_list.extend(["--"]*(max_len-len(any_list)))
            
            # Append all_equal_list_list
            all_equal_size_list.append(any_list)

        # Data {  R1, R2, ... RN }
        data       =  { "R_%d"%(v+1): any_list for v, any_list in enumerate(mg_roll_list_list)}
        #data       = { "R_%d"%(v+1): any_list for v, any_list in enumerate(all_equal_size_list)}
       
        # Data_Index = [ 1, 2, 3, .......   max_len ]
        data_index = [ v+1 for v in range(max_len)]
        # Save col_index_name: [R_1, R_2, R_3 , ....]
        self.mg_roll_table_col_name_list = ["R_%d"%(v+1) for v , _ in enumerate(mg_roll_list_list)]
        
        # Créer Panda DataFrame avec data_index
        self.mg_roll_table_df = pd.DataFrame(data,index=data_index)

    def les_information(self):
        msg =  self.name + "\n"
        msg += "self.number_of_row_list =         %s\n" % self.number_of_row_list
        msg += "self.number_of_cols     =         %d\n" % self.number_of_cols
        msg += "self.mg_roll_table_df   =        \n\n%s\n" % self.mg_roll_table_df
        return msg
    
    # Setting from Excel > Main() > Cette Agent.
    def calculate_linable_probability_distribution___set_lineable_list(self,input_list):
        self.line_able_list = copy.deepcopy(input_list)
    
    def calculate_linable_probability_distribution(self):
        msg = self.name + "\n"


        # Import line_able_obj_list
            # - ['G1', 'S1', 'S2', 'C1', 'C2', 'C3', 'I1', 'I2', 'I3', 'I4', 'W', 'SS']
        line_able_list  = copy.deepcopy(self.line_able_list)
        print("可連線物品:\n%s\n"%line_able_list)

        # Créer probability_data_frame =  [ Initila by 0.0]
            #   -  Count_for_R_1  Count_for_R_2  Count_for_R_3  Count_for_R_4  Count_for_R_5
            #   
        data_empty_list = [[0.0 for _ in range(self.number_of_cols)] for _ in range(len(line_able_list))]
        data_col_norm   = ['Count_for_R_%d'%(v+1) for v in range(self.number_of_cols)]
        probability_df  = pd.DataFrame(data_empty_list,columns=data_col_norm,index=line_able_list)
        print(probability_df)

        # Adjouter ID Col:
        __df = self.mg_roll_table_df.copy()
        id_list = [ v+1 for v in range(self.max_len)]
        __df['ID'] = id_list
        print("Base on the datafrmae:\n",__df)

        # Obtenir Symbol Cnts tout le Col. R_1, R_2, .....
        col_start = 1
        col_end   = self.number_of_cols + 1
        

        print("Check Max_Index In Each Roll ")
        print(self.roll_table_final_index_pos)

       
        for any_index_of_col in range(col_start,col_end):
            col_norm   = "R_%d"%any_index_of_col
            count_norm = "Count_for_R_%d"%any_index_of_col 
            tem_df = __df.groupby(col_norm)['ID'].nunique()
            
            tem_df = tem_df.div(self.roll_table_final_index_pos[any_index_of_col-1])
            

            for each_symbol in tem_df.index:
                if each_symbol != "--":
                    # [Count_for_R_1][C1]      =  tem_df[C1]
                    probability_df[count_norm][each_symbol] = tem_df[each_symbol]
                elif each_symbol == "--":
                    pass
                else:
                    print("Error: Get the unexpected index %s"%each_symbol)

        
        # Afficher the probability table
        print("各個Symbol出現在各個輪的機率")
        print(probability_df)
        



# New Slot_bet_rate_class for 94_Line_Design_Project.
class slot_bet_rate_class_v1():
    def __init__(self,obj_name):
        self.name        = "[slot_bet_rate_class_v1]: use pandas for kernel code"
        self.bet_rate_df = pd.DataFrame()
    
    def ajouter_obj_par_bet_rate_list(self,obj_symbol,obj_bet_rate_list):
        # for 1, 2, 3, 4, 5 line bet : [0,0,3,4,5]
        df_data_list  = obj_bet_rate_list
        df_index      = obj_symbol                                         # 'SS', 'J', 'W' for example
        columns_list  = ["Bet_%d"%(v+1) for v in range(len(df_data_list))] # [Bet_1, Bet_2 ...  Bet_n]
        _tem_df       = pd.DataFrame([df_data_list],columns=columns_list,index=[df_index])
        self.bet_rate_df = self.bet_rate_df.append(_tem_df)

    def les_information(self):
        msg = "[slot_bet_rate_class_v1]: implement with pandas:\n"
        msg += "\n%s\n"%self.bet_rate_df
        return msg

    def obtenir_bet_rate_par_obj_et_bet_index(self,obj_symbol,obj_bet_rate_index):
        col_name = "Bet_%d"%obj_bet_rate_index # Bet_1 or Bet_2 or Bet_3 , or Bet_6
        value = self.bet_rate_df[col_name][obj_symbol]
        return value

    

# Mon parent: slot_bet_rate_agent()
#             support only 3, 4, 5 lines.
#             it have some issue with the previous game like (Pandas, Way_Transformer: 6_line_able_bet_rate is not exist) 
class slot_bet_rate_class():
    def __init__(self,obj_name):
        self.obj_name            = obj_name
        self.obj_3lines_bet_rate = 0.0
        self.obj_4lines_bet_rate = 0.0
        self.obj_5lines_bet_rate = 0.0

    def set_345lines_bet_rate(self,trois,quatre,cinq):
        self.obj_3lines_bet_rate = trois
        self.obj_4lines_bet_rate = quatre
        self.obj_5lines_bet_rate = cinq
    
    def les_formation(self):
        msg  = "[slot_bet_rate_class]['%s']:\n"%self.obj_name
        msg += "3lines_bet_rate        = %s \n"%self.obj_3lines_bet_rate
        msg += "4lines_bet_rate        = %s \n"%self.obj_4lines_bet_rate
        msg += "5lines_bet_rate        = %s \n"%self.obj_5lines_bet_rate
        return msg

    def obtenir_bet_rate(self,trios_quatre_cinq):
        if trios_quatre_cinq == 3: return self.obj_3lines_bet_rate
        if trios_quatre_cinq == 4: return self.obj_4lines_bet_rate
        if trios_quatre_cinq == 5: return self.obj_5lines_bet_rate

        print("[slot_bet_rate_class]: Error ! , no match lines ")
        return 543

# Mon enfant: slot_bet_rate_class()
class slot_bet_rate_agent():
    def __init__(self):
        self.agent_name = ""
        self.bet_rate_class_number = 0
        self.bet_rate_class_list = []
        self.bet_rate_class_dictionary = {}
        self.bet_rate_class_inverse_dictionary = {}
        
    def initial_by_excel(self,input_excel_name, input_table_name, read_length):

        # Set agent_norm:
        self.agent_name = input_table_name
        # Set numbers:
        self.bet_rate_class_number = read_length
        # Ouverte workbook
        workbook = xlrd.open_workbook(input_excel_name)
        # Ouverte sheet
        sheet = workbook.sheet_by_name(input_table_name)
        # Set bet_rate_class_list:  col_index = 6 
        print("[目前取用連線物品固定11, 後續撥空參考原始滾輪設定改成可彈性自動判斷]: read_length =  %d"%read_length)
        for row in range(1,1+read_length):
            # Créer un nouveau class avec obj_norm
            trois  =  float(sheet.cell_value(row, 9))
            quatre =  float(sheet.cell_value(row,10))
            cinq   =  float(sheet.cell_value(row,11))
            tem_class = slot_bet_rate_class(sheet.cell_value(row,6))
            tem_class.set_345lines_bet_rate(trois,quatre,cinq)
            self.bet_rate_class_list.append(tem_class)
        # Set dictionary: col_index = 6
        self.bet_rate_class_dictionary = {index: sheet.cell_value(index+1,6) for index  in range(read_length) }
        self.bet_rate_class_inverse_dictionary = { v: k for k,v in self.bet_rate_class_inverse_dictionary.items()}
            
    def obtenir_bet_rate(self,obj_name,trois_quatre_cinq):
        for any_class in self.bet_rate_class_list:
            if any_class.obj_name == obj_name:
                bet_rate = any_class.obtenir_bet_rate(trois_quatre_cinq)
                return bet_rate

    def les_formation(self):
        msg = "[slot_bet_rate_agent]: call les_formation...\n"
        for any_class in self.bet_rate_class_list:
            msg += any_class.les_formation()
        return msg


# Generate the each run's env (Afficher toute le run par roll-table ou control-weight-table)
class slot_table_agent():
    # Par Exaple: 5 X 3  (5 cols, each col has 3 rows to put symbol)
    # self.number_of_cols     = 5
    # self.number_of_row_list = [3,3,3,3,3]
    def __init__(self,input_number_of_cols,input_number_rows_in_each_col_list):
        self.number_of_row_list = input_number_rows_in_each_col_list
        self.number_of_cols     = input_number_of_cols

    def ajouter_mg_roll_table(self,mg_roll_list_list):
        __mg_roll_list_list = copy.deepcopy(mg_roll_list_list)
        # Save roll_table_final_index_pos [ 25, 19, 22, 26, 29]
        self.roll_table_final_index_pos = [ len(any_list) for any_list in __mg_roll_list_list]

        # Obtenir all_equal_list_list 
        all_equal_size_list = []

        # Obtenir max_len
        len_list = [ len(_list) for _list in __mg_roll_list_list]
        max_len  = max(len_list)

        # Faire all_equal_list_list
        for any_list in __mg_roll_list_list:
            if len(any_list) < max_len:
                any_list.extend(["--"]*(max_len-len(any_list)))
            
            # Append all_equal_list_list
            all_equal_size_list.append(any_list)

        # Data {  R1, R2, ... RN }
        data       = { "R_%d"%(v+1): any_list for v, any_list in enumerate(all_equal_size_list)}
        # Data_Index = [ 1, 2, 3, .......   max_len ]
        data_index = [ v+1 for v in range(max_len)]
        # Save col_index_name: [R_1, R_2, R_3 , ....]
        self.mg_roll_table_col_name_list = ["R_%d"%(v+1) for v , _ in enumerate(all_equal_size_list)]
        


        # Créer Panda DataFrame avec data_index
        self.mg_roll_table_df = pd.DataFrame(data,index=data_index)

    # [obtenir_list_par_id]: Comment Faire:
        # start_run = 0
        # end_run   = 50
        # run_id    =  0, 1, 2, 3, ..... 47, 48, 49. 
        # return  list_r

    def obtenir_mg_roll_table_par_id(self,run_id):
        # Initial start_id_list: for id = 0   [ 1, 1, 1, 1, 1]
        #                        for id = 1   [ 4, 4, 4, 4, 4] if roll_list = [3, 3,3,3,3]
        start_id_list = [  1 + (run_id * self.number_of_row_list[index]) for  index in range(len(self.number_of_row_list))]
        return_list_r = []
        # Loop
        for index, any_row_length in enumerate(self.number_of_row_list): 
            tem_list = []
            for incre_value in range(any_row_length):
                # Obtenir each tem_id
                tem_id = start_id_list[index] + incre_value

                # Calculate the value:
                tem_value = (tem_id % self.roll_table_final_index_pos[index])
                if tem_value == 0:
                    final_id = self.roll_table_final_index_pos[index]
                elif tem_value < self.roll_table_final_index_pos[index]:
                        final_id = tem_value
                else:
                    print("[Error]: Unexpected tem_value with self.roll_table_final_index_pos[index]= (%d, %d)"%(tem_value,self.roll_table_final_index_pos[index]))

                tem_symbol = self.mg_roll_table_df[self.mg_roll_table_col_name_list[index]][final_id]
                tem_list.append(tem_symbol)
            
            # Append
            return_list_r.append(tem_list)
        
        return return_list_r

    ## [Jean]:  2020-04-08 Implement pour obtenir random
        # Afficher: 
            # self.number_of_row_list           =  [3, 3, 3, 3, 3]
            # self.roll_table_final_index_pos   =  [131, 129, 149, 139, 137]
        # Random Range:
            # Initial start_id_list: for id = 0   [ 1, 1, 1, 1, 1]
            #                        for id = 1   [ 4, 4, 4, 4, 4] if roll_list = [3, 3,3,3,3]
        # for 131 , the id range =   (1 , 131) ,  random.randint(1,131)
        # for 129 , the id range =   (1 , 129) ,  random.randint(1,129)

    def obtenir_mg_roll_table_par_natural_random(self,run_id):
        return_list_r = []
        start_id_list = []
        for any_col in range(len(self.number_of_row_list)):
            ##### random_pick_id = random.randint(1,self.roll_table_final_index_pos[any_col]) 
            random_pick_id = jason_random_generator_v1(1,self.roll_table_final_index_pos[any_col])
            start_id_list.append(random_pick_id)
        
        #print("start_id_list =    ",start_id_list)

        # Loop
        for index, any_row_length in enumerate(self.number_of_row_list): 
            tem_list = []
            for incre_value in range(any_row_length):
                # Obtenir each tem_id
                tem_id = start_id_list[index] + incre_value

                # Calculate the value:
                tem_value = (tem_id % self.roll_table_final_index_pos[index])
                if tem_value == 0:
                    final_id = self.roll_table_final_index_pos[index]
                elif tem_value < self.roll_table_final_index_pos[index]:
                        final_id = tem_value
                else:
                    print("[Error]: Unexpected tem_value with self.roll_table_final_index_pos[index]= (%d, %d)"%(tem_value,self.roll_table_final_index_pos[index]))

                tem_symbol = self.mg_roll_table_df[self.mg_roll_table_col_name_list[index]][final_id]
                tem_list.append(tem_symbol)

            # Append
            return_list_r.append(tem_list)
 
        return return_list_r

    
    # Use https://github.com/wolfmib/ja_random_generator_services_via_api_golang
        # Run main.go
        # Referenced ja_python_test_api.py
    def obtenir_mg_roll_table_par_natural_random_via_golang_services(self,run_id):
        return_list_r = []
        start_id_list = []
        for any_col in range(len(self.number_of_row_list)):
            ##### random_pick_id = random.randint(1,self.roll_table_final_index_pos[any_col]) 
            ##### random_pick_id = jason_random_generator_v1(1,self.roll_table_final_index_pos[any_col])
            my_url   = "http://localhost:12345/get_random/"
            low      = "1"
            high     = str(self.roll_table_final_index_pos[any_col]) 
            my_url   = my_url + low + "/" + high
            response = requests.get(my_url)
            random_pick_id = response.json()["value"] 

            #############################

            start_id_list.append(random_pick_id)
        
        #print("start_id_list =    ",start_id_list)

        # Loop
        for index, any_row_length in enumerate(self.number_of_row_list): 
            tem_list = []
            for incre_value in range(any_row_length):
                # Obtenir each tem_id
                tem_id = start_id_list[index] + incre_value

                # Calculate the value:
                tem_value = (tem_id % self.roll_table_final_index_pos[index])
                if tem_value == 0:
                    final_id = self.roll_table_final_index_pos[index]
                elif tem_value < self.roll_table_final_index_pos[index]:
                        final_id = tem_value
                else:
                    print("[Error]: Unexpected tem_value with self.roll_table_final_index_pos[index]= (%d, %d)"%(tem_value,self.roll_table_final_index_pos[index]))

                tem_symbol = self.mg_roll_table_df[self.mg_roll_table_col_name_list[index]][final_id]
                tem_list.append(tem_symbol)

            # Append
            return_list_r.append(tem_list)
 
        return return_list_r


    # Run first 10 runs: return msg 
        # Use self.mg_roll_table_df
        # R_1:  1: G1,  2:I2,  3:I2,  ........   22:C2, 23:C3,  24:I1, 25:C1
        # ----------------------------------------------------------------
        #       for id_run = 0 with roll_len  = 3
        #       pick:  1 + 0*3 =  1     pick_list =  [1,  2,   3]   = [G1, I2, I2]       
        #
        #       for id_run = 7  with roll_len = 3
        #       pick:  1 + 7*3 = 22,   pick_list = [ 22, 23, 24 ]  = [C2, C3, I1]
        #       
        #       for id_run = 8  with roll_len = 3
        #       pick:  1 + 8*3 = 25,   pick_list = [ 25,  1 ,  2 ]  = [C1, G1, I2]
        # -----------------------------------------------------------------
        #      for case 3:  (25, 26, 27)  convert to (25, 1, 2)
        #      How ?  only if the number > 24
        #      --------
        #      25 % 25 =  0   ->  25
        #      26 % 25 =  1  
        #      26 % 25 =  2   
        #      -------------------------
        #      
        # ----------------------------------------------------------------
        #      for id_run = 16 with roll_len = 3
        #       pick:  1 + 16* 3 = 49   pick_list = [49, 50, 51] -> [ 24 ,25, 1]

    def show_mg_roll_table_head(self):
        
        # [Jason]: start_id = [1,1,1,1,1] depend on the row_list [3,3,3,3,3]
        start_id_list = [ 1 for _ in range(len(self.number_of_row_list))]

        # Implement ici apres
        # print("[Debug, 25, 19, 22, 26, 29] =  %s"%self.roll_table_final_index_pos)
        # self.roll_table_final_index_pos = [25, 19, 22 , 26, 29]

        # make first_10_list_r_list
        first_10_list_r_list = []

        msg = ""
        for any_pd_index in range(10):
            print(start_id_list)
            
            # Loop each roll 
            tem_list_r = []
            for index, any_row in enumerate(self.number_of_row_list):
                tem_msg = "For R_%d's roll with run_id = [%d]:\n"%((index+1),any_pd_index)
                # Initial tem_list_r
                tem_list = []

                # Loop each symbol in each roll
                for incre_value in range(any_row):

                    # Obtenir each tem_id
                    tem_id = start_id_list[index] + incre_value

                    # Calculate the value ,   tem_id % the roll_length
                    tem_value = (tem_id  % self.roll_table_final_index_pos[index] )
                    if tem_value == 0:
                        final_id = self.roll_table_final_index_pos[index]
                    elif tem_value < self.roll_table_final_index_pos[index]:
                        final_id = tem_value
                    else:
                        print("[Error]: Unexpected tem_value with self.roll_table_final_index_pos[index]= (%d, %d)"%(tem_value,self.roll_table_final_index_pos[index]))

                    
                    tem_msg += "%d , "%final_id
                    # Append each symbol by final_id
                    tem_symbol        = self.mg_roll_table_df[self.mg_roll_table_col_name_list[index]][final_id]
                    #print(tem_symbol)
                    tem_list.append(tem_symbol)

                msg += tem_msg + "\n"
                tem_list_r.append(tem_list)
            
            # Append each tem_list_r run by run
            first_10_list_r_list.append(tem_list_r)

            # Go to next run_id    
            start_id_list = [start_id_list[i] + self.number_of_row_list[i] for i in range(len(start_id_list))]

        #print(first_10_list_r_list)
        #Afficher 
        afficher_msg = ""
        for any_list_r in first_10_list_r_list:
            afficher_msg += self.afficher_table_par_list_r(any_list_r)
            afficher_msg += "\n"
        print(afficher_msg)

        #print(msg)

    def les_information(self):
        msg  = "slot_table_agent avec pandas:\n"
        msg += "self.number_of_row_list =         %s\n"%self.number_of_row_list
        msg += "self.number_of_cols     =         %d\n"%self.number_of_cols
        msg += "self.mg_roll_table_df   =        \n\n%s\n"%self.mg_roll_table_df
        return msg
        
    def afficher_table_par_list_r(self,list_r):

        # Obtenir all_equal_size:
        all_equal_size_list_r = []
        max_len         = max(self.number_of_row_list)

        for any_list in list_r:
            if len(any_list) < max_len:
                any_list.extend(["--"]*(max_len-len(any_list)))
            
            # Append all_equal_size_list
            all_equal_size_list_r.append(any_list)

        msg  ="[slot_table_agent]: 盤面表現\n"
        data = { "R_%d"%(v+1): any_list for v, any_list in enumerate(all_equal_size_list_r)}

        # Créer Panda Dataframe
        df = pd.DataFrame(data)

        # Afficher Panda Data
        msg += "%s\n"%df

        return msg

    # Previous Code , implement par pandas format to get good display:
        #def afficher_table_par_list_r(self, list_r):
        #    tmp = []
        #    msg  = ""
        #    msg +="[slot_table_agent]: 盤面表現\n"
        #    n = max(self.number_of_row_list)
        #    for _list in list_r:
        #    	m = len(_list)
        #    	tmp.extend(_list)
        #    	if m != n:
        #    		tmp.extend([""]*(n-m))
        #    for i in range(n):
        #    	tem_str = json.dumps(tmp[i::n])
        #    	msg    += tem_str
        #    	msg    += "\n"
        #    return msg

# Calculer RTP (input list_r et faire the rtp calculation)
class slot_calculer_rtp_agent():
    def __init__(self,input_obj_name):
        self.norm                             = input_obj_name
        self.wild_list                        = []
        self.linable_list                     = []
        self.line_setting_list                = [] # For line only
        self.col_lens_by_line_setting_list    = 0  # Obtenir after calling set_line_setting_list() 
        self.apply_type                       = ""
        self.apply_version                    = ""
        self.partner_agent_index              = 0
        self.partner_agent_list               = []
        self.partner_agent_dictionary         ={}
        self.partner_agent_inverse_dictionary = []

        # [Jean]: aller aller, 2, 3, 4, 5  rtp check
        self.actuary_h1_gain_win_line_2  = 0.0
        self.actuary_h1_cht_win_line_2 = 0.000000000000000000001
        self.actuary_h2_gain_win_line_2  = 0.0
        self.actuary_h2_cht_win_line_2 = 0.000000000000000000001
        self.actuary_l6_gain_win_line_2  = 0.0
        self.actuary_l6_cht_win_line_2 = 0.000000000000000000001\


        self.actuary_h1_gain_win_line_3  = 0.0
        self.actuary_h1_cht_win_line_3 = 0.000000000000000000001
        self.actuary_h2_gain_win_line_3  = 0.0
        self.actuary_h2_cht_win_line_3 = 0.000000000000000000001
        self.actuary_h3_gain_win_line_3  = 0.0
        self.actuary_h3_cht_win_line_3 = 0.000000000000000000001
        self.actuary_h4_gain_win_line_3  = 0.0
        self.actuary_h4_cht_win_line_3 = 0.000000000000000000001
        self.actuary_h5_gain_win_line_3  = 0.0
        self.actuary_h5_cht_win_line_3 = 0.000000000000000000001
        self.actuary_l1_gain_win_line_3  = 0.0
        self.actuary_l1_cht_win_line_3 = 0.000000000000000000001
        self.actuary_l2_gain_win_line_3  = 0.0
        self.actuary_l2_cht_win_line_3 = 0.000000000000000000001
        self.actuary_l3_gain_win_line_3  = 0.0
        self.actuary_l3_cht_win_line_3 = 0.000000000000000000001
        self.actuary_l4_gain_win_line_3  = 0.0
        self.actuary_l4_cht_win_line_3 = 0.000000000000000000001
        self.actuary_l5_gain_win_line_3  = 0.0
        self.actuary_l5_cht_win_line_3 = 0.000000000000000000001
        self.actuary_l6_gain_win_line_3  = 0.0
        self.actuary_l6_cht_win_line_3 = 0.000000000000000000001

        
   

    
    #  set_type    =  'line' or 'way'
    def set_type(self,input_type):
        self.apply_type    = input_type
    #  set_version =  'v1' or 'v2' or 'name' 
    def set_version(self,input_version):
        self.apply_version = input_version
    def set_wild_list(self,input_wild_list):
        self.wild_list     = input_wild_list
    def set_linable_list(self,input_lineable_list):
        self.linable_list  = input_lineable_list
    def set_line_setting_list(self,input_line_setting_list):
        self.line_setting_list              = input_line_setting_list
        if self.line_setting_list:
            self.col_lens_by_line_setting_list = len(self.line_setting_list[0])
        else:
            print("[Error]: input_empty input_line_setting_list = %s"%input_line_setting_list)
    def les_information(self):
        msg  ="[%s]\n"%self.norm
        msg +="self.wild_list                     = %s \n"%self.wild_list     
        msg +="self.linable_list                  = %s \n"%self.linable_list   
        msg +="self.apply_type                    = %s \n"%self.apply_type     
        msg +="self.apply_version                 = %s \n"%self.apply_version  
        msg +="self.partner_agent_dictionary      = %s \n"%self.partner_agent_dictionary
        msg +="self.partner_agent_inverse_dict    = %s \n"%self.partner_agent_inverse_dictionary
        msg +="self.partner_agent_list            = %s \n"%self.partner_agent_list
        msg +="self.col_lens_by_line_setting_list = %d \n"%self.col_lens_by_line_setting_list

        # Afficher 25 line settings if set:
        msg +="Self.line_setting_list: 0=row_0,  1=row_1, etc..           \n"
        for any_list in self.line_setting_list:
            msg += "\t\t\t\t       %s\n"%any_list
        return msg
    
    
    # ###############       Line Function List #######################################
        # - add_partner 
        # - call_partner_by_name
        # - calculer_rtp_by_line_setting_v1

    def add_partner(self,input_name,input_class):
       temp_class = input_class
       self.partner_agent_list.append(temp_class)
       self.partner_agent_dictionary.update({self.partner_agent_index: input_name })
       self.partner_agent_inverse_dictionary = { v: k for k, v in self.partner_agent_dictionary.items()}
       self.partner_agent_index +=1

    def call_partner_by_name(self,input_name, input_attr_name, option_input_list=False):
        # Example:    get_msg = bet_rate_agent.les_information()
            # input_name      = 'bet_rate_agent'
            # input_attr_name = 'les_information' 
            #  tem_attr       = getattr(input_name,input_attr_name)
            #  get_msg        = tem_attr()
        if input_name in self.partner_agent_inverse_dictionary:
            tem_attr = getattr(self.partner_agent_list[self.partner_agent_inverse_dictionary[input_name]],input_attr_name)
        else:
            print("[Error]: Didn't add this partner class :  %s  in current parther list = %s"%(input_name,self.partner_agent_inverse_dictionary))
        
        if option_input_list:
            pass # implement the input list later
        else:
            return tem_attr()
    
    def calculer_rtp_by_line_setting_v1(self,run_id,list_r,bet_rate_agent,optional_static_agent=False,optional_pd=None):



        
        debug_msg  = "[calculer_rtp_by_line_setting_v1]:\n"
        system_msg = ""
        gain       = 0
        

        # Loop Each Line: line_index from 0 - 24,  in excel format is 1-25
        # Test
        test_return_g1_cnt = 0

        # Loop Each Obj
        for obj in self.linable_list:     
            for line_index , each_line_list in enumerate(self.line_setting_list):
                # Initial set function
                check_obj    = 0 
                count        = 0 
                current_line = 0

                # Loop Each col_index
                for col_index in range(self.col_lens_by_line_setting_list):
                    # count > line_cnts
                    count += 1

                    current_symbol = list_r[col_index][each_line_list[col_index]]
                    # current_symbol != target_obj, break! and not in wild_list
                    if current_symbol != obj and current_symbol not in self.wild_list:
                        break
                    elif current_symbol in self.wild_list:
                        if obj not in self.wild_list:
                            current_line = count
                        else:  # if the target_obj is 'W' itself...faire other way
                            check_obj    = obj
                            current_line = count

                    elif current_symbol == obj:
                        check_obj    = obj
                        current_line = count

                
                if current_line >=3 and check_obj !=0:

                    # Obtenir gain: bet_amount= 1/ how_manh_lines
                    bet_amount = 1 / len(self.line_setting_list)
                    bet_rate   = bet_rate_agent.obtenir_bet_rate_par_obj_et_bet_index(check_obj,current_line)

                    # Obtenir_bet_rate_par_obj_et_bet_index('G1',3) means:  bet rate with G1_3_lines
                    current_gain = bet_amount * bet_rate
                    gain        += current_gain

                    # Obtenir the win_line: 1~25  ,  since line_index is 0~24
                    win_line_index          = line_index + 1
                    
                    # Enregistrer des données a Pandas
                    # Target: {'Run_ID': int(0),'Win_Obj':'S1',"Bet_Rate_3": 5,"Win_Line":3}
                    if optional_pd is not None:
                        run_id_col           = "Run_ID"
                        run_id_value         = int(run_id)
                        win_obj_col          = "Win_Obj"
                        win_obj_value        = check_obj 
                        bet_rate_index_col   = "Bet_Rate_%d"%current_line
                        bet_rate_index_value = bet_rate
                        win_line_col         = "Win_Line"
                        win_line_value       = int(win_line_index)
                        gain_col             = "Gain"
                        gain_value           = current_gain 
                        list_r_col           = "List_R"
                        list_r_value         = copy.deepcopy(list_r)
                        group_line_col       ="Group_Win_Line"
                        group_line_value     = int(current_line)

                        input_dict           = {group_line_col:group_line_value,run_id_col:run_id_value,win_obj_col:win_obj_value,bet_rate_index_col:bet_rate_index_value,win_line_col:win_line_value,gain_col:gain_value,list_r_col:list_r_value}
                        optional_pd = optional_pd.append(input_dict,ignore_index=True)

                        # Change to int
                        my_int_col_list = [run_id_col,win_line_col,group_line_col]
                        optional_pd[ my_int_col_list] = optional_pd[my_int_col_list].astype(int)

                        # Set the list_r column in the last column
                        front_or_end_list = [group_line_col,run_id_col, win_obj_col,win_line_col,gain_col,list_r_col]
                        optional_pd = optional_pd[[run_id_col,group_line_col, win_obj_col, win_line_col, gain_col] +[c for c in optional_pd if c not in front_or_end_list] + [list_r_col]]

                    else:
                        pass

                    # Afficher les information
                    system_msg += "第%3d條線, Symbol: %3s,  %3d連線,  \n"%(win_line_index,check_obj,current_line)
                    
                    
                    # Créer les information pour Obj_Win_3
                    if current_line == 3:
                        if optional_static_agent:
                            # Hard Code here. the format
                                # obj_3, obj_4, obj_5 etc..
                                # G1_3,  S1_3, W_4, SS_3
                            key_code = "%s_%d" % (check_obj, current_line)
                            optional_static_agent.increase_cnts(key_code)
                        else:
                            pass
                        
        #return 0, system_msg, debug_msg
        if optional_pd is not None:
            return gain, system_msg, debug_msg, optional_pd
        else:
            return gain, system_msg, debug_msg

    # 🐳 🎁 the line calculer support obj >= 2,  in game_806_progressive_jackpot
    # 🎹: implement the version 2: with W1, W2 etc..
    # 🦌: fix the bug for case 
        #  0  L3  L4  L5  H5  H2
        #  1  L2  H3  L2  L5  L2
        #  2  W1  L2  H5  L2  L5
        #  
        #  第 15條線, Symbol:  L2,    5連線,  
        #  din't print  (2,2,1,2) (W1-L2-L2-L2), line-7, 4symbols
        #  need to add specific calculate the wild logic
    # 🎹, 🧪:  implement the version 2:  add pytest_data for checking the testing data coverage

    # 🌟:  #  🌟🌟   load v2.1 version:  
    #                           1. support prevent checking S1 inside the rtp_agent.run() . 
    #                           2. S1 count logic is being iplement outside the libs.
    def calculer_rtp_by_line_setting_v2_for_slot_3(self,run_id,list_r,bet_rate_agent,optional_static_agent=False,optional_pd=None):
        

        ## Here Jean dododo
        wrong_gain = 0

        debug_msg  = "[calculer_rtp_by_line_setting_v1]:\n"
        system_msg = ""
        gain       = 0

        # 🎹,🧪  :  Initial winning_data_list
        pytest_data_list = []

        # 🦉     :  先算線: 因為要比較這個線 有沒有出現 wild-2 or A-3 case
        # 🎹     :  remove wild group: W1, W2 etc..
        def __remove_wild_group(input_list):
            return_list = []
            for any_obj in input_list:
                if any_obj[0] not in ["W"]:
                    return_list.append(any_obj)

            return return_list


        """
        print("[jackpot_anlyzer_slot_v2]: manualy input the list_r ")
        print("[[W1,H1,H2],[W1,H1,H2],[W1,H1,H2],[W1,H1,H2],[W1,H1,H2]]")
        input()
        list_r = [["W1","H1","H2"],["W1","H1","H2"],["W1","H1","H2"],["W1","H1","H2"],["W1","H1","H2"]]
        """
    
        # 🦉: let's loop non_wild_list first.
        non_wild_list = __remove_wild_group(self.linable_list)

        # Loop Each Obj with non-wild list.
        current_gain = 0.0
        return_2_gain = 0.0
        return_3_gain = 0.0
        return_4_gain = 0.0
        return_5_gain = 0.0


        for obj in non_wild_list:     
            if obj == "S1":
                pass
            else:
                for line_index , each_line_list in enumerate(self.line_setting_list):
                    # Initial set function
                    check_obj    = 0 
                    count        = 0 
                    current_line = 0

                    # 🦉: Reset the gain after compare
                    current_obj_gain = 0.0
                    current_wild_gain = 0.0
    
                    # Loop Each col_index
                    for col_index in range(self.col_lens_by_line_setting_list):
                        # count > line_cnts
                        count += 1
    
                        current_symbol = list_r[col_index][each_line_list[col_index]]
                        # current_symbol != target_obj, break! and not in wild_list
                        if current_symbol != obj and current_symbol not in self.wild_list:
                            #system_msg += "[Debug_01]: line_index:  %d ,  col_index:  %d ,  current_symbol:  %s , self.wild_list =  %s\n"%(line_index,col_index,current_symbol,self.wild_list)
                            break
                        elif current_symbol in self.wild_list:
                            if obj not in self.wild_list:
                                current_line = count
                            else:  # if the target_obj is 'W' itself...faire other way
                                check_obj    = obj
                                current_line = count
                        elif current_symbol == obj:
                            check_obj    = obj
                            current_line = count
           
                    # 🐳 🎁 :        v0:  count the obj (except wild), the bet_win_line is >=3
                            #        v1:  implement code to support >=2, made by douge. 
                    # 洗患你 那那那🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳print("[Debug][01]: check_obj:    %s,     current_lins:  %d,     current_wild_gain:   %.4f     current_obj_gain:  %.4f   "%(check_obj,current_line,current_wild_gain,current_obj_gain))
                    if current_line >=2 and check_obj !=0:
                        # Obtenir gain: bet_amount= 1/ how_manh_lines
                        bet_amount = 1 / len(self.line_setting_list)
                        bet_rate   = bet_rate_agent.obtenir_bet_rate_par_obj_et_bet_index(check_obj,current_line)
                        # Obtenir_bet_rate_par_obj_et_bet_index('G1',3) means:  bet rate with G1_3_lines
                        current_obj_gain = bet_amount * bet_rate

                        # 洗患你 那那那🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳print("[Debug][01-enter-obj]: check_obj:    %s,     current_lins:  %d,     current_wild_gain:   %.4f     current_obj_gain:  %.4f   "%(check_obj,current_line,current_wild_gain,current_obj_gain))
                    
                       
                        #  🦉: Stop here! let's compare the wining_obj's gain is greater the wild_obj in this line or not
                        #  🎹: v2 version, compare if the symbol is W1 or W2 by checking [0]  
                        wild_count = 0
                        wild_current_line = 0
                        for __col_index in range(self.col_lens_by_line_setting_list):
                            wild_count += 1
                            current_symbol = list_r[__col_index][each_line_list[__col_index]]
                            #  🎹:
                            if current_symbol[0] != "W":
                                break
                            #  🎹: 
                            elif current_symbol[0] in ["W"]:
                                wild_current_line = wild_count
                        

                        if wild_current_line >=2:
                            # 洗患你 那那那🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳print("[Debug][02-wild]: check_obj:    %s,     current_lins:  %d,     current_wild_gain:   %.4f     current_obj_gain:  %.4f   "%(check_obj,current_line,current_wild_gain,current_obj_gain))
                            #  🎹: v2 version.  "W" changed to "W1" to present the wild scores
                            wild_bet_rate = bet_rate_agent.obtenir_bet_rate_par_obj_et_bet_index("W1",wild_current_line)
                            current_wild_gain = bet_amount * wild_bet_rate
                        else:
                            # 洗患你 那那那🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳print("[Debug][02-else]: check_obj:    %s,     current_lins:  %d,     current_wild_gain:   %.4f     current_obj_gain:  %.4f   "%(check_obj,current_line,current_wild_gain,current_obj_gain))
                            # 反之 我們就設定 gain = 0
                            current_wild_gain = 0.0
    




                        # Compare  with wild vs obj gain !
                        if current_obj_gain > current_wild_gain:
                            current_gain = current_obj_gain
                            # 洗患你 那那那🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳print("[Debug][03-obj>wild]: check_obj:    %s,     current_lins:  %d,     current_wild_gain:   %.4f     current_obj_gain:  %.4f   "%(check_obj,current_line,current_wild_gain,current_obj_gain))
                    
                            ##########################  fuck ..................########
                            # 🧮 make the 2, 3, 4, 5 total_rtp 
                            # 將Break-down 放在此邏輯if, if-else, if-else,  是避免後面邏輯有將current_gain over_lap的情況 .
                            if current_line == 2:

                                # Actuary: Check the group (win_line 2)
                                return_2_gain += current_gain

                                # Actuary: Check the group (win_line 2  with symbol 'H1' )
                                if obj == "H1":
                                    self.actuary_h1_gain_win_line_2 += current_gain
                                    self.actuary_h1_cht_win_line_2 += 1 
                                    print("[Jean]: [%4d]:  H1 Win Line 2:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_h1_gain_win_line_2/run_id),float(self.actuary_h1_cht_win_line_2/run_id/25)))

                                elif obj == "H2":
                                    self.actuary_h2_gain_win_line_2 += current_gain
                                    self.actuary_h2_cht_win_line_2 += 1 
                                    print("[Jean]: [%4d]:  h2 Win Line 2:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_h2_gain_win_line_2/run_id),float(self.actuary_h2_cht_win_line_2/run_id/25)))

                                elif obj == "L6":
                                    self.actuary_l6_gain_win_line_2 += current_gain
                                    self.actuary_l6_cht_win_line_2 += 1 
                                    print("[Jean]: [%4d]:  l6 Win Line 2:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_l6_gain_win_line_2/run_id),float(self.actuary_l6_cht_win_line_2/run_id/25)))


                            elif current_line == 3:
                                return_3_gain += current_gain

                                # Actuary: Check the group (win_line 2  with symbol 'H1' )
                                if obj == "H1":
                                    self.actuary_h1_gain_win_line_3 += current_gain
                                    self.actuary_h1_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  H1 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_h1_gain_win_line_3/run_id),float(self.actuary_h1_cht_win_line_3/run_id/25)))

                                elif obj == "H2":
                                    self.actuary_h2_gain_win_line_3 += current_gain
                                    self.actuary_h2_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  H2 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_h2_gain_win_line_3/run_id),float(self.actuary_h2_cht_win_line_3/run_id/25)))
                                elif obj == "H3":
                                    self.actuary_h3_gain_win_line_3 += current_gain
                                    self.actuary_h3_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  H3 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_h3_gain_win_line_3/run_id),float(self.actuary_h3_cht_win_line_3/run_id/25)))

                                elif obj == "H4":
                                    self.actuary_h4_gain_win_line_3 += current_gain
                                    self.actuary_h4_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  H4 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_h4_gain_win_line_3/run_id),float(self.actuary_h4_cht_win_line_3/run_id/25)))

                                elif obj == "H5":
                                    self.actuary_h5_gain_win_line_3 += current_gain
                                    self.actuary_h5_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  H5 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_h5_gain_win_line_3/run_id),float(self.actuary_h5_cht_win_line_3/run_id/25)))

                                elif obj == "L1":
                                    self.actuary_l1_gain_win_line_3 += current_gain
                                    self.actuary_l1_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  l1 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_l1_gain_win_line_3/run_id),float(self.actuary_l1_cht_win_line_3/run_id/25)))

                                elif obj == "L2":
                                    self.actuary_l2_gain_win_line_3 += current_gain
                                    self.actuary_l2_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  l2 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_l2_gain_win_line_3/run_id),float(self.actuary_l2_cht_win_line_3/run_id/25)))

                                elif obj == "L3":
                                    self.actuary_l3_gain_win_line_3 += current_gain
                                    self.actuary_l3_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  l3 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_l3_gain_win_line_3/run_id),float(self.actuary_l3_cht_win_line_3/run_id/25)))

                                elif obj == "L4":
                                    self.actuary_l4_gain_win_line_3 += current_gain
                                    self.actuary_l4_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  l4 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_l4_gain_win_line_3/run_id),float(self.actuary_l4_cht_win_line_3/run_id/25)))

                                elif obj == "L5":
                                    self.actuary_l5_gain_win_line_3 += current_gain
                                    self.actuary_l5_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  l5 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_l5_gain_win_line_3/run_id),float(self.actuary_l5_cht_win_line_3/run_id/25)))

                                elif obj == "L6":
                                    self.actuary_l6_gain_win_line_3 += current_gain
                                    self.actuary_l6_cht_win_line_3 += 1 
                                    print("[Jean]: [%4d]:  l6 Win Line 3:    %.5f  prob:   %.9f  "%(run_id,float(self.actuary_l6_gain_win_line_3/run_id),float(self.actuary_l6_cht_win_line_3/run_id/25)))






                                
                            elif current_line == 4:
                                return_4_gain += current_gain
                            elif current_line == 5:
                                return_5_gain += current_gain
                            else:
                                input("Error.... ")


      
    
                        elif current_obj_gain < current_wild_gain:
                            # 🦉: Changed the saving information to wild, cause wild_gain is Bigger , you mother fucker !! 
                            current_gain = current_wild_gain
                            #  🎹: v2 version.  "W" changed to "W1" to present the wild winning counts
                            check_obj    = "W1"
                            current_line = wild_current_line
                            bet_rate     = wild_bet_rate
                            # 洗患你 那那那🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳print("[Debug][03-obj<wild]: check_obj:    %s,     current_lins:  %d,     current_wild_gain:   %.4f     current_obj_gain:  %.4f   "%(check_obj,current_line,current_wild_gain,current_obj_gain))


                            # 我想我找到Bug了, 當wild-gain > obj_gain, 我們需要將current_line checking switch for wild_current_line !!!

                            ##########################  fuck ..................########
                            # 🧮 make the 2, 3, 4, 5 total_rtp 
                            # 將Break-down 放在此邏輯if, if-else, if-else,  是避免後面邏輯有將current_gain over_lap的情況 .
                            if wild_current_line == 2:
                                return_2_gain += current_gain
                            elif wild_current_line == 3:
                                return_3_gain += current_gain
                            elif wild_current_line == 4:
                                return_4_gain += current_gain
                            elif wild_current_line == 5:
                                return_5_gain += current_gain
                            else:
                                input("Error.... ")


    
                        elif current_obj_gain == current_wild_gain and current_obj_gain == 0.0:
                            current_gain = 0.0  # both obj_gain=0.0 and wild_gain=0.0 is common....

                        elif current_obj_gain == current_wild_gain:
                            print("[Error]: obj_gain ~ wild_gain")
                            assert current_obj_gain == current_wild_gain
    
                            
                        # 洗患你 那那那🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳print("[Debug][01]: check_obj:    %s,     current_lins:  %d,     current_wild_gain:   %.4f     current_obj_gain:  %.4f   "%(check_obj,current_line,current_wild_gain,current_obj_gain))
                    
    
                        gain        += current_gain
    
    
                        ############################       print("\n\n[slotv2_1.py]L line 986:")
                        ############################       print("check_obj                     ",check_obj)
                        ############################       print("current_line                  ",current_line) 
                        ############################       print("current_gain                  ",current_gain) 
                        ############################       print("bet_rate                      ",bet_rate) 
                        ############################       input("Press Enter \n")


                        # 🎹,🧪  :  save current data_list
                        tem_winning_data_dict = {}
                        tem_winning_data_dict["win_obj"]        =   check_obj
                        tem_winning_data_dict["win_line"]       =   current_line  # win_3, win_4, win_5 etc..
                        tem_winning_data_dict["win_list_r"]     =   list_r
                        tem_winning_data_dict["win_gain" ]      =   round(current_gain,10)
                        tem_winning_data_dict["win_line_index"] =   line_index           # 0,1,2,3,4,5 .... 19 , 20 lines for example.
                        tem_winning_data_dict["win_bet_rate"]   =   round(bet_rate,10)
                        pytest_data_list.append(tem_winning_data_dict)
    
    
                        # Obtenir the win_line: 1~25  ,  since line_index is 0~24
                        win_line_index          = line_index + 1
                        # Enregistrer des données a Pandas
                        # Target: {'Run_ID': int(0),'Win_Obj':'S1',"Bet_Rate_3": 5,"Win_Line":3}
                        #🙃🙃🙃🙃    print("😅: curr gain = ", current_gain)
                        #🙃🙃🙃🙃    input()
                        if optional_pd is not None:
                            #🙃🙃🙃🙃    print("😅: enter optional pd")
                            #🙃🙃🙃🙃    input()



                            run_id_col           = "Run_ID"
                            run_id_value         = int(run_id)
                            win_obj_col          = "Win_Obj"
                            win_obj_value        = check_obj 
                            bet_rate_index_col   = "Bet_Rate_%d"%current_line
                            bet_rate_index_value = bet_rate
                            win_line_col         = "Win_Line"
                            win_line_value       = int(win_line_index)
                            gain_col             = "Gain"
                            gain_value           = current_gain 
                            list_r_col           = "List_R"
                            list_r_value         = copy.deepcopy(list_r)
                            group_line_col       ="Group_Win_Line"
                            group_line_value     = int(current_line)
                            input_dict           = {group_line_col:group_line_value,run_id_col:run_id_value,win_obj_col:win_obj_value,bet_rate_index_col:bet_rate_index_value,win_line_col:win_line_value,gain_col:gain_value,list_r_col:list_r_value}
                            optional_pd = optional_pd.append(input_dict,ignore_index=True)
                            # Change to int
                            my_int_col_list = [run_id_col,win_line_col,group_line_col]
                            optional_pd[ my_int_col_list] = optional_pd[my_int_col_list].astype(int)
                            # Set the list_r column in the last column
                            front_or_end_list = [group_line_col,run_id_col, win_obj_col,win_line_col,gain_col,list_r_col]
                            optional_pd = optional_pd[[run_id_col,group_line_col, win_obj_col, win_line_col, gain_col] +[c for c in optional_pd if c not in front_or_end_list] + [list_r_col]]
                        
                        
                            # 🙃🙃🙃🙃🙃🙃🙃    print("Run is =  %d Current optional_pd:       "%run_id)
                            # 🙃🙃🙃🙃🙃🙃🙃    print(optional_pd)
                            # 🙃🙃🙃🙃🙃🙃🙃    input("Press Enter :\n")

                        
                        else:
                            pass
                        # Afficher les information
                        #system_msg += "[%s]: 五連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_cinq,self.partner_agent_list[0].obtenir_bet_rate(obj, 5))
                        system_msg += "[%4d]: 第%3d條線, Symbol: %3s,  %3d連線,  bet_rate =  %d , gain = %.4f\n"%(run_id,win_line_index,check_obj,current_line, bet_rate,current_gain)
                        system_msg += "     : list_r\n%s\n-----------\n\n"%list_r
                        # Créer les information pour Obj_Win_3
                        # 🖨
                        if current_line >= 3:
                            if optional_static_agent:
                                # Hard Code here. the format
                                    # obj_3, obj_4, obj_5 etc..
                                    # G1_3,  S1_3, W_4, SS_3
                                key_code = "%s_%d" % (check_obj, current_line)
                                optional_static_agent.increase_cnts(key_code)
                            else:
                                pass
                        
                        # 🖨
                        if current_line == 2 and check_obj == "W1":
                            try:
                                key_code = "%s_%d" % (check_obj, current_line)
                                optional_static_agent.increase_cnts(key_code)
                            except:
                                print("[🖨]No wild-2 in this job-card")
            
    
        # calculate the wild
        # 🎹: v2 version and special fix the Wild self-winning logic issue
        #     再次確認中:  結果發現 每次 loop non-wild-obj , we get w-w-w-L1, w-w-w-h1 etc.. logic is correct to add comparing wild line
        #                but, w-w-w-w-w 5 lines,  will not being count... fix now !
        for line_index , each_line_list in enumerate(self.line_setting_list):
            count        = 0 
            current_line_special_check_w_win5 = 0
            current_wild_gain = 0.0

            for col_index in range(self.col_lens_by_line_setting_list):
                # count > line_cnts
                count += 1

                current_symbol = list_r[col_index][each_line_list[col_index]]

                if current_symbol not in ["W1"]:
                    break
                else:
                    current_line_special_check_w_win5 = count

            # 🎹: v2 version and special fix the Wild self-winning logic issue
            #     再次確認中:  結果發現 每次 loop non-wild-obj , we get w-w-w-L1, w-w-w-h1 etc.. logic is correct to add comparing wild line
            #                but, w-w-w-w-w 5 lines,  will not being count... fix now !
            # 🎹: check w-w-w-w-w w-5 case only , see see.  
            if current_line_special_check_w_win5 >= 5:
                # Obtenir gain: bet_amount= 1/ how_manh_lines
                bet_amount = 1 / len(self.line_setting_list)
                bet_rate   = bet_rate_agent.obtenir_bet_rate_par_obj_et_bet_index("W1",current_line_special_check_w_win5)
                # Obtenir_bet_rate_par_obj_et_bet_index('G1',3) means:  bet rate with G1_3_lines
                current_wild_gain = bet_amount * bet_rate

                # 💰: add wild_gain
                gain += current_wild_gain

                # 🐼
                win_line_index          = line_index + 1


                system_msg += "[%4d]: 第%3d條線, Symbol: %3s,  %3d連線,  bet_rate =  %d , gain = %.4f\n"%(run_id,win_line_index,"W1",current_line_special_check_w_win5, bet_rate,current_wild_gain)
                    

                # Enregistrer des données a Pandas
                # Target: {'Run_ID': int(0),'Win_Obj':'S1',"Bet_Rate_3": 5,"Win_Line":3}
                if optional_pd is not None:
                    run_id_col           = "Run_ID"
                    run_id_value         = int(run_id)
                    win_obj_col          = "Win_Obj"
                    win_obj_value        = "W1"
                    bet_rate_index_col   = "Bet_Rate_%d"%current_line_special_check_w_win5
                    bet_rate_index_value = bet_rate
                    win_line_col         = "Win_Line"
                    win_line_value       = int(win_line_index)
                    gain_col             = "Gain"
                    gain_value           = current_wild_gain 
                    list_r_col           = "List_R"
                    list_r_value         = copy.deepcopy(list_r)
                    group_line_col       ="Group_Win_Line"
                    group_line_value     = int(current_line)
                    input_dict           = {group_line_col:group_line_value,run_id_col:run_id_value,win_obj_col:win_obj_value,bet_rate_index_col:bet_rate_index_value,win_line_col:win_line_value,gain_col:gain_value,list_r_col:list_r_value}
                    optional_pd = optional_pd.append(input_dict,ignore_index=True)
                    # Change to int
                    my_int_col_list = [run_id_col,win_line_col,group_line_col]
                    optional_pd[ my_int_col_list] = optional_pd[my_int_col_list].astype(int)
                    # Set the list_r column in the last column
                    front_or_end_list = [group_line_col,run_id_col, win_obj_col,win_line_col,gain_col,list_r_col]
                    optional_pd = optional_pd[[run_id_col,group_line_col, win_obj_col, win_line_col, gain_col] +[c for c in optional_pd if c not in front_or_end_list] + [list_r_col]]
                else:
                    pass
                
        #return 0, system_msg, debug_msg
        # curr_gain , sys_msg, _ , pytest_data_list , self.main_pd 
        if optional_pd is not None:
            return wrong_gain, system_msg, debug_msg, pytest_data_list  , optional_pd , return_2_gain , return_3_gain , return_4_gain , return_5_gain 
        else:
            return wrong_gain, system_msg, debug_msg, pytest_data_list  ,  optional_pd , return_2_gain, return_3_gain , return_4_gain , return_5_gain

    
                






    # ################      About claculer_rtp  #######################################
        # Utilier the self.apply_type et self.apply_version pour choisr les fontion
        # Tu peux implment apres the mutual function de way et line.
    # Implement this later,  since, i got two partner agent: static_agent, bet_rate_agent, 
    #           currently, je ne sais pas comment faire pout pass these two agent into calculer_rtp in good way.
    def calculer_rtp(self,input_list_r):
        # Case 1: way
        if self.apply_type == "way":
            if self.apply_version == "v1":
                RTP,debug_msg, system_msg = self.calculer_rtp_by_way_v1(input_list_r)
                return RTP, debug_msg, system_msg
            else:
                print("[Error]: No Match Version for %s"%self.apply_version)
        # Case 2: line
        elif self.apply_type == "line":
            if self.apply_version == "line_setting_v1":
                return self.calculer_rtp_by_line_setting_v1(input_list_r) # Return: RTP, Debug_Msg, System_MSG
        # Case 3: no line, no way, error!
        else:
            print("[Error]: No Match slot_type for %s"%self.apply_type)
    # --------------------------------------------------------------------------------------------------------------------------------------------------



    # ########################## Way Functions List #######################################################################
        #####       calculer_rtp_by_way_v1 for Panda               -> Need to implement later
        #####       calculer_rtp_by_way_v2 for Way_Transforemer    -> Need to implement later
        #####      ----------------------------------------------------------
        ####       This function use add_bet_rate_agent() -> implement in the future version
        ####       This function use self.partner_agent_partner_agent_list[0] , I shall use self.partner_list["function_name"] to avoid call un-known function.  
    # [Jason]:don't use this , bad_naming. use: add_partner_agent instead
    def add_bet_rate_agent(self,input_name,input_class):
       temp_class = input_class
       self.partner_agent_list.append(temp_class)
       self.partner_agent_dictionary.update({self.partner_agent_index: input_name })
       self.partner_agent_inverse_dictionary = { v: k for k, v in self.partner_agent_dictionary.items()}
       self.partner_agent_index +=1

    # calculer_rtp_by_way_v1:
        ###         __judge_wild_line_ou_non()
        #####                __deep_loop_judge_wild()
        #####      ----------------------------------------------------------
        ####       This function use add_bet_rate_agent() -> implement in the future version
        ####       This function use self.partner_agent_partner_agent_list[0] , I shall use self.partner_list["function_name"] to avoid call un-known function.
    def calculer_rtp_by_way_v1(self,list_r):
        

        #print("list_r inside calculer_rtp_by_way_v1 is %s" %list_r)

        debug_msg  = "[calculer_rtp_by_way_v1]: \n"
        system_msg = ""
        RTP = 0


        # Compute the numero de symbol avec wild 
        # Puis,   numero de symbol =   numero de symbol avec wild - numero de wild 
        for obj in self.linable_list:
                
            # Deep Loop Checking with obj
            # Check 3 lines
            input_list_r = copy.deepcopy(list_r)
            line_trois, tem_debug_msg, tem_sys_msg = self.__judge_wild_line_ou_non(input_list_r,3,obj)
            debug_msg  += tem_debug_msg + "\n"
            #system_msg += tem_sys_msg   + "\n"

            # Check 4 lines
            input_list_r = copy.deepcopy(list_r)
            line_quatre, tem_debug_msg, tem_sys_msg = self.__judge_wild_line_ou_non(input_list_r,4,obj)
            debug_msg  += tem_debug_msg + "\n"
            #system_msg += tem_sys_msg   + "\n"
            
            # Check 5 lines
            input_list_r = copy.deepcopy(list_r)
            line_cinq, tem_debug_msg, tem_sys_msg = self.__judge_wild_line_ou_non(input_list_r,5,obj)
            debug_msg  += tem_debug_msg + "\n"
            #system_msg += tem_sys_msg   + "\n"

            
            gain = 0
            if   line_cinq > 0:
                gain = line_cinq * self.partner_agent_list[0].obtenir_bet_rate(obj,5)
                debug_msg += "[%s]: 5 lines: gain = %2.4f , line_number = %d,   rate =  %2.4f\n" % (obj, gain, line_cinq, \
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 5))

                system_msg += "[%s]: 五連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_cinq, \
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 5))

            elif line_quatre > 0:
                gain = line_quatre * self.partner_agent_list[0].obtenir_bet_rate(obj, 4)
                debug_msg += "[%s]: 4 lines: gain = %2.4f , line_number = %d,   rate =  %2.4f\n" % (obj, gain, line_quatre,\
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 4))
                system_msg += "[%s]: 四連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_quatre, \
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 4))
            elif line_trois > 0:
                gain = line_trois * self.partner_agent_list[0].obtenir_bet_rate(obj, 3)
                debug_msg += "[%s]: 3 lines: gain = %2.4f , line_number = %d,   rate =  %2.4f\n" % (obj, gain, line_trois, \
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 3))
                system_msg += "[%s]: 三連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_trois,\
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 3))
            RTP += gain

        return RTP,debug_msg, system_msg
        
    # calculer_rtp_by_way_v2: [Way]: Apply to Way 
        ###         __judge_wild_line_ou_non_v1(default_col_size=3 , optional_col_size_list=False)
        #####               if optional_col_size_list:
        #####                        __deep_loop_judge_wild_v1_par_col_size_list(col_size_list)                                    
        #####               else:
        #####                        __deep_loop_judge_wild(default_col_size)
    def calculer_rtp_by_way_v2(self, list_r):

        #print("list_r inside calculer_rtp_by_way_v1 is %s" %list_r)

        debug_msg = "[calculer_rtp_by_way_v1]: \n"
        system_msg = ""
        RTP = 0


        # Faire col_size_list pour __deep_loop 
        input_col_size_list = [len(tem_list) for tem_list in list_r]

        print("list_r = ",list_r)
        print("input_col_size_list = ",input_col_size_list)

        # Compute the numero de symbol avec wild
        # Puis,   numero de symbol =   numero de symbol avec wild - numero de wild
        for obj in self.linable_list:

            # Deep Loop Checking with obj
            # Check 3 lines
            input_list_r = copy.deepcopy(list_r)
            line_trois, tem_debug_msg, tem_sys_msg = self.__judge_wild_line_ou_non_v1(input_list_r, 3, obj,optional_col_size_list=input_col_size_list)
            debug_msg += tem_debug_msg + "\n"
            #system_msg += tem_sys_msg   + "\n"

            # Check 4 lines
            input_list_r = copy.deepcopy(list_r)
            line_quatre, tem_debug_msg, tem_sys_msg = self.__judge_wild_line_ou_non_v1(input_list_r, 4, obj,optional_col_size_list=input_col_size_list)
            debug_msg += tem_debug_msg + "\n"
            #system_msg += tem_sys_msg   + "\n"

            # Check 5 lines
            input_list_r = copy.deepcopy(list_r)
            line_cinq, tem_debug_msg, tem_sys_msg = self.__judge_wild_line_ou_non_v1(input_list_r, 5, obj,optional_col_size_list=input_col_size_list)
            debug_msg += tem_debug_msg + "\n"
            #system_msg += tem_sys_msg   + "\n"

            # Check 6 lines
            input_list_r = copy.deepcopy(list_r)
            line_six, tem_debug_msg, tem_sys_msg = self.__judge_wild_line_ou_non_v1(input_list_r, 6, obj,optional_col_size_list=input_col_size_list)
            debug_msg += tem_debug_msg + "\n"
            #system_msg += tem_sys_msg   + "\n"

            gain = 0
            if line_six > 0:
                gain = line_six * self.partner_agent_list[0].obtenir_bet_rate(obj, 5)
                debug_msg += "[%s]: 6 lines: gain = %2.4f , line_number = %d,   rate =  %2.4f\n" % (obj, gain, line_six,self.partner_agent_list[0].obtenir_bet_rate(obj, 6))

                system_msg += "[%s]: 六連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_six,self.partner_agent_list[0].obtenir_bet_rate(obj, 6))

            elif line_cinq > 0:
                gain = line_cinq * self.partner_agent_list[0].obtenir_bet_rate(obj, 5)
                debug_msg += "[%s]: 5 lines: gain = %2.4f , line_number = %d,   rate =  %2.4f\n" % (obj, gain, line_cinq,self.partner_agent_list[0].obtenir_bet_rate(obj, 5))

                system_msg += "[%s]: 五連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_cinq,self.partner_agent_list[0].obtenir_bet_rate(obj, 5))

            elif line_quatre > 0:
                gain = line_quatre * \
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 4)
                debug_msg += "[%s]: 4 lines: gain = %2.4f , line_number = %d,   rate =  %2.4f\n" % (obj, gain, line_quatre,
                                                                                                    self.partner_agent_list[0].obtenir_bet_rate(obj, 4))
                system_msg += "[%s]: 四連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_quatre,
                                                                                      self.partner_agent_list[0].obtenir_bet_rate(obj, 4))
            elif line_trois > 0:
                gain = line_trois * \
                    self.partner_agent_list[0].obtenir_bet_rate(obj, 3)
                debug_msg += "[%s]: 3 lines: gain = %2.4f , line_number = %d,   rate =  %2.4f\n" % (obj, gain, line_trois,
                                                                                                    self.partner_agent_list[0].obtenir_bet_rate(obj, 3))
                system_msg += "[%s]: 三連線: gain = %2.4f , 線數 = %d,   賠率 =  %2.4f\n" % (obj, gain, line_trois,
                                                                                      self.partner_agent_list[0].obtenir_bet_rate(obj, 3))
            RTP += gain

        return RTP, debug_msg, system_msg

    def __judge_wild_line_ou_non(self,input_list_r, input_numero_de_line, input_symbol):
        system_msg = ""
        debug_msg  = "__judge_wild_line_ou_non(input_list_r,input_numero_de_line, input_symbol): \n"
        # Check si le symbol dans le range ou non:
        judge_list_r = [each_col for index, each_col in enumerate(input_list_r) if index < input_numero_de_line]
        debug_msg += "judge_list_r=  " + "%s\n"%judge_list_r

        # Chercher the symbol cnts dans tout le col. 
        # Par example: pour list_r              = [['B', 'A', 'T'], ['J', 'SE', 'K'], ['Q', 'B', 'K']]
        # judge_list_r_cnts_symbol_list for 'B' = [      1        ,         0       ,        1       ]
        judge_list_r_cnts_symbol_list = []
        check_total_symbol_cnts       =  0

        for any_list_r in judge_list_r:
            # Obtenir symbol_cnts:
            tem_cnts_symbol_list     = collections.Counter(any_list_r)
            tem_cnts_symbol          = tem_cnts_symbol_list[input_symbol]

            # Ajouter symbol_cnts_total:
            check_total_symbol_cnts += tem_cnts_symbol
            judge_list_r_cnts_symbol_list.append(tem_cnts_symbol)

        debug_msg += "detect '%s' , judge_list_r_cnts_symbol_list = "%input_symbol + "%s\n"%judge_list_r_cnts_symbol_list

        # Si symbol n'est pas dans la region. return False
        if check_total_symbol_cnts == 0:
            return 0, debug_msg,system_msg # no any line_cnts for this symbol
        else:
            # Deep loop
            input_limit   = input_numero_de_line - 1 #input_numero_de_line = 3, input_limit = 2
            input_layer   = -1 # Start from 0,...etc..
            tem_list      = [0 for _ in range(input_numero_de_line)]  #input_numero_de_line = 3, [0,0,0]
            each_col_size = 3
            check_all_kind_of_set_list = []
            __debug_msg_list = []

            # Run 
            check_all_kind_of_set_list = self.__deep_loop_judge_wild(input_symbol,judge_list_r,input_limit,input_layer,each_col_size,tem_list,check_all_kind_of_set_list,__debug_msg_list)

        for any_debug_msg in __debug_msg_list:
            debug_msg += any_debug_msg + "\n"
        
        
        #line_cnts
        debug_msg += "check_all_kind_of_set_list = %s"%check_all_kind_of_set_list
        line_cnts = len(check_all_kind_of_set_list) 
        return line_cnts, debug_msg, system_msg

    # New version v1: 
        ##  add col_size input setting (Default)
        ##  add support optional_col_size_list for different col_size in different col..
    def __judge_wild_line_ou_non_v1(self,input_list_r, input_numero_de_line, input_symbol,default_col_size=3,optional_col_size_list=False):
        system_msg = ""
        debug_msg  = "__judge_wild_line_ou_non(input_list_r,input_numero_de_line, input_symbol): \n"
        # Check si le symbol dans le range ou non:
        judge_list_r = [each_col for index, each_col in enumerate(input_list_r) if index < input_numero_de_line]
        debug_msg += "judge_list_r=  " + "%s\n"%judge_list_r

        # Chercher the symbol cnts dans tout le col. 
        # Par example: pour list_r              = [['B', 'A', 'T'], ['J', 'SE', 'K'], ['Q', 'B', 'K']]
        # judge_list_r_cnts_symbol_list for 'B' = [      1        ,         0       ,        1       ]
        judge_list_r_cnts_symbol_list = []
        check_total_symbol_cnts       =  0

        for any_list_r in judge_list_r:
            # Obtenir symbol_cnts:
            tem_cnts_symbol_list     = collections.Counter(any_list_r)
            tem_cnts_symbol          = tem_cnts_symbol_list[input_symbol]

            # Ajouter symbol_cnts_total:
            check_total_symbol_cnts += tem_cnts_symbol
            judge_list_r_cnts_symbol_list.append(tem_cnts_symbol)

        debug_msg += "detect '%s' , judge_list_r_cnts_symbol_list = "%input_symbol + "%s\n"%judge_list_r_cnts_symbol_list

        # Si symbol n'est pas dans la region. return False
        if check_total_symbol_cnts == 0:
            return 0, debug_msg,system_msg # no any line_cnts for this symbol
        else:
            # Deep loop
            input_limit   = input_numero_de_line - 1 #input_numero_de_line = 3, input_limit = 2
            input_layer   = -1 # Start from 0,...etc..
            tem_list      = [0 for _ in range(input_numero_de_line)]  #input_numero_de_line = 3, [0,0,0]
            
            check_all_kind_of_set_list = []
            __debug_msg_list = []

            
            # optional_col_size is set, used col_size_list for each col
            if optional_col_size_list:
                debug_msg += "[Info]: Apply different col_size for each col with __deep_loop_judge_wild_v1_par_col_size_list(). Please make sure, you got the setting correctly.\n"
                # Run v1
                check_all_kind_of_set_list = self.__deep_loop_judge_wild_v1_par_col_size_list(input_symbol,judge_list_r,input_limit,input_layer,optional_col_size_list,tem_list,check_all_kind_of_set_list,__debug_msg_list)
            # optional_col_size is not set, use default fixed col size 
            else:
                each_col_size = default_col_size
                # Run v0
                check_all_kind_of_set_list = self.__deep_loop_judge_wild(input_symbol,judge_list_r,input_limit,input_layer,each_col_size,tem_list,check_all_kind_of_set_list,__debug_msg_list)

        for any_debug_msg in __debug_msg_list:
            debug_msg += any_debug_msg + "\n"
        
        
        #line_cnts
        debug_msg += "check_all_kind_of_set_list = %s"%check_all_kind_of_set_list
        line_cnts = len(check_all_kind_of_set_list) 
        return line_cnts, debug_msg, system_msg

    #----------- How to use the DFS ----------------#
        ### index: 0,1,2
        #  input_limit = 2
        #  input_layer = -1

        ### tem_list:          (need to tune for 3: [0,0,0] 4: [0,0,0,0])
        ### each_col_size = 3 (fixed size for each col )

        #check_all_kind_of_set_list  = []
        #tem_list = [0,0,0]
        #each_col_size = 3
    ### Run:
    #check_all_kind_of_set_list = __deep_loop_judge_wild(judge_list,input_limit,input_layer,3,tem_list,check_all_kind_of_set_list)
    def __deep_loop_judge_wild(self,input_symbol,judge_list, layer_limit, input_layer, each_col_size, tem_list, check_all_kind_of_set_list,__debug_msg_list):

        input_layer += 1

        # Arriver deep bottom
        if input_layer > layer_limit:
            
            # Copy new instance
            new_tem_list = copy.deepcopy(tem_list)
        
            # Judge each set et updated check_all_kind_of_set_list
            self.__judge_each_set_est_line_ou_non(input_symbol,judge_list, new_tem_list,check_all_kind_of_set_list, __debug_msg_list)
            return check_all_kind_of_set_list

        # Entrer deep
        for any_value in range(each_col_size):
            tem_list[input_layer] = any_value
            check_all_kind_of_set_list = self.__deep_loop_judge_wild(input_symbol,judge_list, layer_limit, input_layer, each_col_size, tem_list, check_all_kind_of_set_list,__debug_msg_list)


        return check_all_kind_of_set_list
    
    # le nouvell version: pour faire la col_size different par 'col_size_list': Way_Transformer project , will be applied.
    def __deep_loop_judge_wild_v1_par_col_size_list(self,input_symbol,judge_list, layer_limit, input_layer, col_size_list, tem_list, check_all_kind_of_set_list,__debug_msg_list):
        input_layer += 1

        # Arriver deep bottom
        if input_layer > layer_limit:   
            # Copy new instance
            new_tem_list = copy.deepcopy(tem_list)
        
            # Judge each set et updated check_all_kind_of_set_list
            self.__judge_each_set_est_line_ou_non(input_symbol,judge_list, new_tem_list,check_all_kind_of_set_list, __debug_msg_list)
            return check_all_kind_of_set_list

        # Entrer deep, et loop par different col_size
        for any_value in range(col_size_list[input_layer]):
            tem_list[input_layer] = any_value
            check_all_kind_of_set_list = self.__deep_loop_judge_wild_v1_par_col_size_list(input_symbol,judge_list, layer_limit, input_layer, col_size_list, tem_list, check_all_kind_of_set_list,__debug_msg_list)

        return check_all_kind_of_set_list

    # Check each set like ['B','A','B'] etc..
    def __judge_each_set_est_line_ou_non(self,input_symbol,input_judge_list, input_new_tem_list,__get_line_list,__debug_msg_list):
        each_line_set = []
        for any_layer, any_layer_index in enumerate(input_new_tem_list):
            tem_symbol = input_judge_list[any_layer][any_layer_index]
            each_line_set.append(tem_symbol)

        if input_symbol not in each_line_set:
            #print("No, with line_set = %s" % each_line_set)
            return 
        else:

            # Check if any obj is ok
            for any_obj in each_line_set:
                if any_obj == input_symbol or any_obj == 'W':
                    pass
                else:
                    #print("No, with line_set = %s" % each_line_set)
                    return

            # Pass all if
            debug_msg = "Yes, with line_set = %s" % each_line_set
            __debug_msg_list.append(debug_msg)
            __get_line_list.append(input_new_tem_list)

    # #####################################################################################################################################################


if __name__ == "__main__":

    # Test_00:  slot_table_agent: implement later ..
    """

    # Les setting:
    list_r = [ ['A','B','C'], \
                ['B1','B2','B3'], \
                ['C1','C2','C3'], \
                ['D1','D2','D3'], \
                ['E','E','E']
        ]

    input_cols     = 5
    input_row_list = [3, 3, 3, 3, 3]

    # Initial Agent
    msg            = "Test list_r    =      %s\n"%list_r
    msg           += "Input row list =      %s\n"%input_row_list
    table_agent    = slot_table_agent(input_cols,input_row_list)
    msg           += table_agent.afficher_table_par_list_r(list_r)
    print(msg)

    
    # Test_00:  slot_tabler_agent: Test different size of row
    # Les setting:
    list_r = [ ['A','B','C'], \
                ['B1','B2','B3','B4','B5'], \
                ['C1','C2','C3'], \
                ['D1','D2','D3'], \
                ['E','E','E','E']
        ]

    input_cols     = 5
    input_row_list = [3, 5, 3, 3, 4]

    # Initial Agent
    msg            = "Test list_r    =      %s\n"%list_r
    msg           += "Input row list =      %s\n"%input_row_list
    table_agent    = slot_table_agent(input_cols,input_row_list)
    msg           += table_agent.afficher_table_par_list_r(list_r)
    print(msg)


    # Test_01:  different rolling with "test_case_01_different_row_size.xlsx"

    # Obtenir les args:
    get_main_args = ana_sys.analyzer_input_args()

    # Lire le fichier par défaut: TEST Case Default files.
    input_excelname = "test_case_01_different_row_size.xlsx"

    # Lire réglage:
    wb = xlrd.open_workbook(input_excelname)
    setting_sheet       = wb.sheet_by_name("Setting")
    mg_roll_table_sheet = wb.sheet_by_name("MG_Roll_Table")


    # Créer output_agent
    # # Créer output_agent
    ##############################################
    output_agent = ana_sys.analyzer_output_agent()
    ##############################################
    output_agent.set_debug_mode(get_main_args.debug_mode)
    output_agent.set_show_info(get_main_args.show_info)
    output_agent.set_output_folder(get_main_args.output_folder)
    input_default_file_name = "output_" + ana_sys.analyzer_get_tem_file_name_format_by_time()
    input_summary_file_name = "Final_Summary_" + ana_sys.analyzer_get_tem_file_name_format_by_time()
    output_agent.set_default_output_file_name(input_default_file_name)    

    output_info = output_agent.obtenir_info()
    print(output_info)


    # Lire les Setting:
    excel_agent  = ana_sys.read_excel_agent()
    msg          = excel_agent.show_les_key_mots_de_gauche_a_droite(setting_sheet)
    print(msg)

    setting_mode          , _     = excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Mode:")
    setting_numbers_of_col , _    = excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Column:",optional_format='int')
    setting_scatter_symbol , _    = excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Scatter:")
    setting_wild_symbol , _       = excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Wild:")
    setting_scatter_numbers, _    = excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"ScatterNumberEnterFG:",optional_format='int')
    setting_nubmer_of_row_list, _ = excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(setting_sheet,"Row:",optional_format='int')

    msg  = "[系統]: 基本設定如下:\n"
    msg += "模式:              %s\n"%setting_mode
    msg += "Col數量:           %d\n"%setting_numbers_of_col
    msg += "Scatter 圖標:      %s\n"%setting_scatter_symbol
    msg += "Wild 圖標:         %s\n"%setting_wild_symbol
    msg += "幾個%s to FG:      %d\n"%(setting_scatter_symbol,setting_scatter_numbers)
    msg += "Row number list:  %s\n"%(setting_nubmer_of_row_list)

    
    

    # Lire les MG Roll Table:
    mg_roll_r1_list ,  _         = excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R1:")
    mg_roll_r2_list ,  _         = excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R2:")
    mg_roll_r3_list ,  _         = excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R3:")
    mg_roll_r4_list ,  _         = excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R4:")
    mg_roll_r5_list ,  _         = excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R5:")


    msg += "MG第1輪:          %s\n"%mg_roll_r1_list
    msg += "MG第2輪:          %s\n"%mg_roll_r2_list
    msg += "MG第3輪:          %s\n"%mg_roll_r3_list
    msg += "MG第4輪:          %s\n"%mg_roll_r4_list
    msg += "MG第5輪:          %s\n"%mg_roll_r5_list

    # Affichier les setting:
    print(msg)
  
    # Faire mg_roll_list_list
    mg_roll_list_list = []
    mg_roll_list_list.append(mg_roll_r1_list)
    mg_roll_list_list.append(mg_roll_r2_list)
    mg_roll_list_list.append(mg_roll_r3_list)
    mg_roll_list_list.append(mg_roll_r4_list)
    mg_roll_list_list.append(mg_roll_r5_list)


    # Adjuouter mg_roll_list_list
    slot_table_agent = slot_table_agent(setting_numbers_of_col,setting_nubmer_of_row_list)
    slot_table_agent.ajouter_mg_roll_table(mg_roll_list_list)
    mg_roll_msg = slot_table_agent.les_information()
    print(mg_roll_msg)

    # Show first 5 runs:
    slot_table_agent.show_mg_roll_table_head()



    # Start the run 
    # ------- run_setting   -------------------
    start_run = 0
    end_run   = 10
    # ------  output_setting ----------------
    set_output_flag = True
    output_agent.set_output_flag_by_excel(set_output_flag)
    ###################################################################

    #for any_run in range(start_run,end_run):

    for each_run in range(start_run,end_run):

        msg = "[%5d]轉:\n---------------\n"%each_run
        curr_list_r = slot_table_agent.obtenir_mg_roll_table_par_id(each_run)
        msg += slot_table_agent.afficher_table_par_list_r(curr_list_r)
        output_agent.output_agent(msg)


    ###############  TEST 02- With Line_Setting_List ################
    print("###############  TEST 02- With Line_Setting_List ################\n")

    

    setting_linable_obj_list  = ['G1', 'S1', 'S2', 'C1', 'C2', 'C3', 'I1', 'I2', 'I3', 'I4', 'W', 'SS']
    setting_wildable_obj_list = ['W']
    setting_game_type         = 'line'
    # 1th, 2nd, 3rd line_setting. 
    mg_line_setting_list      = [  [0, 0, 0, 0, 0],\
                                   [1, 1, 1, 1, 1],\
                                   [2, 2, 2, 2, 2] ]


    rtp_agent = slot_calculer_rtp_agent('line_design_rtp_agent')
    rtp_agent.set_linable_list(setting_linable_obj_list)
    rtp_agent.set_wild_list(setting_wildable_obj_list)
    rtp_agent.set_type(setting_game_type)
    rtp_agent.set_version('line_setting_v1')
    rtp_agent.set_line_setting_list(mg_line_setting_list)
    #rtp_agent.add_bet_rate_agent('bet_rate_agent', main_slot_bet_rate_agent)
    rtp_agent_info = rtp_agent.les_information()
    output_agent.output_agent(rtp_agent_info)


    # Test run
    list_r =   [['G1', 'I2', 'I2'], ['G1', 'S1', 'S2'], ['G1', 'I1', 'G1'], ['I4', 'I1', 'W'], ['SS', 'S1', 'S2']]

    print(list_r)
    _, msg , _ = rtp_agent.calculer_rtp(list_r)
    print(msg)

    # Test Run with wild 
    list_r = [['G1', 'W', 'I2'], ['G1', 'W', 'S2'], ['G1', 'W', 'G1'], ['I4', 'I1', 'W'], ['SS', 'S1', 'S2']]
    print(list_r)
    _, msg, _ = rtp_agent.calculer_rtp(list_r)
    print(msg)

    """