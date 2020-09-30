
import copy

"""
let's test pytest.

v1: meet basic symbol-win-lines:  only for 3, 4 , 5 line wins

🌟🌟🌟🌟
v2: add S1: 3 (counts), 4(counts), 5(counts) winning scores. 


"""

# slot for 25 lines
# thanks to mary for implement...
line_25_setting = [
    [1,1,1,1,1], # 1
    [0,0,0,0,0], # 2
    [2,2,2,2,2], # 3

    [0,1,2,1,0], # 4
    [2,1,0,1,2], # 5
    [0,0,1,0,0], # 6

    [2,2,1,2,2], # 7
    [1,2,2,2,1], # 8
    [1,0,0,0,1], # 9

    [1,0,1,0,1], # 10
    [1,2,1,2,1], # 11
    [0,1,0,1,0], # 12

    [2,1,2,1,2], # 13
    [1,1,0,1,1], # 14
    [1,1,2,1,1], # 15

    [0,1,1,1,0], # 16
    [2,1,1,1,2], # 17
    [0,2,0,2,0], # 18

    [2,0,2,0,2], # 19
    [0,2,2,2,0], # 20
    [2,0,0,0,2], # 21

    [0,0,2,0,0], # 22
    [2,2,0,2,2], # 23
    [0,2,1,2,0], # 24
    [2,0,1,0,2]  # 25

]


line_obj_bet_rate = {
    "H1": {2:   2,  3:   30, 4:  200, 5:    750},
    "H2": {2:   2,  3:   30, 4:  100, 5:    750},
    "H3": {2:   0,  3:   25, 4:   75, 5:    400},
    "H4": {2:   0,  3:   20, 4:   75, 5:    300},
    "H5": {2:   0,  3:   20, 4:   50, 5:    300},
    "L1": {2:   0,  3:   15, 4:   30, 5:    150},
    "L2": {2:   0,  3:   15, 4:   30, 5:    150},
    "L3": {2:   0,  3:   10, 4:   25, 5:    130},
    "L4": {2:   0,  3:   10, 4:   25, 5:    130},
    "L5": {2:   0,  3:    5, 4:   20, 5:    100},
    "L6": {2:   2,  3:    5, 4:   20, 5:    100},
    "W1": {2:  35,  3:  250, 4: 2500, 5:  10000},
    "S1": {2:   2,  3:    5, 4:   20, 5:    500},
}


# 🌟🌟🌟🌟: add the S1 
#          :also add the H1-H5, L1-L5 2 cases.  
line_obj_25_test_coverage = {
    "H1": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "H2": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "H3": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "H4": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "H5": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "L1": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "L2": {
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "L3": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "L4": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "L5": {
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "L6": {
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "W1": { 
            2: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            3: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            4: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False},
            5: {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False, 16:False, 17:False, 18:False, 19:False, 20:False, 21:False, 22:False, 23:False, 24:False, 25:False}
          },
    "S1":{
        2:{ 1: False},
        3:{ 1: False},
        4:{ 1: False},
        5:{ 1: False}
    }
}





def test_non_wild(input_obj,input_list):
    test_list = copy.deepcopy(input_list)
    if input_obj in test_list:
        while input_obj in test_list:
            test_list.remove(input_obj)
        while "W1" in test_list:
            test_list.remove("W1")
    else:
        return False
    
    if not test_list:
        return True
    else:
        return False


## 說明
## 通常系統判斷W1-3蓮,  利用這個確認此盤面是否是4連 True: 是, False: 不是
## input_obj = "W1"
## input_list = ["W1","W1","W1","W1"] return True
## input_obj = "W1"
## input_list = ["W1","W1","W1","H1"] return False

def test_wild_v1(input_obj, input_list):
    test_list = copy.deepcopy(input_list)
    if input_obj in test_list:
        while "W1" in test_list:
            test_list.remove("W1")
    else:
        return False
    
    # 表示input_list 中 全部都是wilds, test_list is empty now.
    if not test_list:
        return True 

    # 表示input_list 中 不全然是wilds, test_list is NOT empty
    else:
        return False 



class agent():
    def __init__(self):
        print("🧪 :[ja_pytest]: Please tune the parameter in the script so that the test will working with correct setting_informaiton")
        print("🧪 :[ja_pytest]: you get it ?")
        input()
        self.line_setting = line_25_setting
        self.line_obj_bet_rate = line_obj_bet_rate
        self.line_obj_25_test_coverage = line_obj_25_test_coverage


        print(self.line_setting)
        print("-------")
        print(self.line_obj_bet_rate)
        print("---------")
        input("🧪 :[ja_pytest]: confirm two setting !")
        print("------------")
        print(self.line_obj_25_test_coverage)
        print("------------")
        input("🧪 :[ja_pytest]: confirm test coverage map !\n")


        # 🌟🌟🌟: how_many_cases: v2 version. add new cases S1.
        cnt = 0 
        for any_obj in self.line_obj_25_test_coverage:
            for any_win_line in self.line_obj_25_test_coverage[any_obj]:
                tem_len = len(self.line_obj_25_test_coverage[any_obj][any_win_line])
                cnt += tem_len
                print("🧪 :[ja_pytest]:    load      ", any_obj, "   ",any_win_line, "   ", tem_len, " total_size = ",cnt)
         
        self.how_many_cases = cnt
        self.passed_cases  = 0
        input("🧪 :[ja_pytest]: total test cases  =   %4d,  current passed cases = %2d \n"%(self.how_many_cases,self.passed_cases))

        
        # Wild notification
        print("🧪 : This test will apply only 'W1' for step_2_test_line_index() testing ")
        input("[ja_pytest]: do you copy ?")



    # H1, 3 -> 50
    # H1, 4 -> 80 for example
    # if match, return True, if False return False
    def step_1_test_bet_amount(self,test_bet_rate,input_obj,input_win_line):
        if test_bet_rate == self.line_obj_bet_rate[input_obj][input_win_line]:
            return True
        else:
            print("🧪 :[ja_pytest]: raised error with test_bet_amount")
            print("test_bet_rate   =     ", test_bet_rate,  "     self.line_obj_rate[%s][%d]   =   "%(input_obj,input_win_line),self.line_obj_bet_rate[input_obj][input_win_line])
            assert test_bet_rate == self.line_obj_bet_rate[input_obj][input_win_line]


    # W1  or  (W1, W2 ) pairs ,depend on slot-game, implement by your self. 
    # now the case is that "it's W1 only"
    def step_2_test_line_index(self,test_line_index,input_obj,input_win_line,input_list_r):

        # 💡: quick error_diaplay_function.
        def __show_step_2_error_info(ii_test_line_index,ii_obj,ii_win_line,ii_list_r):
            
            ui_line_index = ii_test_line_index + 1
            print("ii_test_line_index  =  ",ui_line_index)
            print("ii_obj              =  ",ii_obj)
            print("ii_win_line         =  ",ii_win_line)
            print("ii_list_r           =  ",ii_list_r)
        

        # 🌟🌟🌟:  add S1 Cases
        if input_obj == "S1":
            print("[ja_pytest]:   meet S1 cases")

            # the S1 , 3, 4, 5 only have one test_line_index each
            assert test_line_index == 1

            # count S1 again
            s1_check_cnts = 0
            for any_col_list in input_list_r:
                for any_obj in any_col_list:
                    if any_obj == "S1":
                        s1_check_cnts += 1
            
            if s1_check_cnts != input_win_line:

                # 💡 讓我指引你一盞明燈 
                __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)

                return False
            else:
                return True

        
        # 🌟🌟🌟:  implement the 2, 3, 4, 5 win_line later...  🙃
        else:

            obj_1 = input_list_r[0][self.line_setting[test_line_index][0]]
            obj_2 = input_list_r[1][self.line_setting[test_line_index][1]]
            obj_3 = input_list_r[2][self.line_setting[test_line_index][2]]
            obj_4 = input_list_r[3][self.line_setting[test_line_index][3]]
            obj_5 = input_list_r[4][self.line_setting[test_line_index][4]]



            # consider non-wild case and in the line_setting dict:
            if input_obj in self.line_obj_bet_rate:

                # add error_cases, input_win_line might be 4 or 5
                if input_win_line == 3:

                    # check error_case win_line=5
                    check_win_5_list = [obj_1,obj_2,obj_3,obj_4,obj_5]
                    res              = test_non_wild(input_obj,check_win_5_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 3, but the win_line is 5  ")
                        # 💡
                        __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)

                    
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check error_case win_line = 4
                    check_win_4_list = [obj_1,obj_2,obj_3,obj_4]
                    res              = test_non_wild(input_obj,check_win_4_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 3, but the win_line is 4")
                        # 💡
                        __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)
                        
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check it's 3 line or not
                    check_win_3_list = [obj_1,obj_2,obj_3]
                    res              = test_non_wild(input_obj,check_win_3_list)
                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 3, but the win_line is not")
                        # 💡
                        __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)

                        # didn't pass test
                        return False

                # add error case, input_win_line= 5
                elif input_win_line == 4:
                    # check error_case win_line=5
                    check_win_5_list = [obj_1,obj_2,obj_3,obj_4,obj_5]
                    res              = test_non_wild(input_obj,check_win_5_list)


                    

                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 4, but the win_line is 5")

                        # 💡
                        __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)

                        # didn't pass test
                        return False
                    else:
                        pass

                    # check it's 4 line or not
                    check_win_4_list = [obj_1,obj_2,obj_3,obj_4]
                    res              = test_non_wild(input_obj,check_win_4_list)
                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 4, but the win_line is not")

                        # 💡
                        __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)

                        # didn't pass test
                        return False

                elif input_win_line == 5:
                    # check it's 5 line or not 
                    check_win_5_list = [obj_1,obj_2,obj_3,obj_4,obj_5]
                    res              = test_non_wild(input_obj,check_win_5_list)
                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 5, but the win_line is not")

                        # 💡
                        __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)

                        # didn't pass test
                        return False

                elif input_win_line == 2:
                    # check it's 2 line or not 
                    check_win_2_list = [obj_1,obj_2]
                    res              = test_non_wild(input_obj,check_win_2_list)

                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 2, but the win_line is not")

                        # 💡
                        __show_step_2_error_info(test_line_index,input_obj,input_win_line,input_list_r)
                        # didn't pass test
                        return False                 

                else:
                    print("[ja_pytest]: False: unspport win_line 3 or 4 or 5:  ",input_win_line)
                    return False

                # Remove all false cases, the rest case is pass. return True
                return True

                
            # consider the "Wild case" 
            elif input_obj == "W1":
                # add error_cases, input_win_line might be 4 or 5
                if input_win_line == 3:
                    # check error_case win_line=5
                    check_win_5_list = [obj_1,obj_2,obj_3,obj_4,obj_5]
                    res              = test_wild_v1(input_obj,check_win_5_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 3, but the win_line is 5")
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check error_case win_line = 4
                    check_win_4_list = [obj_1,obj_2,obj_3,obj_4]
                    res              = test_wild_v1(input_obj,check_win_4_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 3, but the win_line is 4")
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check it's 3 line or not
                    check_win_3_list = [obj_1,obj_2,obj_3]
                    res              = test_wild_v1(input_obj,check_win_3_list)
                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 3, but the win_line is not")
                        # didn't pass test
                        return False

                elif input_win_line == 4:
                    # check error_case win_line=5
                    check_win_5_list = [obj_1,obj_2,obj_3,obj_4,obj_5]
                    res              = test_wild_v1(input_obj,check_win_5_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 3, but the win_line is 5")
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check it's 4 line or not
                    check_win_4_list = [obj_1,obj_2,obj_3,obj_4]
                    res              = test_wild_v1(input_obj,check_win_4_list)
                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 4, but the win_line is not")
                        # didn't pass test
                        return False

                elif input_win_line == 5:
                    # check it's 5 line or not 
                    check_win_5_list = [obj_1,obj_2,obj_3,obj_4,obj_5]
                    res              = test_wild_v1(input_obj,check_win_5_list)
                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 5, but the win_line is not")
                        # didn't pass test
                        return False

                elif input_win_line == 2:

                    # check error_case win_line=5
                    check_win_5_list = [obj_1,obj_2,obj_3,obj_4,obj_5]
                    res              = test_wild_v1(input_obj,check_win_5_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 2, but the win_line is 5")
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check error_case win_line = 4
                    check_win_4_list = [obj_1,obj_2,obj_3,obj_4]
                    res              = test_wild_v1(input_obj,check_win_4_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 2, but the win_line is 4")
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check error_case win_line = 3
                    check_win_3_list = [obj_1,obj_2,obj_3]
                    res              = test_wild_v1(input_obj,check_win_3_list)
                    if res == True:
                        print("[ja_pytest]: False:  judge win_line 2, but the win_line is 3")
                        # didn't pass test
                        return False
                    else:
                        pass

                    # check it's 2 line or not 
                    check_win_2_list = [obj_1,obj_2]
                    res              = test_wild_v1(input_obj,check_win_2_list)
                    if res == True:
                        pass
                    else:
                        print("[ja_pytest]: False:  judge win_line 2, but the win_line is not")
                        # didn't pass test
                        return False



                else:
                    print("[ja_pytest]: False: unspport win_line 3 or 4 or 5:  ",input_win_line)
                    return False

                # Remove all false cases, the rest case is pass. return True
                return True

            
            else:
                print("Error:  The obj:  %s  is not in the line_obj_dict: \n %s \n"%(input_obj,self.line_obj_bet_rate))
                return False



    #  # 🌟🌟🌟:  add S1 Cases
    def step_3_test_win_line_20_gain_v1(self,test_gain,input_obj,input_win_line,input_line_index):

        if input_obj == "S1":
            expected_gain = self.line_obj_bet_rate[input_obj][input_win_line]


            # 🌟: S1 input_line_index = 1 
            if test_gain == expected_gain:
                if self.line_obj_25_test_coverage[input_obj][input_win_line][input_line_index] == True:
                    pass
                else:
                    self.line_obj_25_test_coverage[input_obj][input_win_line][input_line_index] = True

                    print("[ja_pytest][keyword_pytest_coverage]:  current test_coverage updated:  obj: %s  win_line: %d  ui_line_index %d  "%(input_obj,input_win_line,input_line_index))
                    
                    # 💡
                    # self.show_test_coverage()

                return True
            else:
                return False
              

        else:
            # Jason: gain = bet_rate / 25
            expected_gain = float(self.line_obj_bet_rate[input_obj][input_win_line] / 25)

            print("test_gain =   ",test_gain)
            print("expec gain    ",expected_gain)

            if test_gain == expected_gain:
                
                #  Debug: print("[Debug]: the line_index  = ",input_line_index)
                #  Debug: input()
                #  Debug: print("[ja_pytest]: pass case obj: %s  , win_line: %2d , ui_line_index: %2d ,gain: %.4f"%(input_obj,input_win_line,input_line_index+1,expected_gain))

                #  Debug: print("[Debug]: input_obj        ",input_obj)
                #  Debug: print("[Debug]: input_win_line   ",input_win_line)
                #  Debug: print("[Debug]: input_line_index ",input_line_index)


                # Set the test_coverage:
                # 🌟: for non-S1 symbols, we add index +1 , for ui_purpose. 
                ui_line_index = input_line_index + 1
                if self.line_obj_25_test_coverage[input_obj][input_win_line][ui_line_index] == True:
                    pass
                else:
                    self.line_obj_25_test_coverage[input_obj][input_win_line][ui_line_index] = True

                    print("[ja_pytest][keyword_pytest_coverage]:  current test_coverage updated:  obj: %s  win_line: %d  ui_line_index %d  "%(input_obj,input_win_line,ui_line_index))
                    
                    # 💡
                    #self.show_test_coverage()
                
                return True
            else:
                return False


    # 🌟🌟🌟: v2 version  optimized the coding to meet different win_line between (W1, H1, H2) to others. 
    def show_test_coverage(self,key="slot_04"):

        if key == "slot_04":
            for any_obj in self.line_obj_25_test_coverage:
                for any_win_line in self.line_obj_25_test_coverage[any_obj]:
                    print("\n---------Symbol: %s     WinLine:  %d------------------------"%(any_obj,any_win_line))
                    print(self.line_obj_25_test_coverage)
    """     
           之前v1 程式的拉....
               for any_obj in self.line_obj_25_test_coverage:
                if any_obj == "W1" or any_obj == "H1" or any_obj == "H2":
                    print("\n---------------%s----------------"%any_obj)    
                    print("----------- 3 ------------")
                    print(line_obj_25_test_coverage[any_obj][3])
                    print("----------- 4 ------------")
                    print(line_obj_25_test_coverage[any_obj][4])
                    print("----------- 5 ------------")
                    print(line_obj_25_test_coverage[any_obj][5])
                    print("-----------------------------------\n")
    """


    # 🌟🌟🌟: v2 version optimzed the coding to meet different win_line between (W1, H1, H2) to others.
    def show_test_cases_coverage(self):

        # Recalculate again
        self.passed_cases = 0
        for any_obj in self.line_obj_25_test_coverage:
            for any_win_line in self.line_obj_25_test_coverage[any_obj]:
                for any_line_index in self.line_obj_25_test_coverage[any_obj][any_win_line]:
                    if self.line_obj_25_test_coverage[any_obj][any_win_line][any_line_index]:
                        self.passed_cases += 1
                    else:
                        pass

        print("🧪: how_many_cases       = ",self.how_many_cases)
        print("🧪: how_many_cases_pass  = ",self.passed_cases)
        print("🧪: Test coerage.        =  %.4f"%float(self.passed_cases/self.how_many_cases))






"""


[{'win_obj': 'H2', 'win_line': 3, 'win_list_r': [['W1', 'L2', 'L1'], ['W1', 'L1', 'L4'], ['H2', 'H4', 'L6'], ['L6', 'L4', 'H2'], ['S1', 'L5', 'H4']], 'win_gain': 0.0, 'win_line_index': 1, 'win_bet_rate': 40.0}, {'win_obj': 'W1', 'win_line': 2, 'win_list_r': [['W1', 'L2', 'L1'], ['W1', 'L1', 'L4'], ['H2', 'H4', 'L6'], ['L6', 'L4', 'H2'], ['S1', 'L5', 'H4']], 'win_gain': 2.0, 'win_line_index': 5, 'win_bet_rate': 40.0}]
test_gain =    0.0
expec gain     2.0




bug H4-4:  gain = 0.0 ?
[{'win_obj': 'H1', 'win_line': 4, 
 'win_list_r': [['S1', 'H3', 'W1'], ['H3', 'W1', 'L2'], ['H3', 'W1', 'L2'], ['L5', 'H1', 'L6'], ['L5', 'H4', 'L6']], 
 'win_gain': 0.0, 
 'win_line_index': 10, 
 'win_bet_rate': 500.0
 }

Root cause:  W-3 pay score = 500   ,   it's equal to H1-4 pay score = 500 as well... causing the wild_gain ~ obj_gain, so the code didn't assign current_gain in this case..
Fix after chaning the W-3 pay scores from 500 to 600


"""





if __name__ == "__main__":

    """
    win_obj  = "H1"
    win_line = 3 
    print("win_obj  = ",win_obj)
    print("win_line = ",win_line)
    print("win_bet  = ",line_obj_bet_rate[win_obj][win_line])

    for any_obj in line_obj_25_test_coverage:
        print("\n---------------%s----------------"%any_obj)
        print(line_obj_25_test_coverage[any_obj])
        print("-----------------------------------\n")
    """

    test_agent = agent()

    test_agent.show_test_cases_coverage()

    


