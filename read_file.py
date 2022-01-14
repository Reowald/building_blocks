import pandas as pd
import time

# arb_id = hex(0x1005102)
# pid = hex(0x8012)

# df = pd.DataFrame({'Arb ID': arb_id,
#                    'PID': pid},
#                   index=[1])

# data_json = df.to_json(orient='split')
#
# data = pd.read_json(data_json)



# with open('send.csv', 'w') as file:
#     file.write(str(df))
#
# with open('send.csv', encoding="utf8") as input_txt:
#     data = input_txt.readlines()


#
# count = 0
#
# while True:
#     try:
#         time.sleep(1)
#         msg_id = data
#         print(msg_id)
#
#
#         if
#
#     except KeyboardInterrupt:
#         break

while True:
    try:
        df = pd.read_csv('send.csv')
        for i in range(len(df)):
            if df.at[i, 'Send'] == True:
                print('Send the following', df.iloc[i])
            else:
                print('Just hanging around!')
        time.sleep(1)

    except KeyboardInterrupt:
        break
