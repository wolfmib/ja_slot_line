"""
v2 version: 
    - support S1, E1, H1, W1 etc.. format
    - support output package print out
    - add pytest_flag in run(self, pytest_flag=False).  This will initial the test_agent tand start test.


# 🏦  v2.1 version: fix the bug: need to add S1 to be count (S1-3 : 3, S1-4:  10, S1-5: 100)
#     v2.2     actuary: with main_game.agent  et free_game.agent
#     v2.2.1   add std. variance , winning rate,  free-game-enter rate printing.
# 

   要改說明拉 幹

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
    import package.jackpot_analyzer_slot_v2_1 as ana_slot
except:
    import jackpot_analyzer_slot_v2_1 as ana_slot
    

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



# main_game
try:
    import package.Actuary_d_mainv2_2 as main_game

except:
    import Actuary_d_mainv2_2 as main_game


# free_game
# 張菲 後裔 李白
# 🕵🏻‍♂️🕵🏻‍♂️ 🏹🏹  🍺🍺
# 🕵🏻‍♂️🕵🏻‍♂️ 🏹🏹  🍺🍺
try:
    import package.Actuary_d_free_v2_2 as free_game
except:
    import Actuary_d_free_v2_2 as free_game





if __name__ == "__main__":



    # 🔱 🔱
    print("🔱 : please input the main excelname  e.g. job_card_01_mg_case_2.xlsx  ,   docker_vol/job_card_01_mg_case_2.xlsx")
    actuary_job_card_main_name = input()

    # 🔱 🔱
    print("🔱 : please input the free excelname  e.g. job_card_01_fg_case_4.xlsx  ,   docker_vol/job_card_01_fg_case_4.xlsx")
    actuary_job_card_free_name = input()

    # 🔱 🔱
    print("🔱 : please input the fg_times slot-04: please set to 14 ")
    actuary_fg_times = int(input())   

    
    # 🔱 🔱
    print("🔱 : please set the pytes flag, if you are running docker, i suggest you to turn on..   e.g. False , True")
    tem_convered_integer = distutils.util.strtobool(input())
    actuary_pytest = bool(tem_convered_integer)


    # 🔱 🔱
    print("🔱 : please set the runs  e.g.  2000000")
    actuary_set_runs = int(input())



    # loading agent
    set_fg_times = actuary_fg_times   #  set_fg_times = 14
    set_pytest   = actuary_pytest     #  set_pytest   = False              
    main_agent = main_game.agent(default_excelname=actuary_job_card_main_name) 
    free_agent = free_game.agent(default_excelname=actuary_job_card_free_name)


    """
     unit-test:  簡單算單張卡 rtp.
    """
    rtp = 0
    total_gain      = 0.000000000000001
    X2              = 0.000000000000001
    win_cnt         = 0.000000000000001
 



    # Prepare
    base_frequency = math.floor(1000/set_fg_times)
    actuary_enter_free_game_cnts = 0

    # 🔱: run by input_parameter
    for index in range(actuary_set_runs):


        current_id = index + 1

        if set_pytest == True:
            # 💰
            curr_gain, curr_list_r, _tem_pd, enter_free_game = main_agent.run(pytest_flag=True)

        else:
            # 💰
            curr_gain, curr_list_r, _tem_pd , enter_free_game = main_agent.run()



        # 🎁 🚩
        curr_total_fg_gain = 0.0
        if enter_free_game == 1:
            actuary_enter_free_game_cnts += 1
            print("                              [🎁 🚩][%4d] Enter Free Game Cnts [%4d]"%(index,actuary_enter_free_game_cnts))

            
            # range(1,15) -> 1,2,3,.....14
            for fg_run_index in range(1,actuary_fg_times+1):
                # 💰 : one run free_gain , with respin_gain = 0.0  or other values , if enter-respin-mode. 
                curr_single_fg_gain, _curr_list_r, _tem_pd, curr_respin_gain =  free_agent.run(pytest_flag=False)
                
                # 💰
                curr_total_fg_gain += curr_single_fg_gain # This variable  already includes , fg_gain + respin_gain.


        # 💰: main_et_free_gain
        curr_gain += curr_total_fg_gain # combine curr_gain(main) + curr_total_fg_gain (free_game)
        total_gain += curr_gain 

        # Afficher         
        if index > base_frequency and index %(base_frequency*2) == 1:
            # 💰: rtp
            rtp = total_gain / current_id


            print("====================%2d====================="%index)
            print("keyword rtp =  %.4f"%rtp)
            print("===========================================")


            # 🧪: display pytesg cased corrage with % format.
            if set_pytest == True:
                main_agent.ja_pytest_agent.show_test_cases_coverage()



    main_agent.end()

