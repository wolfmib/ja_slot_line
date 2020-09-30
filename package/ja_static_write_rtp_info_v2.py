## Write static information to excel

import xlrd
import xlwt







def _write_value_to_sheet(sheet,col_index,row_index,value):
    
    sheet.write(row_index,col_index,value)
    


def write_5X3_line(input_name,i_total_runs,i_rtp,i_variance,i_std,i_hit_rate,\
          reel_list_1,reel_list_2,reel_list_3,reel_list_4,reel_list_5,\
          pay_lineable_objs_list, pay_bet_rate_list_list,\
          line_dict,line_number):


  
    
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("M %")

    """
    RTP           0.95
    Variance       4
    Std            2
    hr            0.32
    """

    _write_value_to_sheet(sheet,0,0,"Running Counts")
    _write_value_to_sheet(sheet,1,0,i_total_runs)


    _write_value_to_sheet(sheet,0,1,"M %")
    _write_value_to_sheet(sheet,1,1,i_rtp)



    _write_value_to_sheet(sheet,0,2,"Variance")
    _write_value_to_sheet(sheet,1,2,i_variance)

    _write_value_to_sheet(sheet,0,3,"Std.")
    _write_value_to_sheet(sheet,1,3,i_std)

    _write_value_to_sheet(sheet,0,4,"Hit Rate")
    _write_value_to_sheet(sheet,1,4,i_hit_rate)
    """
    ---------------------------------------------------------------------------
    """


    """ Reel Output Format
    R1 R2 R3 R4 R5
    Q  Q   A  J W
    Q  Q   J  ...
    .......

    """

    """ Input Program Format
        ['SC', 'K', 'SA', 'Q', 'SC', 'SC', 'Q', 'SA', 'Q', 'J', 'SA', 'K', 'SC', 'SC', 'K', 'SC', 'SA', 'SC', 'K', 'SA', 'SA', 'SA', 'Q', 'K', 'SC', 'SA', 'SA', 'Q', 'SB', 'J', 'SA', 'J', 'SA', 'J', 'K', 'Q', 'SA', 'SE', 'SC', 'Q', 'K', 'Q', 'SA', 'SA', 'SB', 'SC', 'SS', 'K', 'SD', 'K', 'J', 'SA', 'SC', 'K', 'Q', 'SA', 'J', 'SB', 'J', 'K', 'SA', 'J', 'SC', 'J', 'SB', 'SC', 'Q', 'J', 'Q', 'SC', 'J', 'SA', 'K', 'K', 'SA', 'K', 'SA', 'K', 'A', 'K', 'SA', 'SA', 'K', 'SA', 'A', 'Q', 'A', 'SA', 'SC', 'A', 'SE', 'Q', 'J', 'SA', 'J', 'SB', 'A', 'A', 'J', 'SB', 'A', 'A', 'SC', 'SD', 'SA', 'A', 'K', 'SS', 'K', 'A', 'Q', 'A', 'SB', 'A', 'SC', 'SS', 'SA', 'K', 'SA', 'SA', 'Q', 'SC', 'J', 'SC', 'K', 'Q', 'SA', 'K', 'SB', 'K', 'SA']
        ['Q', 'K', 'J', 'J', 'Q', 'J', 'Q', 'SA', 'J', 'A', 'J', 'SS', 'Q', 'SC', 'Q', 'A', 'SB', 'J', 'SS', 'Q', 'SB', 'SB', 'J', 'SB', 'J', 'W', 'SB', 'SB', 'J', 'SS', 'A', 'Q', 'SD', 'Q', 'A', 'Q', 'SB', 'Q', 'Q', 'SE', 'A', 'A', 'Q', 'A', 'A', 'Q', 'SE', 'SD', 'K', 'A', 'SC', 'SB', 'Q', 'SE', 'A', 'Q', 'J', 'A', 'W', 'SB', 'J', 'A', 'A', 'J', 'J', 'J', 'A', 'SS', 'J', 'Q', 'J', 'Q', 'SC', 'SB', 'Q', 'SB', 'J', 'SB', 'Q', 'J', 'A', 'J', 'SB', 'SD', 'J', 'Q', 'SB', 'J', 'A', 'SB', 'SA', 'Q', 'J', 'J', 'Q', 'SC', 'SA', 'SC', 'Q', 'J', 'SA', 'K', 'Q', 'Q', 'Q', 'SB', 'SB', 'SD', 'J', 'Q', 'J', 'J', 'Q', 'SB', 'Q', 'SE', 'SS', 'SB', 'J', 'J', 'SE', 'SA', 'J', 'SD', 'J', 'J', 'J', 'Q', 'J']
        ['SD', 'A', 'K', 'SD', 'K', 'K', 'J', 'A', 'SD', 'A', 'SE', 'A', 'J', 'SD', 'Q', 'SD', 'SE', 'SE', 'Q', 'J', 'A', 'A', 'SD', 'SB', 'SE', 'A', 'SA', 'J', 'SS', 'SC', 'SD', 'SE', 'A', 'SS', 'Q', 'SE', 'A', 'SB', 'SE', 'SE', 'A', 'SA', 'Q', 'Q', 'J', 'Q', 'K', 'K', 'A', 'J', 'A', 'J', 'J', 'J', 'SD', 'A', 'Q', 'K', 'A', 'Q', 'Q', 'J', 'K', 'SS', 'A', 'K', 'Q', 'K', 'J', 'K', 'Q', 'SD', 'SE', 'SD', 'SA', 'A', 'A', 'Q', 'K', 'SC', 'K', 'W', 'SE', 'K', 'SE', 'J', 'SE', 'A', 'SE', 'K', 'A', 'K', 'SD', 'K', 'SC', 'K', 'A', 'SE', 'A', 'SD', 'A', 'Q', 'Q', 'K', 'A', 'K', 'A', 'A', 'SA', 'J', 'J', 'SD', 'SD', 'W', 'SB', 'K', 'A', 'K', 'A', 'K', 'SB', 'SA', 'K', 'SS', 'K', 'K', 'A', 'A', 'SS', 'Q', 'SC', 'SE', 'K', 'SE', 'SC', 'K', 'SD', 'A', 'K', 'SB', 'A', 'SD', 'K', 'K', 'SE', 'J', 'SD', 'Q', 'J']
        ['K', 'J', 'SC', 'J', 'SC', 'SC', 'SB', 'SA', 'SE', 'SA', 'Q', 'J', 'SC', 'J', 'J', 'K', 'Q', 'SE', 'Q', 'SS', 'K', 'J', 'SS', 'J', 'Q', 'SS', 'SE', 'A', 'J', 'J', 'SB', 'Q', 'A', 'SD', 'SA', 'SD', 'SA', 'K', 'SA', 'J', 'SB', 'A', 'SA', 'SC', 'SB', 'K', 'A', 'SB', 'A', 'SB', 'SB', 'J', 'A', 'K', 'J', 'W', 'K', 'A', 'J', 'Q', 'SB', 'J', 'SB', 'J', 'SD', 'SC', 'K', 'SA', 'SB', 'K', 'Q', 'A', 'J', 'SS', 'J', 'SB', 'Q', 'SC', 'K', 'A', 'SA', 'Q', 'SC', 'K', 'K', 'Q', 'SC', 'SA', 'SC', 'Q', 'SA', 'SB', 'A', 'J', 'SC', 'SS', 'SA', 'Q', 'SA', 'SE', 'SB', 'K', 'A', 'Q', 'A', 'A', 'SB', 'SD', 'A', 'J', 'SD', 'Q', 'Q', 'SA', 'Q', 'SC', 'W', 'Q', 'J', 'SC', 'Q', 'SA', 'Q', 'Q', 'SA', 'A', 'Q', 'J', 'W', 'SC', 'SC', 'SE', 'A', 'A', 'SB', 'K', 'K', 'K', 'K']
        ['W', 'SA', 'Q', 'SB', 'SE', 'K', 'SD', 'SC', 'SS', 'K', 'SC', 'SE', 'SD', 'SA', 'Q', 'Q', 'SD', 'A', 'J', 'SE', 'J', 'K', 'K', 'SE', 'SA', 'A', 'K', 'K', 'SD', 'W', 'A', 'SD', 'Q', 'A', 'Q', 'SC', 'SA', 'SA', 'SB', 'SS', 'A', 'Q', 'A', 'K', 'SD', 'SC', 'K', 'A', 'SS', 'Q', 'SE', 'SB', 'SA', 'J', 'Q', 'SC', 'SE', 'SA', 'J', 'K', 'Q', 'A', 'SD', 'K', 'SB', 'SE', 'SB', 'SC', 'SB', 'SD', 'SC', 'SS', 'SE', 'SA', 'W', 'A', 'A', 'K', 'SA', 'A', 'A', 'SC', 'W', 'K', 'K', 'Q', 'SA', 'J', 'SS', 'Q', 'SB', 'A', 'K', 'J', 'SB', 'SC', 'J', 'A', 'SB', 'K', 'K', 'A', 'J', 'SE', 'SE', 'SC', 'SE', 'A', 'SA', 'J', 'SC', 'Q', 'J', 'SC', 'Q', 'A', 'W', 'SB', 'SD', 'SD', 'SD', 'K', 'SE', 'SB', 'J', 'SA', 'Q', 'J', 'SB', 'SA', 'SB', 'W', 'J', 'W', 'SC', 'SD', 'J']
    
    """



    reel_sheet = workbook.add_sheet("Reel")
    _write_value_to_sheet(reel_sheet,0,0,"R1: ")
    _write_value_to_sheet(reel_sheet,1,0,"R2: ")
    _write_value_to_sheet(reel_sheet,2,0,"R3: ")
    _write_value_to_sheet(reel_sheet,3,0,"R4: ")
    _write_value_to_sheet(reel_sheet,4,0,"R5: ")
    for index, any_symbol in enumerate(reel_list_1):
        # col 0 : R1
        _write_value_to_sheet(reel_sheet,0,index+1,any_symbol)
    for index, any_symbol in enumerate(reel_list_2):
        # col 1 : R2
        _write_value_to_sheet(reel_sheet,1,index+1,any_symbol)
    for index, any_symbol in enumerate(reel_list_3):
        # col 2 : R3
        _write_value_to_sheet(reel_sheet,2,index+1,any_symbol)
    for index, any_symbol in enumerate(reel_list_4):
        # col 3 : R4
        _write_value_to_sheet(reel_sheet,3,index+1,any_symbol)
    for index, any_symbol in enumerate(reel_list_5):
        # col 4 : R5
        _write_value_to_sheet(reel_sheet,4,index+1,any_symbol)




    """ Paytable

    output:   v1 , v2 , v3, v4 , v5 
         SA   0    0    0.6  2.5 10.0
         SB   .......................
         .
         .


    Input:
        💹 Check lineable objs ... 
            ['SA', 'SB', 'SC', 'SD', 'SE', 'A', 'K', 'Q', 'J', 'SS']
            -----------------------
        💹 Check setting_bet_rate_list_list  ... t
            [[0.0, 0.0, 0.6, 2.5, 10.0], [0.0, 0.0, 0.4, 2.0, 5.0], [0.0, 0.0, 0.4, 1.6, 4.0], [0.0, 0.0, 0.3, 1.5, 3.5], [0.0, 0.0, 0.3, 1.2, 3.0], [0.0, 0.0, 0.2, 0.6, 2.5], [0.0, 0.0, 0.16, 0.5, 2.4], [0.0, 0.0, 0.1, 0.4, 2.0], [0.0, 0.0, 0.04, 0.3, 1.6], [0.0, 0.0, 5.0, 50.0, 250.0]]
    """

    pay_table_sheet = workbook.add_sheet("PayTable")
    # Write Objs
    for index, any_obj in enumerate(pay_lineable_objs_list):
        _write_value_to_sheet(pay_table_sheet,0,index+1,any_obj)

    # Write Bet_Rate
    for obj_index , bet_rate_list in enumerate(pay_bet_rate_list_list):
        for index, value in enumerate(bet_rate_list):
            _write_value_to_sheet(pay_table_sheet,index+1,obj_index+1,float(value))
    



    """ Win_Obj_Distribution
    
    

    output:   3      4       5
      SA     0.2     0.1    0.01
      SB     0.01    0.5    0.05


    """

    

    win_obj_distribution_sheet = workbook.add_sheet("Win_Obj_Distribution")
    # Write Objs
    for index , any_obj in enumerate(pay_lineable_objs_list):
        _write_value_to_sheet(win_obj_distribution_sheet,0,index+1,any_obj)

    # Write 3, 4 , 5 win_distribuiton_pro.
    for any_win_index, any_win in enumerate([3,4,5]):
        # Map to Sheet_Col_Index:    3(index0), 4(index1), 5(index2) est dans la col(1,2,3)
        any_win_col = any_win_index + 1

        # 💹  Write title  3, 4, 5 dans la row_0
        _write_value_to_sheet(win_obj_distribution_sheet,any_win_col,0,any_win)

        for any_obj_index, any_obj in enumerate(pay_lineable_objs_list):
            # Map to sheet index
            any_obj_col = any_obj_index + 1



            # Obtenir value dans la dict et calculate the prob. 
            try:
                value = line_dict[any_win][any_obj]    # obtenir cnts
                value_pbob = float(value/(line_number*i_total_runs)) 
            except:
                value_pbob = "None"

            # Write to sheet
            _write_value_to_sheet(win_obj_distribution_sheet,any_win_col,any_obj_col,value_pbob)


    print("[💹]: ---------------------------------------------")
    print("[💹]: Generated Files:   ",input_name)
    print("[💹]: Support Line: 5x3")
    print("[💹]: Calculate Win_Obj by divided %2d lines"%line_number)
    print("[💹]: ---------------------------------------------")

    # Save
    workbook.save(input_name)
    





"""
Used to calculate each table's M% or RTP

"""

if __name__ == "__main__":


    reel_list_col_1 = ['SC', 'K', 'SA', 'Q', 'SC', 'SC', 'Q', 'SA', 'Q', 'J', 'SA', 'K', 'SC', 'SC', 'K', 'SC', 'SA', 'SC', 'K', 'SA', 'SA', 'SA', 'Q', 'K', 'SC', 'SA', 'SA', 'Q', 'SB', 'J', 'SA', 'J', 'SA', 'J', 'K', 'Q', 'SA', 'SE', 'SC', 'Q', 'K', 'Q', 'SA', 'SA', 'SB', 'SC', 'SS', 'K', 'SD', 'K', 'J', 'SA', 'SC', 'K', 'Q', 'SA', 'J', 'SB', 'J', 'K', 'SA', 'J', 'SC', 'J', 'SB', 'SC', 'Q', 'J', 'Q', 'SC', 'J', 'SA', 'K', 'K', 'SA', 'K', 'SA', 'K', 'A', 'K', 'SA', 'SA', 'K', 'SA', 'A', 'Q', 'A', 'SA', 'SC', 'A', 'SE', 'Q', 'J', 'SA', 'J', 'SB', 'A', 'A', 'J', 'SB', 'A', 'A', 'SC', 'SD', 'SA', 'A', 'K', 'SS', 'K', 'A', 'Q', 'A', 'SB', 'A', 'SC', 'SS', 'SA', 'K', 'SA', 'SA', 'Q', 'SC', 'J', 'SC', 'K', 'Q', 'SA', 'K', 'SB', 'K', 'SA']
    reel_list_col_2 = ['Q', 'K', 'J', 'J', 'Q', 'J', 'Q', 'SA', 'J', 'A', 'J', 'SS', 'Q', 'SC', 'Q', 'A', 'SB', 'J', 'SS', 'Q', 'SB', 'SB', 'J', 'SB', 'J', 'W', 'SB', 'SB', 'J', 'SS', 'A', 'Q', 'SD', 'Q', 'A', 'Q', 'SB', 'Q', 'Q', 'SE', 'A', 'A', 'Q', 'A', 'A', 'Q', 'SE', 'SD', 'K', 'A', 'SC', 'SB', 'Q', 'SE', 'A', 'Q', 'J', 'A', 'W', 'SB', 'J', 'A', 'A', 'J', 'J', 'J', 'A', 'SS', 'J', 'Q', 'J', 'Q', 'SC', 'SB', 'Q', 'SB', 'J', 'SB', 'Q', 'J', 'A', 'J', 'SB', 'SD', 'J', 'Q', 'SB', 'J', 'A', 'SB', 'SA', 'Q', 'J', 'J', 'Q', 'SC', 'SA', 'SC', 'Q', 'J', 'SA', 'K', 'Q', 'Q', 'Q', 'SB', 'SB', 'SD', 'J', 'Q', 'J', 'J', 'Q', 'SB', 'Q', 'SE', 'SS', 'SB', 'J', 'J', 'SE', 'SA', 'J', 'SD', 'J', 'J', 'J', 'Q', 'J']
    reel_list_col_3 = ['SD', 'A', 'K', 'SD', 'K', 'K', 'J', 'A', 'SD', 'A', 'SE', 'A', 'J', 'SD', 'Q', 'SD', 'SE', 'SE', 'Q', 'J', 'A', 'A', 'SD', 'SB', 'SE', 'A', 'SA', 'J', 'SS', 'SC', 'SD', 'SE', 'A', 'SS', 'Q', 'SE', 'A', 'SB', 'SE', 'SE', 'A', 'SA', 'Q', 'Q', 'J', 'Q', 'K', 'K', 'A', 'J', 'A', 'J', 'J', 'J', 'SD', 'A', 'Q', 'K', 'A', 'Q', 'Q', 'J', 'K', 'SS', 'A', 'K', 'Q', 'K', 'J', 'K', 'Q', 'SD', 'SE', 'SD', 'SA', 'A', 'A', 'Q', 'K', 'SC', 'K', 'W', 'SE', 'K', 'SE', 'J', 'SE', 'A', 'SE', 'K', 'A', 'K', 'SD', 'K', 'SC', 'K', 'A', 'SE', 'A', 'SD', 'A', 'Q', 'Q', 'K', 'A', 'K', 'A', 'A', 'SA', 'J', 'J', 'SD', 'SD', 'W', 'SB', 'K', 'A', 'K', 'A', 'K', 'SB', 'SA', 'K', 'SS', 'K', 'K', 'A', 'A', 'SS', 'Q', 'SC', 'SE', 'K', 'SE', 'SC', 'K', 'SD', 'A', 'K', 'SB', 'A', 'SD', 'K', 'K', 'SE', 'J', 'SD', 'Q', 'J']
    reel_list_col_4 = ['K', 'J', 'SC', 'J', 'SC', 'SC', 'SB', 'SA', 'SE', 'SA', 'Q', 'J', 'SC', 'J', 'J', 'K', 'Q', 'SE', 'Q', 'SS', 'K', 'J', 'SS', 'J', 'Q', 'SS', 'SE', 'A', 'J', 'J', 'SB', 'Q', 'A', 'SD', 'SA', 'SD', 'SA', 'K', 'SA', 'J', 'SB', 'A', 'SA', 'SC', 'SB', 'K', 'A', 'SB', 'A', 'SB', 'SB', 'J', 'A', 'K', 'J', 'W', 'K', 'A', 'J', 'Q', 'SB', 'J', 'SB', 'J', 'SD', 'SC', 'K', 'SA', 'SB', 'K', 'Q', 'A', 'J', 'SS', 'J', 'SB', 'Q', 'SC', 'K', 'A', 'SA', 'Q', 'SC', 'K', 'K', 'Q', 'SC', 'SA', 'SC', 'Q', 'SA', 'SB', 'A', 'J', 'SC', 'SS', 'SA', 'Q', 'SA', 'SE', 'SB', 'K', 'A', 'Q', 'A', 'A', 'SB', 'SD', 'A', 'J', 'SD', 'Q', 'Q', 'SA', 'Q', 'SC', 'W', 'Q', 'J', 'SC', 'Q', 'SA', 'Q', 'Q', 'SA', 'A', 'Q', 'J', 'W', 'SC', 'SC', 'SE', 'A', 'A', 'SB', 'K', 'K', 'K', 'K']
    reel_list_col_5 = ['W', 'SA', 'Q', 'SB', 'SE', 'K', 'SD', 'SC', 'SS', 'K', 'SC', 'SE', 'SD', 'SA', 'Q', 'Q', 'SD', 'A', 'J', 'SE', 'J', 'K', 'K', 'SE', 'SA', 'A', 'K', 'K', 'SD', 'W', 'A', 'SD', 'Q', 'A', 'Q', 'SC', 'SA', 'SA', 'SB', 'SS', 'A', 'Q', 'A', 'K', 'SD', 'SC', 'K', 'A', 'SS', 'Q', 'SE', 'SB', 'SA', 'J', 'Q', 'SC', 'SE', 'SA', 'J', 'K', 'Q', 'A', 'SD', 'K', 'SB', 'SE', 'SB', 'SC', 'SB', 'SD', 'SC', 'SS', 'SE', 'SA', 'W', 'A', 'A', 'K', 'SA', 'A', 'A', 'SC', 'W', 'K', 'K', 'Q', 'SA', 'J', 'SS', 'Q', 'SB', 'A', 'K', 'J', 'SB', 'SC', 'J', 'A', 'SB', 'K', 'K', 'A', 'J', 'SE', 'SE', 'SC', 'SE', 'A', 'SA', 'J', 'SC', 'Q', 'J', 'SC', 'Q', 'A', 'W', 'SB', 'SD', 'SD', 'SD', 'K', 'SE', 'SB', 'J', 'SA', 'Q', 'J', 'SB', 'SA', 'SB', 'W', 'J', 'W', 'SC', 'SD', 'J']
    


    pay_objs =  ['SA', 'SB', 'SC', 'SD', 'SE', 'A', 'K', 'Q', 'J', 'SS']
    pay_bets =    [[0.0, 0.0, 0.6, 2.5, 10.0], [0.0, 0.0, 0.4, 2.0, 5.0], [0.0, 0.0, 0.4, 1.6, 4.0], [0.0, 0.0, 0.3, 1.5, 3.5], [0.0, 0.0, 0.3, 1.2, 3.0], [0.0, 0.0, 0.2, 0.6, 2.5], [0.0, 0.0, 0.16, 0.5, 2.4], [0.0, 0.0, 0.1, 0.4, 2.0], [0.0, 0.0, 0.04, 0.3, 1.6], [0.0, 0.0, 5.0, 50.0, 250.0]]



    #C'est obetnier from package/ja_datascientist_slot_symbol_distribution.py
    test_dict = {3: {'SA': 52559, 'SB': 34252, 'SC': 113228, 'SD': 245454, 'A': 94065, 'K': 35593, 'Q': 125956, 'J': 65002, 'T': 140009, 'SS': 80166}, 4: {'SA': 4574, 'SB': 2028, 'SC': 14797, 'SD': 19134, 'A': 9451, 'K': 5800, 'Q': 11402, 'J': 7700, 'T': 10863, 'SS': 7389}, 5: {'SA': 417, 'SB': 293, 'SC': 1021, 'SD': 1962, 'A': 469, 'K': 1001, 'Q': 1553, 'J': 1206, 'T': 1042, 'SS': 902}}


    # col_at 0,  row at 9 
    write_5X3_line("table_static_v2.xlsx",50000,0.95,4,2,0.33,\
           reel_list_col_1,reel_list_col_2,reel_list_col_3,reel_list_col_4,reel_list_col_5,\
           pay_objs,pay_bets,\
           test_dict,25) #25line


    




    



