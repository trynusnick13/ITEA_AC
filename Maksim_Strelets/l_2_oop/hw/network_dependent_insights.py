from Maksim_Strelets.l_2_oop.hw.base_insight import *


class FacebookInsight(BaseInsight):
    def __init__(self, dimensions_dict, dimensions, **kwargs):
        self.dimensions_dict = dimensions_dict
        self.dimensions = dimensions
        super().__init__(**kwargs)


class GoogleInsight(BaseInsight):
    def __init__(self, actions, **kwargs):
        self.actions = actions
        super().__init__(**kwargs)


class TwitterInsight(BaseInsight):
    def __init__(self, first_date, last_date, **kwargs):
        self.first_date = first_date
        self.last_date = last_date
        super().__init__(**kwargs)


class SnapchatInsight(BaseInsight):
    def __init__(self, weight, type, **kwargs):
        self.weight = weight
        self.type = type
        super().__init__(**kwargs)
