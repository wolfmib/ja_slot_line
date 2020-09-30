

import pandas as pd



# Input Example:
    # ja_docker_write_pkl.run("test_pd",my_df)
def run(input_file_name,input_df,option_path="docker_vol"):
    input_df.to_pickle("./%s/%s.pkl"%(option_path,input_file_name))








if __name__ == "__main__":

    name_list =  ['johnny','jason','mary','jean','take','douge']
    age_list  =  [36,29,26,40,34,38]

    my_pd = pd.DataFrame(list(zip(name_list,age_list)),columns=["Norm","Age"])

    print("[🐳]: let's write the pkl to docker_vol ")
    print("my_pd:                ",my_pd)
    run("test_pkl_output_pd",my_pd)
