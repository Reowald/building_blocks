import pandas as pd

arb_id = hex(0x1005102)
pid = b'\x11,\x80'

df = pd.DataFrame({'Arb ID': arb_id,
                   'PID': pid},
                  index=[1, 2])

# with open('send.csv', 'w') as file:
#     file.write(str(df))