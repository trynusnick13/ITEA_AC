from Serhii_Hidenko.l_2_oop.hw.baseinsight import BaseInsight


class TwitterInsight(BaseInsight):

    def __init__(self, first_date=None, last_date=None, **kwargs):

        self.first_date = first_date
        self.last_date = last_date

        super().__init__(**kwargs)
