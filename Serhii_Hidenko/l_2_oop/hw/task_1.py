from Serhii_Hidenko.l_2_oop.hw.baseinsight import BaseInsight
from Serhii_Hidenko.source.hw_start import insights


if __name__ == "__main__":

    for insight in insights:

        try:
            bi = BaseInsight(**insight)
        except ValueError as err:
            print(f"Error: {err}")
        else:
            print(bi.__dict__)
