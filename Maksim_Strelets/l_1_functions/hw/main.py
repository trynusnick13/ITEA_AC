from Maksim_Strelets.l_1_functions.hw.hw_start import insights
from Maksim_Strelets.l_1_functions.hw.functions import *

removable = ["period", "count", "total_count", "page_id", "entities_affected.entities.link",
             "entities_affected.entities.status", "entities_affected.entities.days_in_data"]

# task 1
# for el in removable:
#     dict_remove(insights, el)

# tasks 2, 9, 10
# dfs(insights)

# task 3
# temp = dict_get(insights, "objective")

# task 4
# temp = ins_to_dict(insights, "id", "objective")

# task 5
# temp = ins_to_dict(dict_get(insights, "entities_affected"), "campaign_id", "campaign_name")

# task 6
# temp = list(set(ins_to_str(insights)))

# task 7
# sum = calculate(insights, "metric_sums.sum")
# sum_level = calculate(insights, "metric_sums.sum_level")
# sum_general = calculate(insights, "metric_sums.sum_general")

# task 8
# insights = sort(insights, "type")
# insights = sort(insights, "api")
# insights = sort(insights, "report_name")
# insights = sort(insights, "objective")


# task 11
calc_by_formula(insights)


# task 12
# temp = dict_get(insights, "entities_affected.entities")
# temp = list(filter(lambda x: int(x["spend_sum"]) > 200, temp))

# print(temp)
# save(insights)