from debugging_code_13 import debug
from timing_functions_14 import timer


class TimeWaster:
    """Time waster class...

    """

    @debug
    def __init__(self, max_num):
        """

        :param max_num:
        """
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


tw = TimeWaster(1000)
tw.waste_time(999)
