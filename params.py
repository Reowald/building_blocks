import pandas as pd
import os


# This funtion just imports and sorts the parameter data
def data_sort(csv):
    # this tool should be used carefully with source control
    csv = 'config/' + csv + '.csv'
    print('The following file is being sorted {}'.format(csv))
    df = pd.read_csv(csv)

    df = df.dropna(axis='index', thresh=3)
    df = df.reset_index(drop=True)
    df = df.drop(columns='Unnamed: 0')

    # no high limits are placed on registers as gaps are wildly extravagant
    cmd_hr = 0  # command holding register
    nv_hr = 2000  # non-volatile holding register

    inst_ir = 0  # instrumentation input register
    fw_ir = 2000  # faults and warnings input register
    # sys is an outlier as it will calculate the total system values
    sys_ir = 4000  # system info input register

    try:
        if csv == 'config/cmd.csv':
            reg = cmd_hr
            mbus_reg = 4
        elif csv == 'config/nv.csv':
            reg = nv_hr
            mbus_reg = 4
        elif csv == 'config/inst.csv':
            reg = inst_ir
            mbus_reg = 3
        elif csv == 'config/fw.csv':
            reg = fw_ir
            mbus_reg = 3
        elif csv == 'config/sys.csv':
            reg = sys_ir
            mbus_reg = 3
    except ValueError:
        print('no file or incorrect filename given')

    for rows in range(len(df)):
        if df.at[rows, 'd_type'] == 'U16':
            df.at[rows, 'mbus_offset'] = reg
            reg += 1
        elif df.at[rows, 'd_type'] == 'S16':
            df.at[rows, 'mbus_offset'] = reg
            reg += 1
        elif df.at[rows, 'd_type'] == 'F32':
            df.at[rows, 'mbus_offset'] = reg
            reg += 2
        # make sure these columns are populated with something
        elif pd.isnull(df.at[rows, 'id_priority']):
            df.at[rows, 'id_priority'] = '1'
        elif pd.isnull(df.at[rows, 'freq']):
            df.at[rows, 'freq'] = '1'
        else:
            pass

    df.to_csv(csv)

    return print('Modbus Register offset '
                 'successfully added use SC '
                 'to ensure changes are captured')


# The purpose of this class is to distribute the parameter files
class Pcm_params:

    def __init__(self):
        # MCU parameters
        # commands (send)
        self.file_cmd = 'config/cmd.csv'
        # instrumentation; faults, warnings and measurements
        self.file_inst = 'config/inst.csv'
        # non volatile registers; set-points, gains and configuration
        self.file_nv = 'config/nv.csv'

        # CM4 parameters
        # msg id and modbus registers
        self.file_param = 'config/param.csv'
        # system settings calculated by the cm4
        self.file_sys = 'config/sys.csv'
        # system config unit names address and external V and A settings
        self.file_sys_config = 'config/sys_config.csv'

    #handling of pid bytes for python-can
    def pid_list(self, df):
        pids = []
        for i in range(len(df)):
            pid = df.pid[i]
            #removes '0x' from hex
            pid = bytes.fromhex(pid[2:])
            #flips order for CAN send
            pid = pid[1:2] + pid[0:1]
            pids.append(pid)
        return pids


    def cmd(self):
        df = pd.read_csv(self.file_cmd)
        pids = self.pid_list(df)
        return pids, df

    def inst(self):
        df = pd.read_csv(self.file_inst)
        pids = self.pid_list(df)
        return pids, df

    def nv(self):
        df = pd.read_csv(self.file_nv)
        pids = self.pid_list(df)
        return pids, df


    def param(self):
        df = pd.read_csv(self.file_param)
        pids = self.pid_list(df)
        return pids, df


    def sys(self):
        df = pd.read_csv(self.file_sys)
        return df

    def sys_config(self):
        df = pd.read_csv(self.file_sys_config)

        # active = df.index[df['active'] == True].tolist()
        # mask = df['active'] == True
        # Avoid SettingWithCopy https://www.youtube.com/watch?v=4R4WsDJ-KVc
        # mask = df.active[df.active == True].copy()
        # print('There are: ', mask.sum(), 'active systems configured')
        # list of active systems from config file
        # active = df.iloc[mask]
        # print('Systems configured', active)
        # All of the above is better handled at end to avoid SettingWithCopy errors

        'last 2 bytes'
        read_request = '00'
        write_request = '01'
        read_respond = '02'
        write_respond = '03'
        watchdog = '10'

        # extract active systems from config file as strings
        cm4_r_req = df.cm4 + read_request
        mcu_r_resp = df.mcu + read_respond
        cm4_wr_req = df.cm4 + write_request
        mcu_wr_resp = df.mcu + write_respond

        watchdog = df.mcu + watchdog
        # watchdog can be an int as it has an inherent msg id
        # and will be used for establishing and validating connections
        watchdog = watchdog.apply(int, base=16)

        # all id turn into integers as this is what the arb id will be
        cm4_r_req = cm4_r_req.apply(int, base=16)
        mcu_r_resp = mcu_r_resp.apply(int, base=16)
        cm4_wr_req = cm4_wr_req.apply(int, base=16)
        mcu_wr_resp = mcu_wr_resp.apply(int, base=16)

        df['watchdog'] = watchdog
        df['cm4_r_req'] = cm4_r_req
        df['mcu_r_resp'] = mcu_r_resp
        df['cm4_wr_req'] = cm4_wr_req
        df['mcu_wr_resp'] = mcu_wr_resp

        # active.insert(10, "new col", new_col) this worked
        # mask = df.active[df.active == True].copy()
        mask = df.active == True

        #copy tells pandas that this is new
        active = df.loc[mask].copy()

        print('There are: ', active.shape[0], 'active systems configured')
        print('Systems configured', active)

        return active
