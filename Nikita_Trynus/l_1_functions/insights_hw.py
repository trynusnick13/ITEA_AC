from Yurii_Khomych.l_1_functions.hw_start import *


def remove_in_dict_by_value(some_dict, string='', value=None):
    if value:
        if string in list(some_dict.keys()) and some_dict[string] != value:
            print(f'del {string} in dict by value {some_dict[string]}')
            some_dict.pop(string)
    else:
        if string in list(some_dict.keys()) and some_dict[string] != value:
            print(f'del {string} in dict by value {some_dict[string]}')
            some_dict.pop(string)

    try:
        for elem in list(some_dict.keys()):
            if type(some_dict[elem]) == type(dict()):
                remove_in_dict_by_value(some_dict[elem], string, value)
            elif type(some_dict[elem]) == type(list()):
                remove_by_value(some_dict[elem], string, value)
    except AttributeError as err:
        print(err)


def remove_by_value(some_list, unused_keys='', value=None):
    try:
        if some_list == []:
            raise Exception("Give me something that worth my time")
    except Exception as e:
        print(e)
    bad_guys = unused_keys.split()
    for word in bad_guys:

        for elem in some_list:
            if type(elem) == type(dict()):
                remove_in_dict_by_value(elem, word, value)
    return some_list


def get_all(some_list, all=[], get_key=''):
    for elem in some_list:
        if type(elem) == type(dict()):
            get_all_in_dict(elem, all, get_key)
    return all


def get_all_in_dict(some_dict, all, get_key=''):
    if get_key in list(some_dict.keys()):
        print(f'add {get_key} in dict from {some_dict[get_key]}')
        all.append(some_dict[get_key])

    try:
        for elem in list(some_dict.keys()):
            if type(some_dict[elem]) == type(dict()):
                get_all_in_dict(some_dict[elem], all, get_key)
            elif type(some_dict[elem]) == type(list()):
                get_all(some_dict[elem], all, get_key)
    except AttributeError as err:
        print(err)


def sorting(dict_, by_what):
    return sorted(dict_, key=lambda x: x.get('by_what', 'Nonetype'))


def replacing(dict_, key_to_replace, condition, replacing_word):
    for i in dict_:
        if i.get(key_to_replace) == condition:
            i[key_to_replace] = replacing_word
            print(i.get(key_to_replace, None))


def calculating(string):
    temp = get_all(insights, [], 'metric_sums')
    sum_ = list(map(lambda x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11:
                    x1[string] + x2[string] + x3[string] + x4[string] + x5[string] +
                    x6[string] + x7[string] + x8[string] + x9[string] +
                    x10[string] + x11[string], *temp))
    return sum(sum_)


def formulas(key_for_formula):
    a = {
        1: lambda sum_, sum_level, sum_general, period: (sum_ * sum_level / sum_general) / period,
        2: lambda sum_, sum_level, sum_general, period: (sum_ * sum_level ** 2 / sum_general) / period,
        3: lambda sum_, sum_level, sum_general, period: (sum_level / sum_general) / period,
        4: lambda sum_, sum_level, sum_general, period: (sum_level * sum_general / 100) / period
    }
    return a[key_for_formula]


def elita(list_of_insights, value):
    list_of_entities_mr_than_value = []
    list_of_entities = get_all(list_of_insights, [], 'entities')
    print(list_of_entities)
    for entity in list_of_entities:
        for i in entity:
            if i['spend_sum'] > value:
                list_of_entities_mr_than_value.append(i)

    return list_of_entities_mr_than_value


def work_with_apis(list_of_insights):
    for i in list_of_insights:
        if i.get('period') is None or i.get('period') > 4:
            i['period'] = 7

    list_of_metrics_and_periods_api = []
    for i in list_of_insights:
        if not i.get('metric_sums') is None:
            list_of_metrics_and_periods_api.append((i['metric_sums'], i['period'], i['api']))

    print(list_of_metrics_and_periods_api)
    logg_of_summaries = []
    for lis, period, api in list_of_metrics_and_periods_api:
        for metrics in lis:
            try:
                metrics.update({'summary': formulas(api)(metrics['sum'], metrics['sum_level'],
                                                         metrics['sum_general'], period)})
            except ZeroDivisionError as err:
                print(err, ' Why on earth are you doing this shit, crazy motherfucker!?!?!?!')
                metrics.update({'summary': 0})

            logg_of_summaries.append(metrics['summary'])
    return logg_of_summaries



if __name__ == '__main__':
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
    # 11
###############################
    list_of_appropriate = elita(insights,200)
#####################################################
    # 10
    log = work_with_apis(insights)
    print(log)
