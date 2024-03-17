import pandas as pd
import os

adress = "D:\\C_docs\\영 어 단 어 엑 셀 파 일.xlsx"
day_num = input('day num? ')

df = pd.read_excel(adress, sheet_name=f'day{day_num}', header=None)
df_shuffled = df.sample(frac=1).reset_index(drop=True)

if not os.path.exists(adress):
    print('error')
else:
    with pd.ExcelWriter(adress, mode='a', engine='openpyxl') as writer:
        df_shuffled.to_excel(writer, sheet_name=f'day{day_num} test', index=False, header=False)
        print('success')
