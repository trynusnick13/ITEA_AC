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

if __name__ == '__main__':
    for i in insights:
        print(i.get('page_id'))
    replacing(insights, 'page_id', '(not set)', None)