import numpy as np
import pandas as pd

df = pd.read_json("sample_data.json")

# print(df.columns)

user_exp_df = df[['id','event_date','city','problem_area','status','cancellation_reason','rating','feedback_reason', 'handling_time','first_response']]

user_exp_df.to_csv('user_exp_data.csv')
