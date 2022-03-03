import time
from dataclasses import dataclass

import pandas
from threading import Thread


@dataclass
class DataFrameHolder:
    """This dataclass holds a reference to the current DF in memory.
    This is necessary if you do operations without in-place modification of
    the DataFrame, since you will need replace the whole object.
    """
    dataframe: pandas.DataFrame = pandas.DataFrame(columns=['A', 'B'])

    def update(self, data):
        self.dataframe = self.dataframe.append(data, ignore_index=True)


class StreamLoader:
    """This class is our worker communicating with the websocket"""

    def __init__(self, df_holder: DataFrameHolder) -> None:
        super().__init__()
        self.df_holder = df_holder

    def update_df(self):
        # read from websocket and update your DF.
        data = {
            'A': [1, 2, 3],
            'B': [4, 5, 6],
        }
        self.df_holder.update(data)

    def run(self):
        # limit loop for the showcase
        for _ in range(5):
            self.update_df()
            print("[1] Updated DF %s" % str(self.df_holder.dataframe))
            time.sleep(3)


class LightComputation:
    """This class is a random computation worker"""

    def __init__(self, df_holder: DataFrameHolder) -> None:
        super().__init__()
        self.df_holder = df_holder

    def compute(self):
        print("[2] Current DF %s" % str(self.df_holder.dataframe))

    def run(self):
        # limit loop for the showcase
        for _ in range(5):
            self.compute()
            time.sleep(5)


def main():
    # We create a DataFrameHolder to keep our DataFrame available.
    df_holder = DataFrameHolder()

    # We create and start our update worker
    stream = StreamLoader(df_holder)
    stream_process = Thread(target=stream.run)
    stream_process.start()

    # We create and start our computation worker
    compute = LightComputation(df_holder)
    compute_process = Thread(target=compute.run)
    compute_process.start()

    # We join our Threads, i.e. we wait for them to finish before continuing
    stream_process.join()
    compute_process.join()


if __name__ == "__main__":
    main()