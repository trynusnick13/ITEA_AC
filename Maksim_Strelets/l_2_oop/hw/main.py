from Maksim_Strelets.l_2_oop.hw.network_dependent_insights import *
from Yurii_Khomych.l_1_functions.hw_start import insights


def insight_chooser(api):
    return {
        1: FacebookInsight,
        2: GoogleInsight,
        3: TwitterInsight,
        4: SnapchatInsight
    }[api]


def insight_builder(insight_list):
    res = []
    for el in insight_list:
        if "api" in el.keys():
            res.append(insight_chooser(el["api"])(**el))
    return res


a = insight_builder(insights)
pass
