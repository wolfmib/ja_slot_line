import pandas as pd



"""
Jason:
    from collections import defaultdict
    dic={}
    for g in ['male', 'female']:   
      dic[g]=defaultdict(dict)
      for y in [2013, 2014]:
        dic[g][y]=df[(df[Gender]==g) & (df[Year]==y)] #store the DataFrames to a dict of dict

    !! Add iloc[0]["Count"]: 0 first_row,   Count, columnname
    dic[3]["SA"] = group_df[ (group_df["Group_Win_Line"] == 3) & (group_df["Win_Obj"] == "SA")].iloc[0]["Count"]


Target: 
    The goal is loaing pickle
    Seperate the SA_3 , SA_4, SD_5 .. counts and probability etc..



Input:
    lineable_obj_list =  ["SA","A","K"]
    win_list = [3, 4, 5]

output:
    dic{}
    group_df
"""



def run_line(i_lineable_obj_list, i_win_list, i_df):
    i_df["new_id"] = i_df.index 

    group_df = i_df.groupby(["Group_Win_Line","Win_Obj"])["new_id"].count().reset_index(name="Count")
    
    dic = {}
  
    for g_win in i_win_list:
        dic[g_win]= {}
        for g_obj in i_lineable_obj_list:
            _tem = group_df
            #v = _tem[ (_tem["Group_Win_Line"] == g_win) & (_tem["Win_Obj"] == g_obj)].iloc[0]["Count"]
            try:
                dic[g_win][g_obj] = _tem[ (_tem["Group_Win_Line"] == g_win) & (_tem["Win_Obj"] == g_obj)].iloc[0]["Count"]
            except:
                dic[g_win][g_obj] = 0.0
            #print(dic[g_win][g_obj] )

    return dic, group_df





if __name__ == "__main__":
    lineable_obj_list =  ["SA","SB","SC","SD","A","K","Q","J","T","SS","W"]
    win_list = [3,4,5]
    pickle_name = "result.pkl"

    # Load Pickle to DataFrame
    df = pd.read_pickle(pickle_name)
    
    # Run Function
    dic, new_df = run_line(lineable_obj_list,win_list,df)

    print("obj_list                     =",lineable_obj_list)
    print("win_list                     =",win_list)
    print("picklename                   =",pickle_name)

    print("-----------------------------")
    print(dic)
    print(new_df)


    """     Test Result 

            obj_list                     = ['SA', 'SB', 'SC', 'SD', 'A', 'K', 'Q', 'J', 'T', 'SS']
            win_list                     = [3, 4, 5]
            picklename                   = result.pkl

            -----------------------------
            {3: {'SA': 52559, 'SB': 34252, 'SC': 113228, 'SD': 245454, 'A': 94065, 'K': 35593, 'Q': 125956, 'J': 65002, 'T': 140009, 'SS': 80166}, 4: {'SA': 4574, 'SB': 2028, 'SC': 14797, 'SD': 19134, 'A': 9451, 'K': 5800, 'Q': 11402, 'J': 7700, 'T': 10863, 'SS': 7389}, 5: {'SA': 417, 'SB': 293, 'SC': 1021, 'SD': 1962, 'A': 469, 'K': 1001, 'Q': 1553, 'J': 1206, 'T': 1042, 'SS': 902}}
                Group_Win_Line Win_Obj   Count
            0                3       A   94065
            1                3       J   65002
            2                3       K   35593
            3                3       Q  125956
            4                3      SA   52559
            5                3      SB   34252
            6                3      SC  113228
            7                3      SD  245454
            8                3      SS   80166
            9                3       T  140009
            10               4       A    9451
            11               4       J    7700
            12               4       K    5800
            13               4       Q   11402
            14               4      SA    4574
            15               4      SB    2028
            16               4      SC   14797
            17               4      SD   19134
            18               4      SS    7389
            19               4       T   10863
            20               5       A     469
            21               5       J    1206
            22               5       K    1001
            23               5       Q    1553
            24               5      SA     417
            25               5      SB     293
            26               5      SC    1021
            27               5      SD    1962
            28               5      SS     902
            29               5       T    1042
    """
    


