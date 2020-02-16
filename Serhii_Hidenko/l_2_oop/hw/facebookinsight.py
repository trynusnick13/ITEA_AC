from Serhii_Hidenko.l_2_oop.hw.baseinsight import BaseInsight


class FacebookInsight(BaseInsight):

    def __init__(self, dimensions_dict=None, dimensions=None, **kwargs):

        self.dimensions_dict = dimensions_dict
        self.dimensions = dimensions

        super().__init__(**kwargs)
