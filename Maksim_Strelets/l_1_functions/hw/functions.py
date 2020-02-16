import json


# удаляет по имени
def dict_remove(insights_list, name):
    path = name.split(".")

    if not (type(insights_list) is list):
        insights_list = [insights_list]

    for insight in insights_list:
        if not (type(insight) is dict):
            continue

        if not (path[0] in insight.keys()):
            continue

        if len(path) > 1:
            dict_remove(insight[path[0]], ".".join(path[1:]))
        else:
            del insight[path[0]]


def elem_get(insight, key):
    if type(key) is not str:
        return None
    path = key.split(".")

    if type(insight) is list:
        res = [elem_get(x, key) for x in insight]
        return res

    if path[0] not in insight.keys():
        return None

    if len(path) > 1:
        return elem_get(insight[path[0]], ".".join(path[1:]))
    else:
        return insight[key]


# возвращает по имени
def dict_get(insights_list, name):
    path = name.split(".")
    res = []

    if not (type(insights_list) is list):
        insights_list = [insights_list]

    for insight in insights_list:
        temp = elem_get(insight, name)
        if temp:
            res += temp

    return res


# поиск в глубину с изменением найденых значений
def dfs(insights_list):
    if not (type(insights_list) is list):
        insights_list = [insights_list]

    for insight in insights_list:
        if not (type(insight) is dict):
            continue

        for key in insight.keys():
            dfs(insight[key])
            keys2rem = []
            if key == "table_columns":
                for x in insight[key]:
                    if x["unit"] != "EUR": keys2rem.append(x)
                for x in keys2rem: insight[key].remove(x)
            elif key == "metric_sums":
                for x in insight[key]:
                    if x["unit_key"] != "EUR":  keys2rem.append(x)
                for x in keys2rem: insight[key].remove(x)
            elif key == "report_name":
                if insight[key] == "device":
                    insight[key] = insight[key].upper()
            elif key == "page_id":
                if insight[key] == "(not set)":
                    insight[key] = None


def ins_to_dict(insights_list, key, val=""):
    if not val:
        val = key
    res = {}
    for i in range(len(insights_list)):
        if key not in insights_list[i].keys() or val not in insights_list[i].keys():
            continue
        res[i if key not in insights_list[i].keys() else insights_list[i][key]] = insights_list[i][val]
    return res


# считает сумму и среднее по заданному пути
def calculate(insights_list, name):
    arr = dict_get(insights_list, name)
    try:
        temp = []
        for x in arr: temp.append(int(x))
        return sum(temp), sum(temp) / len(temp)
    except Exception as e:
        print(e)


# сортирует по ключу первого уровня
def sort(insights_list, key):
    res = []
    for insight in insights_list:
        if key in insight.keys():
            res.append(insight)
    res.sort(key=lambda x: x[key])
    for insight in insights_list:
        if key not in insight.keys():
            res.append(insight)
    return res


def summary(period, api, summ, sum_level, sum_general, **kwargs):
    if period > 4 or period is None:
        period = 7
    if sum_general == 0:
        return None
    formula = {
        1: lambda: (summ * sum_level / sum_general) / period,
        2: lambda: (summ * sum_level ^ 2 / sum_general) / period,
        3: lambda: (sum_level / sum_general) / period,
        4: lambda: (sum_level * 100) / period
    }
    return formula[api]()


def calc_by_formula(insights_list):
    keys = ["period", "api", "metric_sums.sum", "metric_sums.sum_level", "metric_sums.sum_general"]
    res = []
    for insight in insights_list:
        if "metric_sums" not in insight.keys():
            continue
        for i in range(len(insight["metric_sums"])):
            insight["metric_sums"][i]["summ"] = insight["metric_sums"][i]["sum"]
            try:
                val = summary(**{**insight, **insight["metric_sums"][i]})
            except Exception as e:
                print(e)
            else:
                res.append(val)
    return res


def save(insights_list):
    with open('hw_out.json', 'w') as outfile:
        json.dump(insights_list, outfile, ensure_ascii=False, indent=4)