from sys import path
path.append(r'/Users/nicktrynus/ITEA/ITEA_AC/Yurii_Khomych/l_1_functions/')
from hw_start import insights


def remove_in_dict_by_value(some_dict, string='', value=None):
    if value:
        if string in list(some_dict.keys()) and some_dict[string]!=value:
            print(f'del {string} in dict by value {some_dict[string]}')
            some_dict.pop(string)
    else:
        if string in list(some_dict.keys()) and some_dict[string]!=value:
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
    """
    :param some_list: pretty clear
    :param unused_keys: key to delete
    :return: formatted list
    """
    try:
        if some_list == []:
            raise Exception("Give me something that worth my time")
    except Exception as e:
        print(e)
    bad_guys = unused_keys.split()
    for word in bad_guys:

        for elem in some_list:
            if type(elem)==type(dict()):
                remove_in_dict_by_value(elem,word, value)
    return some_list


def get_all(some_list, all=[], get_key=''):
    for elem in some_list:
        if type(elem)==type(dict()):
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


def key_for_sort(dict_):
    return i.get('report_name')


# a = [{'a':1, 'b':1, 'd':4, 'c':{'a':1, 'b':3, 'd':4, 'm':[{'a':1, 'b':3, 'd':4}]}},{'c':1, 'b':3},\
#                                                                     {'a':[{'a':1, 'b':3, 'd':4}]}  ]

# a = remove_by_value(a, 'b')
b = get_all(insights,[], 'metric_sums')
# insights = remove(insights, 'period count total_count page_id link status days_in_data')
#
sum_lev=0
sum_lev =list(map(lambda x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11 :\
                      x1['sum_level']+ x2['sum_level']+ x3['sum_level']+ x4['sum_level']+ x5['sum_level']+\
                      x6['sum_level']+ x7['sum_level']+ x8['sum_level']+ x9['sum_level']+\
                      x10['sum_level']+ x11 ['sum_level'], *b))
print(sum(sum_lev))

a = sorted(insights, key=lambda x: x.get('report_name', 'Nonetype'))
for i in a:
   print(i.get('report_name', 'NoneType'))

for i in insights:
    if i.get('report_name') == 'device':
        i['report_name'] = 'device'.upper()
        print(i['report_name'])
