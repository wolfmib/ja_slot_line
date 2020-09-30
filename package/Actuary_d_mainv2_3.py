"""
v2 version: 
    - support S1, E1, H1, W1 etc.. format
    - support output package print out
    - add pytest_flag in run(self, pytest_flag=False).  This will initial the test_agent tand start test.


# 🏦  v2.1 version: fix the bug: need to add S1 to be count (S1-3 : 3, S1-4:  10, S1-5: 100)
      v2.2 .... 
      v2.3 Jean: ajouter le gain de scatter-deux,  

3 Jean: log
    - 2020-09-25 apres'midi:  
        - on termine le premier test-run avec python-test.
        - puis, nous devons adjouter le gain de scatter-deux et afficher le rtp egalement.
        -                    ajouter un gain scatter     
    - 2020-09-25 check the rtp: 0.59 (simulation) vs 0.54 (actuary)
        -  let's check the 2, 3, 4, 5 rtp distribution first fuck!! gogogo!!

"""


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
import matplotlib.pyplot as plt
import numpy as np

# Pandas
import pandas as pd
import math

#from utility import *
import time

# 🎲: for main program use only, load package first, it's important. 
try:
    import package.analyzer_system as ana_sys
except:
    import analyzer_system as ana_sys
    
# 🎲: for main program use only, remove try, except logic..
# 🎹: load v2 version to support W1, W2, W3 S1, S2, S3 logic, please loading with v2 table
#     load v2.1 version: 
#                 1. support prevent checking S1 inside the rtp_agent.run() . 
#                 2. S1 count logic is being iplement outside the libs.
try:
    import package.jackpot_analyzer_slot_v2_2 as ana_slot
except:
    import jackpot_analyzer_slot_v2_2 as ana_slot
    

# 🎁:  support input symbol for comparning. 
# 🏢:  load package first, it's important. 
try:
    import package.ja_slot_count_ss as count_ss
except:
    import ja_slot_count_ss as count_ss


# 🖨💹 Excel static Files v2 version for output
    #  m%, 
    # reel, 
    # bet_rate, 
    # win_prob_distribution
# 🏢:  load package first, it's important. 
try:
    import package.ja_static_write_rtp_info_v2 as ja_static_rtp 
except:
    import ja_static_write_rtp_info_v2 as ja_static_rtp 


# 🐼 🐳
# 🏢:  load package first, it's important. 
try:
    import package.ja_docker_write_pkl as ja_write_pkl
except:
    import ja_docker_write_pkl as ja_write_pkl

# 🐼, # 🎲: for main program use only, remove try, except logic..
# 🏢:  load package first, it's important. 
try:
    import package.ja_datascientist_slot_symbol_distribution as ja_symbol_distribution
except:
    import ja_datascientist_slot_symbol_distribution as ja_symbol_distribution



# 📮: api post libs
import requests
import random

# 🔱:  handling the "False" to bool value False !
import distutils.util


class agent():
    # 📅 add show log 
    def __init__(self,default_excelname="job_card_01_mg_case_1.xlsx",show_log=False,show_debug=False):

        # 🎹: v2 version, notification
        print("[🎹]: load v2 version to support W1, W2, W3 S1, S2, S3 logic, please loading with v2 table")
        print("[🎹]: load v2 version to support pytest, code self.run() to self. run(pytest_flag=True)")



        # 🏦  v2.1 version: fix the bug: need to add S1 to be count (S1-3 : 3, S1-4:  10, S1-5: 100)
        print("🏦  v2.1 version:    Pleasse set the S1 score ")
        self.S1_2_pay_score = float(input("S1: 2      score =  2\n"))
        self.S1_3_pay_score = float(input("S1: 3      score =  5\n"))
        self.S1_4_pay_score = float(input("S1: 4      score = 20\n"))
        self.S1_5_pay_score = float(input("S1: 5      score = 500\n"))

        print("🏦  v2.1 version:    Your extra pay-table for S1 (3, 4, 5 is ...")
        print(self.S1_2_pay_score)
        print(self.S1_3_pay_score) 
        print(self.S1_4_pay_score) 
        print(self.S1_5_pay_score) 
        input("🏦  v2.1 version:    OK....... Press Enter")
        

        # 🏦  v2.1 version:  let's metric the cnts
        self.S1_2_cnts = 0
        self.S1_3_cnts = 0
        self.S1_4_cnts = 0
        self.S1_5_cnts = 0





        # 👨‍⚕️: let's see the H1-2 RTP portion
        self.h2_2_rtp = 0.0000000000000000000001



        # 🎹 🧪: v2 and make pytest as well..: 
        #        default is False
        #        become True When  activated at self.run(self,pytest_flag=True)
        self.pytest_status = False

         
        #      you can set to [2,3,4,5 ] if needed. ...
        print("[🎲 ,🐼] Default static_document_01 output is count  win line 3, 4, 5 for each object")
        print("[🎲]: C'est important.. c'est image suitalble pour symbol bet-rate 3,4,5 et wild bet-rate 2,3,4,5.")
        print("[🎲]: Si vous utiliser symbol bet-rate 2,3,4,5, c'est problem...  tu dois implement dansla la 806_SLOT_project's ***package/docker_v1.py") 
        print("[🦜]: I hope you understand !!  Press Enter if you read this")
        print("[🦜]: usning the rep_calcuer_rtp_line_v2_for_slot,  because wild_2_line is be count as well....")
        read_nothing = input("[🦜]You get it ???\n\n")


        print("Bonjour")

        # 🖨
        print(" Please set the output name , so you can easily find it in output folder 📂")
        print(" e.g.:   test_rtp_95_50w_runs   ->  output_test_rtp_95_50w_runs_xxxxxxxxx.txt")
        self.tag_filename = input("Type: \n")

        # 📊
        print(" Please set the static output name ,")
        print(" e.g.:   static_M_rtp   ->  static_M_rtp.xlsx")
        self.static_filename = input("Type: \n")



        # Lire le fichier par défaut:
        self.input_excelname = default_excelname

        # Lire réglage:
        wb = xlrd.open_workbook(self.input_excelname)
        setting_sheet         = wb.sheet_by_name("Setting")
        mg_roll_table_sheet   = wb.sheet_by_name("MG_Roll_Table")
        mg_line_setting_sheet = wb.sheet_by_name("MG_Line_Setting")


        # Créer output_agent
        # # Créer output_agent
        ##############################################
        self.output_agent = ana_sys.analyzer_output_agent()
        ##############################################
        # 📅 add show debug
        if show_debug == True:
            self.output_agent.set_debug_mode(True)
        else:
            self.output_agent.set_debug_mode(False)


        # 📅 add show log 
        if show_log == True:
            self.output_agent.set_show_info(True)
        else:
            self.output_agent.set_show_info(False)
            
        
        self.output_agent.set_output_folder("output")


        # 🖨
        self.input_default_file_name = "output_" + self.tag_filename + "_" + ana_sys.analyzer_get_tem_file_name_format_by_time()
        self.input_summary_file_name = "Final_Summary_" + self.tag_filename + "_" + ana_sys.analyzer_get_tem_file_name_format_by_time()
        self.output_agent.set_default_output_file_name(self.input_default_file_name)    

        output_info = self.output_agent.obtenir_info()
        print(output_info)


        # 🖌
        self.rtp_list = []
        self.run_id_list = []
        print("🖌: Please write the chart name e.g. rtp_97_50w")
        self.rtp_name = input("Type: \n")



        # Lire les Setting:
        self.excel_agent  = ana_sys.read_excel_agent()
        msg          = self.excel_agent.show_les_key_mots_de_gauche_a_droite(setting_sheet)
        print(msg)

        self.setting_mode          , _     = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Mode:")
        self.setting_numbers_of_col , _    = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Column:",optional_format='int')
        self.setting_scatter_symbol , _    = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Scatter:")
        self.setting_wild_symbol , _       = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"Wild:")
        self.setting_scatter_numbers, _    = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col(setting_sheet,"ScatterNumberEnterFG:",optional_format='int')
        self.setting_number_of_row_list, _ = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(setting_sheet,"Row:",optional_format='int')

        msg  = "[系統]: 基本設定如下:\n"
        msg += "模式:              %s\n"%self.setting_mode
        msg += "Col數量:           %d\n"%self.setting_numbers_of_col
        msg += "Scatter 圖標:      %s\n"%self.setting_scatter_symbol
        msg += "Wild 圖標:         %s\n"%self.setting_wild_symbol
        msg += "幾個%s to FG:      %d\n"%(self.setting_scatter_symbol,self.setting_scatter_numbers)
        msg += "Row number list:  %s\n"%(self.setting_number_of_row_list)

    
        # Lire les MG Line Setting: Par Example 25 lines
        self.setting_line_number  , _     = self.excel_agent.obtenir_value_par_norm(mg_line_setting_sheet,"LineNumber:",optional_format='int')
        self.setting_roll_number  , _     = self.excel_agent.obtenir_value_par_norm(mg_line_setting_sheet,"RollNumber:",optional_format='int')
        self.mg_line_setting_list  , _    = self.excel_agent.obtenir_value_par_norm_by_input_table_range_dans_la_row_direction(mg_line_setting_sheet,"LineSetting:",self.setting_line_number,self.setting_roll_number,optional_format='int')

        msg += "[系統]: 中獎線設定如下:\n"
        msg += "線數:              %d\n"%self.setting_line_number
        msg += "輪數:              %d\n"%self.setting_roll_number
        for any_list in self.mg_line_setting_list:
            msg += "中獎線:           %s\n"%any_list
    

        # Lire les MG Roll Table:
        self.mg_roll_r1_list ,  _         = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R1:")
        self.mg_roll_r2_list ,  _         = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R2:")
        self.mg_roll_r3_list ,  _         = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R3:")
        self.mg_roll_r4_list ,  _         = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R4:")
        self.mg_roll_r5_list ,  _         = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(mg_roll_table_sheet,"R5:")

        msg += "\n\n"
        msg += "MG第1輪:          %s\n"%self.mg_roll_r1_list
        msg += "MG第2輪:          %s\n"%self.mg_roll_r2_list
        msg += "MG第3輪:          %s\n"%self.mg_roll_r3_list
        msg += "MG第4輪:          %s\n"%self.mg_roll_r4_list
        msg += "MG第5輪:          %s\n"%self.mg_roll_r5_list


        # Lire les Bet_Rate: Implement later
        # setting_linable_obj_list  Example:  ['G1','S1','S2','C1','C2','C3','I1','I2','I3','I4','W','SS'] 
        self.setting_linable_obj_list, _ = self.excel_agent.obtenir_value_par_norm_dans_tout_le_col_avec_auto_search_value_list_lens(setting_sheet, "LinableSymbol:")


        # setting_bet_rate_list_list Example:
            #setting_bet_rate_list_list =  [ [0, 0, 80, 200, 600],\
            #                                [0, 0, 40, 100, 300],\
            #                                [0, 0, 40, 100, 300],\
            #                                [0, 0, 16,  40, 120],\
            #                                [0, 0, 16,  40, 120],\
            #                                [0, 0, 16,  40, 120],\
            #                                [0, 0,  8,  20,  60],\
            #                                [0, 0,  8,  20,  60],\
            #                                [0, 0,  8,  20,  60],\
            #                                [0, 0,  8,  20,  60],\
            #                                [0, 0,  0,   0,   0],\
            #                                [0, 0,  0,   0,   0]
            #                              ]
        number_of_rows = len(self.setting_linable_obj_list)    # 12 symbols
        number_of_cols = self.setting_numbers_of_col           # 5 rolls
        self.setting_bet_rate_list_list, _ = self.excel_agent.obtenir_value_par_norm_by_input_table_ragne_dans_la_col_direction(setting_sheet,"LinableSymbol:",number_of_rows,number_of_cols,optional_format='float')
    
        # Créer the bet_slot_agent in main()
        self.main_slot_bet_rate_agent = ana_slot.slot_bet_rate_class_v1("line_bet_rate_agent")
        # Adjouter row by row
        for any_obj, any_bet_rate_list in zip(self.setting_linable_obj_list,self.setting_bet_rate_list_list):
            self.main_slot_bet_rate_agent.ajouter_obj_par_bet_rate_list(any_obj,any_bet_rate_list)

        msg += self.main_slot_bet_rate_agent.les_information()

        # Test 
        test_index    = 4  # for example: "C2"
        bet_index     = 5  # for example Bet_5
        msg += "\n--------------\nTest to Bet_%d bet with symbol %s\n"%(bet_index, self.setting_linable_obj_list[test_index])
        test_bet_value = self.main_slot_bet_rate_agent.obtenir_bet_rate_par_obj_et_bet_index(self.setting_linable_obj_list[test_index],bet_index)
        msg += "Bet_Value = %.2f\n------------\n"%test_bet_value

        # Affichier les setting:
        print(msg)
    
        # Faire mg_roll_list_list
        self.mg_roll_list_list = []
        self.mg_roll_list_list.append(self.mg_roll_r1_list)
        self.mg_roll_list_list.append(self.mg_roll_r2_list)
        self.mg_roll_list_list.append(self.mg_roll_r3_list)
        self.mg_roll_list_list.append(self.mg_roll_r4_list)
        self.mg_roll_list_list.append(self.mg_roll_r5_list)


        ###### Table_Agent: 
        # Adjuouter mg_roll_list_list
        self.slot_table_agent = ana_slot.slot_table_agent(self.setting_numbers_of_col,self.setting_number_of_row_list)
        self.slot_table_agent.ajouter_mg_roll_table(self.mg_roll_list_list)
        mg_roll_msg = self.slot_table_agent.les_information()
        print(mg_roll_msg)

        # Show first 5 runs:
        self.slot_table_agent.show_mg_roll_table_head()

        ###### Line_Setting_Analysis_Agent: 
        # Adjouter mg_roll_list_list
        self.slot_line_analysis_agent = ana_slot.slot_line_setting_analysis(self.setting_numbers_of_col,self.setting_number_of_row_list)
        self.slot_line_analysis_agent.ajouter_mg_roll_table(self.mg_roll_list_list)
        slot_line_setting_analysis_info = self.slot_line_analysis_agent.les_information()
        print(slot_line_setting_analysis_info)

        # Obtenir analysis information:
        # - line able list
        self.slot_line_analysis_agent.calculate_linable_probability_distribution___set_lineable_list(self.setting_linable_obj_list)
        self.slot_line_analysis_agent.calculate_linable_probability_distribution()




        ###### Start the run 

        # 🎮 Runs
        # ------- run_setting   -------------------
        self.start_run = 0
 

        # ------- run_setting   -------------------
        self.hit_cnts  = 0
        # ------  output_setting ----------------
        set_output_flag = True
        self.output_agent.set_output_flag_by_excel(set_output_flag)
        # ------  Initial rtp agent --------------
        # setting_wildable_obj_list = ['W']  # implement this later (from excel input)
        setting_game_type         = 'line' # implement this later (from excel input)
        self.rtp_agent                = ana_slot.slot_calculer_rtp_agent('line_design_rtp_agent')
        self.rtp_agent.set_linable_list(self.setting_linable_obj_list)
        self.rtp_agent.set_wild_list(self.setting_wild_symbol)
        self.rtp_agent.set_type(setting_game_type)
        self.rtp_agent.set_version('line_setting_v1')
        self.rtp_agent.set_line_setting_list(self.mg_line_setting_list)
        self.rtp_agent.add_bet_rate_agent('bet_rate_agent',self.main_slot_bet_rate_agent)
        rtp_agent_info = self.rtp_agent.les_information()
        self.output_agent.output_agent(rtp_agent_info)

        # TEST Partner fucntion
        check_msg = self.rtp_agent.call_partner_by_name('bet_rate_agent','les_information')
        print("check:\n",check_msg)
        ###################################################################

        #for any_run in range(start_run,end_run):


        # Excel G1 ~ prob ~ 0.04462, total_cnts = 7879300
        # Calculate the prob_list for checking first.


        # ---- Static agent -----------
        # Créer static_agent
        self.static_agent_v1            = ana_sys.analyzer_static_monitor_agent_v1()
        # Add Calss:  --> static_agent_v1.append_class("G1_3","G1_3連線")
        for any_obj in self.setting_linable_obj_list:
            english_name = "%s_3"%any_obj
            chinese_name = "%s_3連線"%any_obj      
            self.static_agent_v1.append_class(english_name,chinese_name)
        # Add to main_rtp_agent.
        self.rtp_agent.add_partner('static_agent_v1',self.static_agent_v1)
        static_info  = self.rtp_agent.call_partner_by_name('static_agent_v1','show_cnts')
        #static_info = static_agent_v1.show_cnts()
        print("Static Information")
        self.output_agent.output_agent(static_info)
        print(static_info)
        input("Press Check.....\n")
        # ----------------------------
        self.total_run_cnt = 0
        self.total_gain    = 0.0
        self.X2            = 0.0
        self.curr_variance = 0.0

    
        # ---  Pandas Solve Everyting ----
        self.main_pd = pd.DataFrame()



    def __see_rtp_from_pd(self,my_pd):

            current_run_id     = int(my_pd.Run_ID.max())
            total_run          = current_run_id +  1
          
            print("[,slot_typeline_docker_v1]Total run =  %6d"%total_run)

            gain_group   = my_pd.groupby(['Group_Win_Line'])
            f = {
                'Gain' : 'sum',
            }
            get_gain_data = gain_group.agg(f) #get_gain_data est DF
            get_gain_data['RTP'] = get_gain_data.Gain.apply(lambda x: x / total_run)
            # df = df.append({'List_R':list_r},ignore_index=True)

            print(get_gain_data)
            


        
    def __see_each_smbol_distribution(self,divided_cnts,my_pd):
        
        # Obtenir Count et Probability
            # count() Obtenir sum_of_rows
            # reset_index, creer nouvelle dataframe with correct et Assign sum_of_rows to ' Count' column
        symbol_group = my_pd.groupby(['Group_Win_Line','Win_Obj'])['Run_ID'].count().reset_index(name='Count')
        
        # Compute Probability
        symbol_group['Probability'] = symbol_group.Count.apply(lambda x: x / divided_cnts)
        print(symbol_group)


    # 回傳值:
         # curr_gain
         # curr_list_r: "SA","SB","SC","SD" or "SS" for FreeGame
    # 🎹: 如果 pytest_flag set to True
    #     第一次           :  Initial test_agent, then self.pytest_status= True.  之後就不用再re-initial
    #     第二次 to the end:  checking self.pytest_status = True,  直接use created agent to do pytest.  
    #       
    def run(self,pytest_flag=False):
    

        wrong_gain = 0 

        # Add run_cnt
        self.total_run_cnt +=1

        msg = "[%5d]轉:\n---------------\n"%self.total_run_cnt
        

        #########################################################
        curr_list_r = self.slot_table_agent.obtenir_mg_roll_table_par_natural_random(self.total_run_cnt)


        # 🙃: check wild-3 > h1-4 case
        # fixed la: curr_list_r = [["W1","H2","H3"],["W1","L1","L3"],["W1","L2","L3"],["H1","H1","H1"],["H5","H5","H5"]]
        # fixed la: curr_list_r = [["W1","H2","H3"],["W1","L1","L3"],["W1","L2","L3"],["W1","L5","L5"],["L3","H5","H5"]]


        # 🖨
        msg += self.slot_table_agent.afficher_table_par_list_r(curr_list_r)
        self.output_agent.output_agent(msg)
        

        # 🎁: Calculate the Free game here,   mode = counts of scatter
        # 🎹: v2 version, SS-> S1
        obtenir_scater_cnts = count_ss.run(curr_list_r,"S1")



        ####flfwmflwfnwkfnkf🦜 這邊
        ###################################### print("[Actuary_d_maiv2_2.py][line 462]: Checking error case....")
        ###################################### curr_list_r = [['S1', 'H3', 'W1'], ['H3', 'W1', 'L2'], ['H3', 'W1', 'L2'], ['L5', 'H1', 'L6'], ['L5', 'H4', 'L6']]
        ###################################### print(curr_list_r)
        ###################################### input("Press Enter....\n")




        #print(m[,slot_typeline_docker_v1]g_knife_list_r)Check the self.main_pd
        # Calculater RTP: input_two_important_agent    
            # - main_slot_bet_rate_agent
            # - optional_static_agent=static_agent_v1
        # 🎹, 🧪:  implement the version 2:  add pytest_data for checking the testing data coverage
        wrong_gain , sys_msg, _ , pytest_data_list , self.main_pd , tem_gain_two, tem_gain_thr, tem_gain_fou, tem_gain_fiv = self.rtp_agent.calculer_rtp_by_line_setting_v2_for_slot_3(self.total_run_cnt,curr_list_r, self.main_slot_bet_rate_agent,optional_static_agent=self.static_agent_v1,optional_pd=self.main_pd)
        self.output_agent.output_agent(sys_msg)






        #🙃🙃🙃🙃🙃🙃🙃    print("Check the self.main_pd")
        #🙃🙃🙃🙃🙃🙃🙃    print(self.main_pd)
        #🙃🙃🙃🙃🙃🙃🙃    input("Press Enter \n")

        #🙃🙃🙃🙃🙃🙃🙃  print("[devlopment]:  ",pytest_data_list)
        #🙃🙃🙃🙃🙃🙃🙃  input()


        # 🏦         v2.1 version: fix the bug: need to add S1 to be count (S1-3 : 3, S1-4:  10, S1-5: 100)
        # 🌟🌟🌟🌟: meet the pytest new version, so we need to add the extra S1-3, S1-4, S1-5 counts here. 

        # Basic checking
        assert obtenir_scater_cnts == 0 or obtenir_scater_cnts == 1 or obtenir_scater_cnts == 2 or obtenir_scater_cnts == 3 or obtenir_scater_cnts == 4 or obtenir_scater_cnts == 5

        tem_winning_data_dict = {}
        # 🌟: win, let's make the data. for test agent to test.
        # 🌟: v2_3 version, on extend S2 winning_line to S2_2 as well. :
        if obtenir_scater_cnts >= 2:           #if obtenir_scater_cnts >= 3:
            tem_winning_data_dict["win_obj"]        =   "S1"
            tem_winning_data_dict["win_line"]       =   obtenir_scater_cnts # S1-2, S1-3, S1-4, S1-5
            tem_winning_data_dict["win_list_r"]     =   copy.deepcopy(curr_list_r)
            tem_winning_data_dict["win_line_index"] =   1          # so S1 , the win_line_index =1
            

        if obtenir_scater_cnts == 2:
            wrong_gain += self.S1_2_pay_score
            self.S1_2_cnts += 1
            tem_winning_data_dict["win_gain"]   = self.S1_2_pay_score
            tem_winning_data_dict["win_bet_rate"] = self.S1_2_pay_score
            # 🌟: append the S1-2 case
            pytest_data_list.append(tem_winning_data_dict)

            tem_gain_two += self.S1_2_pay_score

        elif obtenir_scater_cnts == 3:
            wrong_gain += self.S1_3_pay_score 
            self.S1_3_cnts += 1 
            tem_winning_data_dict["win_gain" ]      =   self.S1_3_pay_score 
            tem_winning_data_dict["win_bet_rate"]   =   self.S1_3_pay_score 
            # 🌟: append the S1-3 case
            pytest_data_list.append(tem_winning_data_dict)

            tem_gain_thr += self.S1_3_pay_score

        elif obtenir_scater_cnts == 4:
            wrong_gain += self.S1_4_pay_score
            tem_winning_data_dict["win_gain" ]      =   self.S1_4_pay_score 
            tem_winning_data_dict["win_bet_rate"]   =   self.S1_4_pay_score 
            self.S1_4_cnts += 1 
            
            # 🌟: append the S1-4 case
            pytest_data_list.append(tem_winning_data_dict)

            tem_gain_fou += self.S1_4_pay_score

        elif  obtenir_scater_cnts == 5:
            wrong_gain += self.S1_5_pay_score    
            tem_winning_data_dict["win_gain" ]      =   self.S1_5_pay_score 
            tem_winning_data_dict["win_bet_rate"]   =   self.S1_5_pay_score 
            self.S1_5_cnts += 1   

            # 🌟: append the S1-5 case
            pytest_data_list.append(tem_winning_data_dict)

            tem_gain_fiv += self.S1_5_pay_score

        elif obtenir_scater_cnts == 0 or obtenir_scater_cnts == 1:
            pass
        else:
            print("Error , unexpected the S1 cnts  ",obtenir_scater_cnts)
            raise EnvironmentError


        # 🎁 🚩: check if enter free game or not !!!
        if obtenir_scater_cnts >=3:
            return_free_game_flag = 1 
        else:
            return_free_game_flag = 0



        # 💰💰💰💰💰💰💰 用分配的gain加總就沒錯了....
        curr_gain = tem_gain_two + tem_gain_thr + tem_gain_fou + tem_gain_fiv

        # 🎹, 🧪:
        """
          配搭的 data_dict  說明:
                tem_winning_data_dict = {}
                tem_winning_data_dict["win_obj"]        =   check_obj
                tem_winning_data_dict["win_line"]       =   current_line  # win_3, win_4, win_5 etc..
                tem_winning_data_dict["win_list_r"]     =   list_r
                tem_winning_data_dict["win_gain" ]      =   current_gain
                tem_winning_data_dict["win_line_index"] =   line_index           # 0,1,2,3,4,5 .... 19,   total: 20 lines for example.
                tem_winning_data_dict["win_bet_rate"]   =   bet_rate

                pytest_data_list.append(tem_winning_data_dict)
        """


        ##################print("Before the input_data_list")
        ##################print(pytest_data_list)
        ##################input("Press Enter\n")

        # 🎹, 🧪:
        if pytest_flag == True:

            # Checkt first time or secnod time
            if self.pytest_status == False:
                print("Create the test_agent ...")
                print(pytest_data_list)

                # # 🌟🌟🌟🌟: loading new version of ja_pytest libs to support S1, cheecking.
                try:
                    import package.ja_pytest_v2 as ja_pytest
                except:
                    import ja_pytest_v2 as ja_pytest

                self.ja_pytest_agent = ja_pytest.agent()

                # Set status to True. So that we don't need to initial agent again.
                self.pytest_status = True


                # 🎹, 🧪: test with 3 steps.
                for any_data_dict in pytest_data_list:
                    test_obj        = any_data_dict["win_obj"]
                    test_bet_rate   = any_data_dict["win_bet_rate"]
                    test_win_line       = any_data_dict["win_line"]
                    test_line_index = any_data_dict["win_line_index"]   # mappng win_line_index -> line_index ( 1~20 , 0~19)
                    test_list_r         = copy.deepcopy(any_data_dict["win_list_r"])
                    test_gain           = any_data_dict["win_gain"]

                    if self.ja_pytest_agent.step_1_test_bet_amount(test_bet_rate,test_obj,test_win_line):
                        pass
                    else:
                        print("[d_main_respin_v2]: Error when checking step_1_test_bet_amount")
                        input()
                    
                    if self.ja_pytest_agent.step_2_test_line_index(test_line_index,test_obj,test_win_line,test_list_r):
                        pass
                    else:
                        print("[d_main_respin_v2]: Error when checking step_2_test_line_index")
                        input()

                    if self.ja_pytest_agent.step_3_test_win_line_20_gain_v1(test_gain,test_obj,test_win_line,test_line_index):
                        pass
                    else:
                        print("[d_main_respin_v2]: Error when checking step_3_test_win_line_20_gain_v1")
                        input()
                


            else:
                print("Do the test_agent ...")
                print(pytest_data_list)
                # 🎹, 🧪: test with 3 steps.
                for any_data_dict in pytest_data_list:
                    test_obj        = any_data_dict["win_obj"]
                    test_bet_rate   = any_data_dict["win_bet_rate"]
                    test_win_line       = any_data_dict["win_line"]
                    test_line_index = any_data_dict["win_line_index"]   # mappng win_line_index -> line_index ( 1~20 , 0~19)
                    test_list_r         = copy.deepcopy(any_data_dict["win_list_r"])
                    test_gain           = any_data_dict["win_gain"]

                    if self.ja_pytest_agent.step_1_test_bet_amount(test_bet_rate,test_obj,test_win_line):
                        pass
                    else:
                        print("[d_main_respin_v2]: Error when checking step_1_test_bet_amount")
                        input()
                    
                    if self.ja_pytest_agent.step_2_test_line_index(test_line_index,test_obj,test_win_line,test_list_r):
                        pass
                    else:
                        print("[d_main_respin_v2]: Error when checking step_2_test_line_index")
                        input()

                    if self.ja_pytest_agent.step_3_test_win_line_20_gain_v1(test_gain,test_obj,test_win_line,test_line_index):
                        pass
                    else:
                        print("[d_main_respin_v2]: Error when checking step_3_test_win_line_20_gain_v1")
                        input()

                    
                    ## 👨‍⚕️: Check h2_2_rtp (skip the first run , shall be fine to get the statics..)

                    if test_obj == "H1" and test_win_line == 2:
                        self.h2_2_rtp += test_gain 
                        print("[Doctor][h2_2_rtp]:       curr_gain  =    %.4f      ,  total_gain  =    %.4f     with rtp-portion    =   %.4f"%(test_gain,self.h2_2_rtp,float(self.h2_2_rtp/self.total_run_cnt)))


        # [Mary Debug]
        # print("[,slot_typeline_docker_v1]############ %d run ###############"%each_run)
        # print("[,slot_typeline_docker_v1]curr_list_r    =    ",curr_list_r)
        # print("[,slot_typeline_docker_v1]hit_symbol     =    ",curr_list_r)
        # print("[,slot_typeline_docker_v1]changed_r      =    ",mg_knife_list_r)
        # print("[,slot_typeline_docker_v1]\n\n")
        # print(m[,slot_typeline_docker_v1]sg)
        # print("[,slot_typeline_docker_v1]-------")
        # print(s[,slot_typeline_docker_v1]ys_msg)
        # read_nothing = input("Enter Key....")

        self.total_gain            += curr_gain
        self.curr_rtp               = self.total_gain / self.total_run_cnt
        self.X2                    += curr_gain ** 2
        if curr_gain > 0:
            self.hit_cnts += 1
            self.win_rate  = float(self.hit_cnts/self.total_run_cnt)


        
        # Display progress
        if self.total_run_cnt % 2000 == 1 and self.total_run_cnt > 3000:
            divided_cnts = self.total_run_cnt * len(self.mg_line_setting_list)
            print("[,slot_typeline_docker_v1]running %d , current_information: \n\n%s\n\n"%(self.total_run_cnt,self.static_agent_v1.show_probability_by_input_cnts(divided_cnts)))
            print("[,slot_typeline_docker_v1]\n-----\n")
            print(self.main_pd)
            print("[,slot_typeline_docker_v1]\n-----\n")
            self.__see_rtp_from_pd(self.main_pd)
            print("[,slot_typeline_docker_v1]\n----\n") 
            self.__see_each_smbol_distribution(divided_cnts ,self.main_pd)

            ## [Jean]:  On vois la variance et standard vadiation ici
            ##          
            print("[,slot_typeline_docker_v1][Jean][In-Progess]: On besoin de faire variance et standard into pickle apres ")


            self.curr_variance =  float(self.X2/self.total_run_cnt) - float(self.curr_rtp**2)
            print("[,slot_typeline_docker_v1]\n------------------------[slot_typeline_docker_v1]-------------------------\n")
            print("[,slot_typeline_docker_v1]Current RTP <X>      est                 %.6f"%self.curr_rtp)
            print("[,slot_typeline_docker_v1]Current <X2>         est                 %.6f"%(self.X2/self.total_run_cnt))
            print("[,slot_typeline_docker_v1]Current Variance     est                 %.6f"%self.curr_variance)
            print("[,slot_typeline_docker_v1]Standard deviation   est                 %.6f"%math.sqrt(self.curr_variance))
            print("[,slot_typeline_docker_v1]Winning Rate         est                 %.6f"%self.win_rate)
            print("[,slot_typeline_docker_v1]\n--------------------------------------------------------\n")
        


            # 🏦: version 2.1
            print("self.S1_2_cnts  =     %8d     with ratio    %.4f   "%(self.S1_2_cnts,float(self.S1_2_cnts/self.total_run_cnt)))
            print("self.S1_3_cnts  =     %8d     with ratio    %.4f   "%(self.S1_3_cnts,float(self.S1_3_cnts/self.total_run_cnt)))
            print("self.S1_4_cnts  =     %8d     with ratio    %.4f   "%(self.S1_4_cnts,float(self.S1_4_cnts/self.total_run_cnt)))
            print("self.S1_5_cnts  =     %8d     with ratio    %.4f   "%(self.S1_5_cnts,float(self.S1_5_cnts/self.total_run_cnt)))
           


            # 🦉 Note
            print("[,slot_typeline_docker_v1]📊 Game Way 🛣  has funciton: def __see_each_smbol_distribution_v1(divided_cnts,my_pd): \n\
                     implement this to __see___line_v1()   later \n\
                     🦜 ......")

            # 🧪: display pytesg cased corrage with % format.
            if self.pytest_status == True:
                self.ja_pytest_agent.show_test_cases_coverage()


        # 🖌
        self.rtp_list.append(self.curr_rtp)    
        self.run_id_list.append(self.total_run_cnt)    


        #  Return
        return_curr_list_r = copy.deepcopy(curr_list_r)

        # 🎁
        return curr_gain, return_curr_list_r, self.main_pd , return_free_game_flag, tem_gain_two, tem_gain_thr, tem_gain_fou, tem_gain_fiv




    def end(self):
        #############################################################################################################################

        # 💹 Write the summar to static_excel, save your fucking time.
        # Basic version first. 
        # 🦜 Implement the SA_3, SA_4 cnts by new dataframe -> excel by next Monday.

        #import package.ja_static_write_rtp_info as ja_static_rtp 

        reel_list_col_1 = self.mg_roll_r1_list
        reel_list_col_2 = self.mg_roll_r2_list
        reel_list_col_3 = self.mg_roll_r3_list
        reel_list_col_4 = self.mg_roll_r4_list
        reel_list_col_5 = self.mg_roll_r5_list

        pay_objs = self.setting_linable_obj_list
        pay_bets = self.setting_bet_rate_list_list


        # 🐼
        symbol_win_dict, _pd = ja_symbol_distribution.run_line(self.setting_linable_obj_list,[3,4,5],self.main_pd)

        # 🐳 write_5X3_line
        ja_static_rtp.write_5X3_line("./docker_vol/%s.xlsx"%self.static_filename,self.total_run_cnt,self.curr_rtp,self.curr_variance,math.sqrt(self.curr_variance),self.win_rate,\
               reel_list_col_1,reel_list_col_2,reel_list_col_3,reel_list_col_4,reel_list_col_5,\
               pay_objs,pay_bets,\
                symbol_win_dict, self.setting_line_number ) # 🎲 


            
        # Final
        divided_cnts = self.total_run_cnt * len(self.mg_line_setting_list)
        print("[,slot_typeline_docker_v1]running %d , current_information: \n\n%s\n\n"%(self.total_run_cnt,self.static_agent_v1.show_probability_by_input_cnts(divided_cnts)))
        print("[,slot_typeline_docker_v1]\n-----\n")
        print(self.main_pd)
        print("[,slot_typeline_docker_v1]\n-----\n")
        self.__see_rtp_from_pd(self.main_pd)
        print("[,slot_typeline_docker_v1]\n----\n") 
        self.__see_each_smbol_distribution(divided_cnts ,self.main_pd)
        
        ## [Jean]:  On vois la variance et standard vadiation ici
        ##          
        print("[,slot_typeline_docker_v1][Jean][In-Progess]: On besoin de faire variance et standard into pickle apres ")


        self.curr_variance =  float(self.X2/self.total_run_cnt) - float(self.curr_rtp**2)
        print("[,slot_typeline_docker_v1]\n------------------------[slot_typeline_docker_v1]-------------------------\n")
        print("[,slot_typeline_docker_v1]Current RTP <X>      est                 %.6f"%self.curr_rtp)
        print("[,slot_typeline_docker_v1]Current <X2>         est                 %.6f"%(self.X2/self.total_run_cnt))
        print("[,slot_typeline_docker_v1]Current Variance     est                 %.6f"%self.curr_variance)
        print("[,slot_typeline_docker_v1]Standard deviation   est                 %.6f"%math.sqrt(self.curr_variance))
        print("[,slot_typeline_docker_v1]Winning Rate         est                 %.6f"%self.win_rate)
        print("[,slot_typeline_docker_v1]\n--------------------------------------------------------\n")
    
        # 🦉 Note
        print("[,slot_typeline_docker_v1]📊 Game Way 🛣  has funciton: def __see_each_smbol_distribution_v1(divided_cnts,my_pd): \n\
                 implement this to __see___line_v1()   later \n\
                 🦜 ......")


        # 🐳 🐼 📊
        ja_write_pkl.run(self.static_filename,self.main_pd)

        # 🐳 🐼 🖌
        rtp_df = pd.DataFrame(list(zip(self.rtp_list,self.run_id_list)),columns=['RTP',"Run_ID"])
        ja_write_pkl.run("%s_rtp_data"%self.rtp_name,rtp_df)

        
        # 🐳 🖌, save to docker_vol
        fig, ax = plt.subplots()
        ax.plot(self.run_id_list,self.rtp_list,'g',label=self.rtp_name)
        legend = ax.legend(loc='upper center',shadow=True,fontsize='x-large')
        legend.get_frame().set_facecolor('C0')
        plt.savefig('./docker_vol/%s.png'%self.rtp_name)
        plt.show()



if __name__ == "__main__":

    # 📮 🕸 :
    print("[🕸]:  Please set the port...  e.g. 80 or 7691")
    input_port = int(input())

    # 📮 🕸:
    print("[🕸]:  Please set host_name: for 📠: 'localhost',  \n🐳: docker_internal: 10.10.20.33")
    input_ip_name = input()



    # 🔱 🔱
    print("🔱 : how many runs for takeing one sample: e.g.  5000 or 1000")
    acutary_sample_nb = int(input())   


    # 🔱 🔱
    print("🔱 : please input the excelname  e.g. job_card_01_mg_case_1.xlsx  ,   docker_vol/job_card_01_mg_case_1.xlsx")
    actuary_job_card_name = input()

    # 🔱 🔱
    print("🔱 : please input the fg_times  因為是main_game: please set to 1 ")
    actuary_fg_times = int(input())   

    
    # 🔱 🔱
    print("🔱 : please set the pytes flag, if you are running docker, i suggest you to turn on..   e.g. False , True")
    tem_convered_integer = distutils.util.strtobool(input())
    actuary_pytest = bool(tem_convered_integer)


    # 🔱 🔱
    print("🔱 : please set the runs  e.g.  2000000")
    actuary_set_runs = int(input())


    # 🔱 🔱
    print("🔱 : please tag the pkl file  e.g.  jp_fg_hero_01 , ct_mg_01 etc.. ")
    actuary_tag_pkl = input()


    # loading agent
    set_fg_times = actuary_fg_times   #  set_fg_times = 1 to meet main_game la 
    set_pytest   = actuary_pytest     #  set_pytest   = False              
    test_agent = agent(default_excelname=actuary_job_card_name) 


    """
     unit-test:  簡單算單張卡 rtp.
    """
    rtp = 0
    total_gain = 0.000000000000001



    # 🔱: Initial cnts
    actuary_run_cnt = 0
    actuary_tem_rtp = 0.0
    actuary_id = 0 
    actuary_rtp_list = []
    actuary_id_list = []


    actuary_gain_two = 0.0
    actuary_gain_thr = 0.0
    actuary_gain_fou = 0.0
    actuary_gain_fiv = 0.0   
    

    # 🔱: run by input_parameter
    for index in range(actuary_set_runs):

        # 🔱:
        actuary_run_cnt += 1


        current_id = index + 1

        if set_pytest == True:
            curr_gain, curr_list_r, _tem_pd, _enter_fg_flag , tem_gain_two, tem_gain_thr, tem_gain_fou, tem_gain_fiv  = test_agent.run(pytest_flag=True)

        else:
            curr_gain, curr_list_r, _tem_pd , _enter_fg_flag , tem_gain_two, tem_gain_thr, tem_gain_fou, tem_gain_fiv = test_agent.run()

        # 💰
        total_gain += curr_gain 

        actuary_gain_two += tem_gain_two 
        actuary_gain_thr += tem_gain_thr 
        actuary_gain_fou += tem_gain_fou
        actuary_gain_fiv += tem_gain_fiv



        print("%5d:     "%current_id,"  ", "curr_gain:  %.4f  "%curr_gain,   "total gain: %.4f  "%total_gain,  "curr_rtp:  %.4f"%(total_gain/current_id))
        print("(2,3,4,5):        %.4f  "%(actuary_gain_two  / current_id))
        print("(2,3,4,5):        %.4f  "%(actuary_gain_thr  / current_id))
        print("(2,3,4,5):        %.4f  "%(actuary_gain_fou  / current_id))
        print("(2,3,4,5):        %.4f  "%(actuary_gain_fiv  / current_id))
        




        # 💰
        rtp = total_gain / current_id

        # 🔱: 💰
        actuary_tem_rtp += curr_gain


        # 🔱: collect data for one sample
        if actuary_run_cnt == acutary_sample_nb:   
            # 🔱: add rtp
            actuary_tem_rtp = float(actuary_tem_rtp / acutary_sample_nb)
            actuary_rtp_list.append(actuary_tem_rtp)

            # 📮 🕸 : sendint the rtp_samples to kubectl rtp_server pod
            data_pack = {"value": actuary_tem_rtp}

            # 📮 🕸 :  Send
            resp = requests.post('http://%s:%d/actuary/api/v1.0/rtps'%(input_ip_name,input_port),json=data_pack)

            # 📮 🕸 :  Check if the response is 201
            if resp.status_code != 201:
                print("[📮 🕸]Warning:APIError POST /rtps with code:  ",resp.status_code) 

            print("[📮 🕸 : ]Created rtp value, return rtp:  ",resp.json()['rtp'])
            

            # 🔱: add id
            actuary_id += 1
            actuary_id_list.append(actuary_id)

            # 🔱: reset 
            actuary_tem_rtp = 0.0
            actuary_run_cnt = 0

            # 🔱: keep save into docker_vol/xxxxx.pkl
            rtp_df = pd.DataFrame(list(zip(actuary_rtp_list,actuary_id_list)),columns=['RTP',"Sample_ID"])
            ja_write_pkl.run("actuary_v1_%s_rtp_take_%d_runs_into_one_sample"%(actuary_tag_pkl,acutary_sample_nb),\
                              rtp_df)

        # Afficher         
        base_frequency = math.floor(1000/set_fg_times)
        if index > base_frequency and index %(base_frequency*2) == 1:
            print("===========================================")
            print("keyword rtp =  %.4f"%rtp)
            print("===========================================")


            # 🧪: display pytesg cased corrage with % format.
            if set_pytest == True:
                test_agent.ja_pytest_agent.show_test_cases_coverage()


    test_agent.end()

