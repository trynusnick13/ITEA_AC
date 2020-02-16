from Nikita_Trynus.l_2_oopchik.hw_opchik import BaseInsight, MetricSummary
from Nikita_Trynus.l_1_functions.insights_hw import *
# hochu i importiruyu so zvezdochkoy


# ex. 1: in the previous h/w we differentiated classes by api, so I used that in this exercise
FacebookInsight = type('FacebookInsight', (BaseInsight,), {'dimensions_dict': None, 'dimensions': None, 'period': 3})
GoogleInsight = type('GoogleInsight', (BaseInsight,), {'actions': None, 'period': 7})
TwitterInsight = type('TwitterInsight', (BaseInsight,), {'first_date': None, 'last_date': None, 'period': 10})
SnapchatInsight = type('SnapchatInsight', (BaseInsight,), {'weight': None, 'type': None, 'period': 30})

# ex. 2:
list_of_metric_summary = get_all(insights, [], 'metric_summary')
needed_dict = dict(zip(list_of_metric_summary[0]['cpc'].keys(), [None] * len(list_of_metric_summary[0]['cpc'].keys())))
MetricSummary = type('MetricSummary', (), needed_dict)


if __name__ == '__main__':

    # a = BaseInsight()
    # print(a.api)
    # a.currency = 1
    # print(a.unit)

    list_of_insights = []
    for insight in insights:
        temp = object()
        if insight.get('api') == 1:
            temp = FacebookInsight()
            list_of_insights.append(temp)
            print(f'{type(temp).__name__}')

        elif insight.get('api') == 2:
            temp = GoogleInsight()
            list_of_insights.append(temp)
            print(f'{type(temp).__name__}')

        elif insight.get('api') == 3:
            temp = TwitterInsight()
            list_of_insights.append(temp)
            print(f'{type(temp).__name__}')

        else:
            temp = SnapchatInsight()
            list_of_insights.append(temp)
            print(f'{type(temp).__name__}')

        temp.metrics = insight.get('metric_summary')
        if temp.metrics is not None:
            print(temp.sum_of_metrics())
            pass