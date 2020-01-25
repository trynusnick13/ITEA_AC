from sys import path
from Nikita_Trynus.l_1_functions.insights_hw import *
path.append(r'/Users/nicktrynus/ITEA_AC/Yurii_Khomych/l_1_functions/')
from hw_start import insights



# 1 exercise
new_insights = remove_by_value(insights, 'period count total_count page_id link status days_in_data')

# 2 exercise
new_insights = remove_by_value(insights, 'unit', 'EUR')
new_insights = remove_by_value(insights, 'unit_key', 'EUR')

# 3 && 4 exercises
list_of_objectives = get_all(insights, [], 'objective')
dict_of_objectives = dict(zip(list(range(len(list_of_objectives))), list_of_objectives))
unique = set(list_of_objectives)

# 5 exercise
list_of_campaign_id = get_all(insights, [], 'campaign_id')
dict_of_campaign_id = dict(zip(list(range(len(list_of_campaign_id))), list_of_campaign_id))

# 6 exercise
sum_ = calculating('sum')
sum_level = calculating('sum_level')
sum_general = calculating('sum_general')
print(sum_, sum_level, sum_general)

# 7 exercise
sorted_api = sorting(insights, 'api')
sorted_type = sorting(insights, 'type')
sorted_report_name = sorting(insights, 'report_name')
sorted_objective = sorting(insights, 'objective')

# 8+9 exercises
replacing(insights, 'report_name', 'device', 'device'.upper())
replacing(insights, 'page_id', '(not set)', None)